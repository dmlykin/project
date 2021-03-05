#!/usr/bin/env bash

if [ -z "$1" ]
then
    echo "Specify container name"
    exit 1
fi

if [[ ! $(docker images project:dev | tail -1 | grep project) ]]
then
  docker build -t project:dev dev --build-arg UID=$(id -u $(whoami)) --build-arg GID=$(id -g $(whoami))
fi

if [[ $(docker ps -f name=$1 | tail -1 | grep $1) ]]
then
    echo Already started
elif [[ $(docker ps -f name=$1 -a | tail -1 | grep $1) ]]; then
    docker start $1
else
    docker run -d -P -v $(readlink -e ../):/home/developer/project \
    --name=$1 \
    --ipc=host \
    project:dev
fi
