# docker2

```
docker rm $(docker ps -a -q)

docker rmi $(docker images | grep "^<none>" | awk "{print $3}")
```

## docker autocomplete
```
mkdir -p ~/.zsh/completion

curl -L https://raw.githubusercontent.com/docker/compose/master/contrib/completion/zsh/_docker-compose > ~/.zsh/completion/_docker-compose

vi ~/.zshrc
fpath=(~/.zsh/completion $fpath)
autoload -Uz compinit && compinit -i
추가

exec $SHELL -l 셸 리로드
```

## v

```
docker run --rm -it -p 9000:8000 eb /bin/zsh


도커 똑같은거 더 킬때
docker exec -it <NAMES> or <CONTAINER ID> /bin/zsh

docker run --rm -it -p 9000:80 eb /bin/zsh
```


## rdbs

```
psql --host=RDBSHOST--port=POSTGRES PORT --username=USER --dbname=DANAME
```

```
eb init

eb create
```