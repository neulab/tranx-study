#!/bin/bash

# remove existing profiles
rm -rf /home/vagrant/.mozilla/firefox/dqy0r712.default-release/
rm -rf /home/vagrant/.mozilla/firefox/m9ztmqyf.default/

unzip -o -q /vagrant/firefox-profile.zip -d /home/vagrant/.mozilla/firefox/