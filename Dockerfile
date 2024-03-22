FROM ubuntu:latest
LABEL authors="kamal"

ENTRYPOINT ["top", "-b"]