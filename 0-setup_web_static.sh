#!/usr/bin/env bash
# Preparing my WebServers for my App

# installing The NGINX webserver
apt-get update
apt-get install -y nginx

# Making some directories
mkdir /data/
mkdir /data/web_static/
mkdir /data/web_static/releases/
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
echo "Hello Allem" >/data/web_static/releases/test/index.html

# Making a Symbolic link
ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

# Changing the owner of a folder and all of its contents
chown -R ubuntu:ubuntu /data/

printf %s "server {

        listen 80 default_server;
        listen [::]:80 default_server;
        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;
        add_header X-Served-By $HOSTNAME;


        location /hbnb_static {
            alias /data/web_static/current;
            index index.html index.htm index.nginx-debian.html;
        }
}" >/etc/nginx/sites-available/default
service nginx restart
exit 0
