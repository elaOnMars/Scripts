#!/bin/bash

# iptables logs are saved in /var/log/
# Regularly copy this file to a subdirectory and delete the file as it will probably becomes too big! 
cd /var/log/ | find ./iptables* -type f -size +500M -exec cp {} log.archive/. \; \
  && cat /dev/null > iptables.dropped

# Save the file in /etc/cron.daily to clean your log file(s)
