import sys
import os
import json
import signal
import logging

from mitmproxy import ctx
from datetime import datetime
from http.client import responses

LOG_FILE_PATH = "/vagrant/browser_requests.log"

"""
RequestsLogger is an addon for mitmdump that logs information about request
and response pairs to file. As it does not do any changes to the body of the
request/response, I advise to run it with `--set stream_large_bodies=1`,
which enables streaming of the request/response body.
"""

class RequestsLogger:

    def __init__(self):
        logging.basicConfig(filename=LOG_FILE_PATH,
                            filemode='a',
                            format='%(asctime)s\t%(message)s',
                            datefmt='%s',
                            level=logging.INFO)

        logging.info("Logging started")

    def done(self):
        logging.info("Logging stopped")
        logging.shutdown()

    """ 
    This hook function is called by `mitmdump` whenever a response is received from a target server.
    the flow object holds information about both request and response (the whole HTTP/s flow).
    """
    def response(self, flow):
        if flow.request.method == "GET" and flow.response.status_code == 200:
            logging.info(flow.request.url)
            
plugin = RequestsLogger()

addons = [
    plugin
]
