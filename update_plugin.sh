#!/bin/bash

rm -f tranx_plugin-SNAPSHOT.zip
wget -q https://github.com/neulab/tranX-plugin/releases/latest/download/tranx_plugin-SNAPSHOT.zip
unzip -o -q tranx_plugin-SNAPSHOT.zip -d /home/vagrant/.local/share/JetBrains/PyCharmCE2020.1/
rm -f tranx_plugin-SNAPSHOT.zip

## make scripts exec-able
chmod +x /vagrant/*.sh

## disable PyCharm update notifications
echo '<application>
  <component name="NotificationConfiguration">
    <notification groupId="IDE and Plugin Updates" displayType="NONE" />
  </component>
</application>' > /home/vagrant/.config/JetBrains/PyCharmCE2020.1/options/notifications.xml
