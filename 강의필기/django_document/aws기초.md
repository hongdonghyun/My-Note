수업에 배운 내용을 토대로 개인적으로 사용하는 문서이며 사실이 아닐수도 있습니다.


이 문서에서는 `django` 설치, `pyenv`설정, `secret_key` 폴더 설정, `aws` 연동과 실행등을 다룰 예정입니다.

#가상환경 설치 및 django설치

1. `pyenv virtualenv x.x.x name`

2. `pip install django`

3. ```git init, .gitignore, pip freeze > requirement.txt, README.md``` 작성

4. 기존의 프로젝트를 사용 하거나 생성
 - ```django-admin startproject name```

5. `source root` 지정 및 인터프리터 설정

# django deploy 

## deployment checklist
github에 `secret_key`가 올라가면 큰 문제가 발생 하므로 `.gitignore`에 추가 하기 위한 작업을 먼저 진행한다.
`.config_secret` 폴더 안에 들어가는 파일은 `json`형식을 사용한다.

`json`파일 안에서는 `''`가 먹히지 않으니 `""`를 사용하자. `,`사용에도 주의하자.

### 폴더 생성
`django project`안에서 `.config_secret`폴더 생성
 
```
settings_common,
settings_debug,
settings_deploy.json
파일 생성
``` 
common.json
```
{"django":{"secret_key":django project secret_key}}
```
debug.json 
```
{"django":{"allowed_hosts":"*"}}
```
deploy.json
```
{"django":
{"allowed_hosts":"*"}}
```
  
> 2.settings_common.json 파일은 배포환경과 개발환경에서 둘다 사용할 비밀값을 넣는 파일	
> 들어가야 하는 값들은 `debug`,`ALLOWED_HOST`,`secret_key` 등이 있다.
> 자세한건 [여기](https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/)를 참고하도록 한다.

### settings.py 분할
1. `config(프로젝트 생성시 생긴 폴더)`안에 `settings`패키지를 생성하여 `base.py`를 생성한다.

2. `base.py`안에 기존에 있던 `settings.py` 의 내용을 넣고 
`settings.py`는 삭제한다.

3. `base.py`안에 `.config_secret`폴더 안에 있는 `json`파일을 불러온다
> **주의**
> `config`폴더 안에 `settings`패키지를 하나 더 생성 하였기 때문에 기존의 `BASE_DIR`을 바꿔줘야한다.
>  기존 `BASE_DIR`에 `os.path.dirname`을 한번 더 씌운다 (os.path.dirname)은 상위폴더로 가게 해준다
> **!!아주중요!!**	
> **.gitignore에 폴더를 추가해준다**

4. 각자 방법은 다를 수 있으나 수업에서 배운 내용대로 사용했다.
 
_config/settings/base.py_

```
ROOT_DIR = os.path.dirname(BASE_DIR)

CONFIG_SECRET_DIR= os.path.join(ROOT_DIR,'.config_secret)

CONFIG_SECRET_COMMON_FILE = os.path.join(CONFIG_SECRET_DIR,'settings_common.json)'

CONFIG_SECERT_DEBUG_FILE =
os.path.join(CONFIG_SECRET_DIR,'settings_debug.json')

CONFIG_SECRET_DEPLOY_FILE =
os.path.join(CONFIG_SECRET_DIR,'settings_deploy.json'

config_secret_common = json.loads(open(CONFIG_SECRET_COMMON_FILE).read())


SECRET_KEY = config_secret_common["django"]["secret_key"]

debug와 allowed는 삭제
```
**commit하세요.**

_config/settings/debug.py_

```
from .base import *

config_secret_debug =json.loads(open(CONFIG_SECRET_DEBUG_FILE).read())

DEBUG = True
ALLOWED_HOSTS = config_secret_debug["django"]["allowed_hosts"]


```

>앞으로 **runserver는./manage.py runserver --settings=config.settings.debug** 로 한다.

