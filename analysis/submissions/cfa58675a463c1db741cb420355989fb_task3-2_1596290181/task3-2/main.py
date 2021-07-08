# Example code, write your program here

import json
import os


class TxtSub(object):
    def __init__(self, o):
        self.o = o
        self.result = dict()

    def add(self, root, file):
        d = root.split('/')[-1]
        if d not in self.result:
            self.result[d] = list()
        with open(os.path.join(root, file)) as f:
            self.result[d].append(f.read())

    def output(self):
        for k, v in self.result.items():
            with open(os.path.join(self.o, k + '.txt'), 'w') as f:
                f.flush()
                f.write(''.join(v))


class JsonSub(object):
    def __init__(self, o):
        self.o = o
        self.result = dict()

    def add(self, root, file):
        d = root.split('/')[-1]
        if d not in self.result:
            self.result[d] = list()
        with open(os.path.join(root, file)) as f:
            self.result[d].append(json.loads(f.read()))

    def output(self):
        for k, v in self.result.items():
            with open(os.path.join(self.o, k + '.json'), 'w') as f:
                f.flush()
                o = list()
                i = 1
                for ff in v:
                    for ll in ff:
                        o.append({
                            "id": i,
                            "first_name": ll['first_name'],
                            "last_name": ll['last_name'],
                            "email": ll['email'],
                            "gender": ll['gender'],
                            "ip_address": ll['ip_address'],
                        })
                        i += 1
                f.write(json.dumps(o))


ts = TxtSub('output')
js = JsonSub('output')

for root, subdirs, files in os.walk('data'):
    for file in files:
        if '.txt' in file:
            ts.add(root, file)
        if '.json' in file:
            js.add(root, file)

ts.output()
js.output()
