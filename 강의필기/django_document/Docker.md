[참고할사이트](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
# Docker
docker run ubuntu:16.04

docker run --rm -it -p 9000:8000 ubuntu:16.04 /bin/bash

docker build . -t eb_ubuntu -f .dockerfiles/Dockerfile.ubuntu

docker tag 이미지이름 태그이름

docker push hong4367/eb_ubuntu



## 초기세팅

폴더에 `pip install django` 설치
`.gitignore` 파일 복사 or 생성
`django-admin startproject projectname`

`pyenv virtualenv x.x.x env_name`

`pyenv local env_name`

프로젝트 구조화

- .config_secret 폴더	
- .settings 모듈
- .wsgi 모듈
	
`소스루트 지정 및 인터프리터 설정`

`pip freeze > requirement.txt`
	
git init 및 remote 저장소 추가
commit하기	
**필수체크 .gitignore에 내용 이 다들어갔는지**

settings 파일 모듈화

wsgi 모듈화 하기

.dockerfiles 모듈화

.requirements 모듈화

자세한 파일트리는 [practice_docker](https://github.com/hongdonghyun/practice_docker/tree/master/django_app/config/settings)

github로