## READ.MD 생성 및 작성
[작성방법은 여기를 참고한다.](https://drive.google.com/open?id=0B-9HQxuZ0uRNbnZRQU5DVW9lMEk)

# aws배포 기초
로그인 후 EC2 create

Launch를 누르면 key pair에 관한 내용이 나온다.

간단히 내용을 정리해 보자면 데이터베이스에 접근권한을 얻기위해선 기본키로 복호화를 해줘야 하니 기본키를 가지고 있으라는 내용이다.

실제 aws에서 RSA로 암호화를 하고 있기 때문에 기본키는 **절대** 유출이 되어선 안된다.

기본키는 만드는순간에만 저장이 가능하니 반드시 저장하도록 하자

`create a new key pair`를 선택
이름은 취향껏 정한다.

[기본설정과 설명이 담긴 github](https://github.com/hongdonghyun/Deploy/blob/master/01.%20EC2.md)

저장한 기본키 파일을 ssh파일에 옮기도록 한다.
` mv 저장된곳/privatekeyname ~/.ssh`
이후 생성하고 이름을 정해준다.

하단에 Public DNS가 나오는게 이것이 우리가 사용할 주소가 된다.

그리고 key 파일에 대한 권한을 자기자신만 사용할 수 있도록 바꿔준다.

터미널에서 .ssh폴더로 이동 후 `chmod 400 privatekeyname`을 하면 읽기전용으로 바뀐다.

## ssh설치 및 사용 
우분투와 macOS는 기본적으로 깔려있다.

[관련문서](http://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

privatekey권한 설정까지 마쳤다면 이제 서버에 접속해보도록 하자

`ssh -i ~/.ssh/<기본키> <user@><Public DNS)`를 입력한다.

>작성자는 ubuntu 서버를 사용했기 때문에 user가 ubuntu가 된다.
자세한 내용은 문서를 참고한다.
>접속주소를 어딘가에 저장해서 사용해놓는것이 좋다 (매우길다)

입력을 하게 되면 불안한 메시지가 뜨는데 겁먹지 말도록 하자
aws에서 `님 진짜 접근할거? ㄹㅇ? ` 이렇게 물어보고 있는것이다.

>문자에서 fingerprint is SHA256 줄줄줄 나오는데 SHA256방식을 통해 기본키와 공개키로 해싱을 한 값이 나오고 있다.(맞나?)
>
>aws key Pair카테고리에 들어가면 볼 수 fingerprint값을 볼 수 있다.
>
>이 값을 통해 내가 접근하려는 서버가 맞는지 확인을 해줄 수 있다.

이 문서를 보고 따라오고 있다면 처음 접속하는 것이니 yes를 입력한다.

접속했다면 서버에 접속한것을 확인할 수 있다.

이후 **로컬**셸을 하나 더 열어서
위에서 작업했던 프로젝트로 들어가서
`pip install awscli`를 설치한다.
>awscli 는 로컬에서 aws서버를 관리하게 해주는 commandline tool이다[관련문서](https://aws.amazon.com/ko/cli/)

`aws ec2 get-console-output --instance-id 자신의 서버 instanceID`
를 입력하면 `aws configure`가 없다고 나올것이다.

설정을 aws홈페이지로 가서
`service`-> `iam`검색 후 `User`로 가면 `AddUser`를 해줄 수 있다.
만들어주자

Acess type을 알아서 설정 하도록 한다.

작성자는 CLI에서 사용하기 때문에
`Programmatic access`만 사용한다.
완료했다면 next로 넘어간다.

만든User는 아무 권한이 없기 때문에
`Attach existing policies directly`를 눌러 권한을 준다.

EC2를 검색하여 `EC2Fullaccess`가 적힌 권한 하나만 준다. 

계속 진행하여 `complete`단계에서
`AccesskeyID`와 `Secret access key`를 얻을 수 있는데
여기서만 보여주고 다신 안보여준다.

download를 눌러서 받아오던지 따로 적어주던지는 취향껏 한다.
이 값들을 셸에서 `aws configure`를 입력하면 나오는 창에 적어준다.

`default region`에는 `ap-northeast-2`를 적어준다 여기가 한국이다.
>1은 일본이라고한다.

완료를 했다면 `aws ec2 get-console-output --instance-id 자신의 서버 instanceID` 입력하여 다시 들어가면 들어가진것을 확인할 수 있다.

### aws configure 값을 보고 싶을때
 홈폴더(`~`)에서 `.aws`에 접근하면 `config`,`credentials`파일 두개가 보인다.
 
`config`는 기본 설정된 값들을 볼 수 있고
`credentials`에서는 `access_key_id`와 `secret_acess_key`값을 볼 수있고 바꾸는것도 가능하다.


## ubuntu 기본 설정

`echo $SHELL`을 입력하면 기본 셸이 bash로 나온다.
이것을 zsh로 바꿔줄 것이다.

_설치시 아카이브 어쩌고 에러 뜬다면_
`sudo apt-get update`

_python-pip 설치_
`sudo apt-get install python-pip`

_zsh 설치_
`sudo apt-get install zsh`

_oh-my-zsh 설치_
`sudo curl -L http://install.ohmyz.sh | sh`

_Default shell 변경_
`sudo chsh ubuntu -s /usr/bin/zsh`

위 과정을 한 후 서버를 나갔다 들어와서
`echo $SHELL`을 입력하면 `zsh`이 깔린걸 확인할 수 있다.

_pyenv requirements설치_
[공식문서](https://github.com/pyenv/pyenv/wiki/Common-build-problems)
```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils
```

_pyenv 설치_
```
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
```

_pyenv 설정 .zshrc에 기록_

```
최하단에 적어준다.
vi ~/.zshrc
export PATH="/home/ubuntu/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

_Pillow 라이브러리 설치_
```
sudo apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk
```

다 설치 했으면 나갔다 들어오자
>zshrc에 alias로 명령어를 등록해두면 편하다.

```
#연결
alias con-ec2="ssh -i ~/.ssh/키값 유저이름@Public DNS"


#삭제
alias delete-ec2="ssh -i ~/.ssh/키값 유저이름@Public DNS rm -rf 삭제할 주소"


#생성
alias scp-ec2-ori="scp -i ~/.ssh/키값 -r 가지고올 로컬 주소 유저이름@Public DNS:생성할 주소"

#업데이트
alias scp-ec2="delete-ec2 && scp-ec2-ori"
```

다시 설정을 하자

_Django 관련 설정_
`sudo chown -R ubuntu:ubuntu /srv/`
>srv 파일의 owner를 ubuntu로 바꾼다

[관련문서](http://www.thegeekstuff.com/2010/09/linux-file-system-structure/?utm_source=tuicool)

_pyenv 설치_
```
pyenv install 3.5.3
pyenv virtualenv 로컬가상환경이름
pyenv local 로컬가상환경이름
```

_requirement 설치_
```
pip install -r requirements.txt
```

_runserver 테스트_

```
cd 폴더
./manage.py runserver --settings=config.settings.debug
```
>./manage.py runserver --settings=config.settings.debug 0:8000을 하면 밑의 과정을 한 후 접근이 가능하다.

##aws security group

create security group을 누른다

name ,description 을 적어준다
>description은 설명을 적는다

Add Rule을 눌러서
`ssh 22` `port source는 Myip`
`CustomTCP 8000`

instance로 돌아가서 `action` `networking` `security group`을 설정한 네임으로 바꿔준다
>launch wizard는 해제한다
 
#끝