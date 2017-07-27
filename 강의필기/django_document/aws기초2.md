export DJANGO_SETTINGS_MODULE =config.settings.debug

> uWSGI
웹 서버(Nginx)와 웹 애플리케이션(Django)간의 연결을 중계해준다.
(Nginx에서 받은 요청을 Django에서 처리하기 위한 중계인 역할을 해준다)

> Nginx
웹 서버. 클라이언트로부터의 HTTP요청을 받아 정적인 페이지/파일을 돌려준다.


# uwsgi

1편에서 ec2에 django를 올려 로컬동작을 확인 했다면 이제 uwsgi와 nginx로 평생 돌리는 작업을 해줘야 한다.

이놈들은 평생 서버만 돌리다 죽을것이다.
_local_

```
config/settings/deploy.py 
생성
```

_sever_

```
sudo adduser user_name
```

평생 서버를 돌릴 노예를 하나 만든다.

```
virtualenv 환경 내부에서 실행

pip install uwsgi

그 후 동작하는지 한번 돌려보자

uwsgi --http :8080 --home (virtualenv경로) --chdir (django프로젝트 경로) -w (프로젝트명).wsgi

헷갈릴 나를 위해 예시를 보자
uwsgi --http :8000 --home ~/.pyenv/versions/aws_practice --chdir /srv/aws_practice/django_app -w config.wsgi
```
>wsgi.py 안에
>os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.debug")
>이렇게 수정해야 실행됨

wsgi는 분할이 가능하다.


`config` 안에 `wsgi`패키지를 만들고
`debug.py` `deploy.py` 를 만든다

_config/settings/deploy.py_
_config/settings/debug.py_

```
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.( debug or deploy )")
<< ^ 여기가 다르다>>
application = get_wsgi_application()
```

## uwsgi.ini
분할을 하고 난 이후 uwsgi.ini를 만들어 보자

_`.config_secret`_안에 `uwsgi`폴더를 만들고 `deploy.ini`를 만들자

_`.config_secret/uwsgi/deploy.ini`_

```
[uwsgi]
home = /home/ubuntu/.pyenv/versions/aws_practice
chdir = /srv/aws_practice/django_app
module = config.wsgi.deploy

uid = deploy
gid = deploy

socket = /tmp/ec2.sock
chmod-socket = 666
chown-socket = deploy:deploy

enable-threads = true
master=true

vacuum = true

```

ini(대통령아님)파일을 작성 했다면 동작하는지 확인해보자.

```
uwsgi --ini .config_secret/uwsgi/deploy.ini
```
잘된다.

## nginx
`.config_secret`에 `nginx`폴더를 만들고 `ngix.conf`파일과 `ec2.conf`를 만든다

이해할 자신이 없으니 일단 외우자

_`.config_secret/nginx/ec2.conf`_

```
server {
    listen 80;
    server_name *.compute.amazonaws.com;
    charset utf-8;
    client_max_body_size 128M;

    location / {
        uwsgi_pass      unix:///tmp/ec2.sock;
        include         uwsgi_params;
    }
}

```

_`.config_secret/uwsgi/uwsgi.service`_

```
[Unit]
Description = uWSGI service
After=syslog.target

[Service]
ExecStart=/home/ubuntu/.pyenv/versions/aws_practice --ini srv/aws_practice/.config_secret/uwsgi/deploy.ini

Restart=always
KillSignal=SIGQUIT
Type=notify
StandardError=syslog
NotifyAccess=all

[Install]
WantedBy=multi-user.target
```

`sudo adduser deploy`를 하자

유저를 만들었다면

```
sudo /home/ubuntu/.pyenv/versions/aws_practice/bin/uwsgi --http :8000 --ini /srv/aws_practice/.config_secret/uwsgi/deploy.ini
```
sudo권한으로 ini파일을 실행해본다.

정상실행이 되었다면 도메인:8000으로 접속해보자 internal server error, 400에러가 뜨지 않았다면 성공이다.

**만약 에러가뜬다면 오타찾기를 먼저하자.**

다시 서버에서 nginx를 설치를 해보자

```
sudo apt-get install software-properties-common python-software-properties
sudo add-apt-repository ppa:nginx/stable
sudo apt-get update
sudo apt-get install nginx
nginx -v
```
마지막으로 nginx버전이 나왔는지 확인해보자

ex) `nginx version: nginx/1.12.0`

정상출력되면 아주 잘 깔린것이다.

`sudo cat /etc/nginx/nginx.conf`를 해서 비어있는 nginx.conf의 파일에 붙여넣기를 하자

_`sudo cat /etc/ngninx/nginx.conf를 하면 나오는코드`_

```
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
	worker_connections 768;
	# multi_accept on;
}

http {

	##
	# Basic Settings
	##

	sendfile on;
	tcp_nopush on;
	tcp_nodelay on;
	keepalive_timeout 65;
	types_hash_max_size 2048;
	# server_tokens off;

	# server_names_hash_bucket_size 64;
	# server_name_in_redirect off;

	include /etc/nginx/mime.types;
	default_type application/octet-stream;

	##
	# SSL Settings
	##

	ssl_protocols TLSv1 TLSv1.1 TLSv1.2; # Dropping SSLv3, ref: POODLE
	ssl_prefer_server_ciphers on;

	##
	# Logging Settings
	##

	access_log /var/log/nginx/access.log;
	error_log /var/log/nginx/error.log;

	##
	# Gzip Settings
	##

	gzip on;
	gzip_disable "msie6";

	# gzip_vary on;
	# gzip_proxied any;
	# gzip_comp_level 6;
	# gzip_buffers 16 8k;
	# gzip_http_version 1.1;
	# gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

	##
	# Virtual Host Configs
	##

	include /etc/nginx/conf.d/*.conf;
	include /etc/nginx/sites-enabled/*;
}


#mail {
#	# See sample authentication script at:
#	# http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
#
#	# auth_http localhost/auth.php;
#	# pop3_capabilities "TOP" "USER";
#	# imap_capabilities "IMAP4rev1" "UIDPLUS";
#
#	server {
#		listen     localhost:110;
#		protocol   pop3;
#		proxy      on;
#	}
#
#	server {
#		listen     localhost:143;
#		protocol   imap;
#		proxy      on;
#	}
#}
```

`username`은 아까  adduser했던 유저로 바꿔주고 `server_names_hash_bucket_size`를 250으로 바꾸고 주석을 풀자

로컬에서 바꿨으니 당연히 서버로 전송해주자 `scp`명령어를 쓰도록

```
sudo cp -f /srv/aws_practice/.config_secret/nginx/nginx.conf /etc/nginx/nginx.conf

sudo cp -f /srv/aws_practice/.config_secret/nginx/ec2.conf /etc/nginx/sites-available/

sudo ln -sf /etc/nginx/sites-available/ec2.conf /etc/nginx/sites-enabled/ec2.conf

sudo cp -f /srv/aws_practice/.config_secret/uwsgi/uwsgi.service /etc/systemd/system/uwsgi.service

sudo rm -rf /etc/nginx/sites-enabled/default
```

```
sudo systemctl restart uwsgi

sudo systemctl restart nginx
```
