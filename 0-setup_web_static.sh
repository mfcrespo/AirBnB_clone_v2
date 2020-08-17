#!/usr/bin/env bash
#Install Nginx
sudo apt-get update
sudo apt-get -y install nginx
#create directories
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
#create a fake HTML file
echo -e "<html>\n    <head>\n    </head>\n    <body>\n        Holberton School\n    </body>\n</html>" > /data/web_static/releases/test/index.html
#create a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
#Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/
#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}" /etc/nginx/sites-available/default
#Apply changes to nginx
sudo service nginx restart
