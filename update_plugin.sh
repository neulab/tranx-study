#!/bin/bash

rm -f tranx_plugin-SNAPSHOT.zip
wget -q https://github.com/neulab/tranX-plugin/releases/latest/download/tranx_plugin-SNAPSHOT.zip
unzip -o -q tranx_plugin-SNAPSHOT.zip -d /home/vagrant/.local/share/JetBrains/PyCharmCE2020.1/
rm -f tranx_plugin-SNAPSHOT.zip

## for post-task survey
pip3 install questionnaire
