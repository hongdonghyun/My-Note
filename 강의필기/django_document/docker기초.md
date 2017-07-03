#docker

```
docker run ubuntu:16.04

docker run --rm -it ubuntu:16.04 /bin/bash

docker ps

docker cp . <NAMES>:srv/<폴더이름>

docker build -t <사용할 이미지 이름> <dockerfile이 존재하는 경로>
```

## docker 내부세팅


```
apt-get update


apt-get install python-pip zsh curl

apt-get install git vim

apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils

apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

curl -L http://install.ohmyz.sh |sh

curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

vi ~/.zshrc
export PATH="/home/ubuntu/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 3.5.3

```

##레이어 나눈것들 한방실행

실행하려는 서버에 `dockerfile`생성(확장자 docker)

```
FROM ubuntu:16.04
MAINTAINER hong4367@gmail.com
RUN     apt-get -y update

RUN     apt-get install -y python-pip curl

RUN     apt-get install -y git vim
RUN     apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils

RUN     apt-get install -y libtiff5-dev libjpeg8-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk

RUN     curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

RUN     echo 'export PATH="/home/ubuntu/.pyenv/bin:$PATH"'>>~/.bash_profile
RUN     echo 'eval "$(pyenv init -)"'>>~/.bash_profile
RUN     echo 'eval "$(pyenv virtualenv-init -)"'>>~/.bash_profile
RUN     source ~/.bash_profile
RUN 	pyenv install 3.5.3


EXPOSE 4567
```

