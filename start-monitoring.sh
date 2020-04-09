#!/bin/bash
rm -f browser_requests.log
/usr/local/bin/mitmdump -q --set stream_large_bodies=1 -s /vagrant/browser-request-logger.py &
