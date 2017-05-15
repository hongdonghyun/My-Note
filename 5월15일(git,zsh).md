#5월 15일

##git 설치법
brew install git


##Shell(셸) 설정

brew install zsh zsh-completions

curl -L http://install.ohmyz.sh | sh

확인법
echo $SHELL


##자주 사용하는 명령어 별칭 (alias)지정하기

alias

alias <사용할 명령어>="<명령어 내용>"

## Pycharm 별칭 지정 예시
alias py="open -a /Applications/PyCharm\ CE.app/Contents/MacOS/pycharm"

[git 라이프 사이클]
(/Users/hongdonghyun/projects/자료/git-lifecycle.png)

##git 사용법
[git 파일 수정하고 저장하기 설명 링크](https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EC%88%98%EC%A0%95%ED%95%98%EA%B3%A0-%EC%A0%80%EC%9E%A5%EC%86%8C%EC%97%90-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0)

파일을 만들어서 내용을입력한 후의 파일은 untracked상태에 있음 add전에 내용을 수정해도 상태는 안바뀜

_git add 파일이름_ add를 하면 상태가 뉴파일 or modified로 바뀜 (아직 untracked)에 존재 

add한 파일에 내용을 수정하면 modified에 존재하게됨

수정된 파일을 add하면 modified가 초록색(수정이 적용됨)으로 되고 commit준비 상태가 됨(스테이징 상태)

commit을하게되면 nothing to commit이 뜸


**git init** :git 폴더 설정

**rm -rf .git** :파일 지우기 (-rf 하위폴더도 안물어보고 다 지움)

**status** : 변경사항보기 
(최초변경파일 untracked 파일에 저장됨)

**git log** : 추가되었던 로그 보기

**touch** :파일 만들기

**git add** : git 폴더에 추가한다 스테이지 영역에 추가됨(add --all 전부추가)

**git commit -m** :파일을 git에 올린다

**git diff --staged** : 스테이지 영역과 비교

**git diff** : modified영역과 비교?

**git mv** : 파일이름 바꾸기
*vim써서 파일만들기*

**리눅스 파일 링크 걸기** : ln -s 원본파일 링크걸곳주소