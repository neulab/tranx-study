#!/bin/bash
# export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$UID/bus"
echo "Setting timezone..."
timezone=`wget -qO - http://geoip.ubuntu.com/lookup | sed -n -e 's/.*<TimeZone>\(.*\)<\/TimeZone>.*/\1/p'`

echo $timezone
sudo timedatectl set-timezone "$timezone"

# `timedatectl set-timezone` doesn't update `/etc/timezone`
# https://unix.stackexchange.com/q/451709/143394
#  <<<"$timezone" sudo tee /etc/timezone &> /dev/null

# printf '\ntimedatectl says:\n'
# timedatectl

# Update xfce4-panel clock
# https://unix.stackexchange.com/a/227405/143394
# if property=$(xfconf-query -c xfce4-panel --list | grep timezone); then
#     if [[ $(wc -l <<<"$property") -eq 1 ]]; then # only one clock widget
#         xfconf-query -c xfce4-panel -p "$property" -s "$timezone"
#         printf '\nUpdated xfce4-panel clock timezone to: %s\n' "$timezone"
#     else
#         >&2 printf 'Not changing multiple xfce4-panel properties:\n%s\n' "$property"
#     fi
# fi

xfconf-query --create -c xfce4-panel -t string -p "/plugins/plugin-5/timezone" -s "$timezone"
