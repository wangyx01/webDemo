# webDemo
Django web demo
# uwsgi.ini
```
[uwsgi]
socket = :8000
chdir = /root/Single/webDemo/website    --manage.py的上级目录
wsgi-file = webDemo/wsgi.py
processes = 2
threads = 4
vacuum = true
max-requests = 1000
limit-as = 512
buffer-size = 30000
pidfile = /var/run/uwsgi.pid
daemonize = /var/log/uwsgi.log
harakiri = 60
```
# /etc/nginx/conf.d/https.conf
```
upstream django {
    server 127.0.0.1:8000;
}
server {
    listen      8080;
    server_name 192.168.47.148;
    charset     utf-8;
 
    client_max_body_size 75M;
 
    location /static {
        alias /root/Single/webDemo/website/static;
    }
 
    location / {
        uwsgi_pass  django;
        include     /etc/nginx/uwsgi_params;
    }
}
```
