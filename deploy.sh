#!/usr/bin/env bash

cd /Users/ilya/PycharmProjects/pushkin-netmiko
tar czvf netmiko.tar.gz netmiko
echo "put netmiko.tar.gz" |sftp -i ~/.ssh/id_rsa_berestenko i.berestenko@192.168.133.141
ssh -i ~/.ssh/id_rsa_berestenko i.berestenko@192.168.133.141 "tar xzvf netmiko.tar.gz; rm -rf /home/i.berestenko/.local/lib/python3.5/site-packages/netmiko; mv netmiko /home/i.berestenko/.local/lib/python3.5/site-packages/netmiko"

#ssh -i ~/.ssh/id_rsa_berestenko i.berestenko@192.168.133.141 "./sdn/restart_gunicorn.sh"
