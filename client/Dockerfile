# BUILD
FROM golang:1.18-alpine as build_uploader
RUN mkdir /usr/local/xpeed
WORKDIR /usr/local/xpeed
 
COPY uploader/go.mod ./
COPY uploader/go.sum ./
 
RUN go mod download
 
COPY uploader/*.go ./
 
RUN CGO_ENABLED=0 go build -o uploader
 
# DEPLOY
FROM debian:bullseye

RUN mkdir /usr/local/xpeed
WORKDIR /usr/local/xpeed

RUN apt-get update && apt-get install -y curl jq gnupg1 apt-transport-https dirmngr
# Pulling from package directly instead from the speedtest install page, as that is not working right now
RUN curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash
RUN apt-get install speedtest

COPY ./run.sh ./run.sh
COPY --from=build_uploader /usr/local/xpeed/uploader ./uploader

RUN chmod +x ./run.sh
RUN chmod +x ./uploader

CMD ["sh", "run.sh"]
