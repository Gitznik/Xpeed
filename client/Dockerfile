# BUILD
FROM golang:1.18-alpine as build_uploader
RUN mkdir /usr/local/xpeed
WORKDIR /usr/local/xpeed
 
COPY uploader/go.mod ./
COPY uploader/go.sum ./
 
RUN go mod download
 
COPY uploader/*.go ./
 
RUN go build -o /uploader
 
# DEPLOY
FROM debian:buster

RUN mkdir /usr/local/xpeed
WORKDIR /usr/local/xpeed

RUN apt-get update && apt-get install -y curl jq gnupg1 apt-transport-https dirmngr
RUN curl -s https://install.speedtest.net/app/cli/install.deb.sh | bash
RUN apt-get install speedtest

COPY ./run.sh ./run.sh
COPY --from=build_uploader /uploader /uploader

RUN chmod +x ./run.sh

CMD ["sh", "run.sh"]
