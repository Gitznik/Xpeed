FROM debian:buster

RUN mkdir /usr/local/xpeed
WORKDIR /usr/local/xpeed

RUN apt-get update && apt-get install -y curl jq gnupg1 apt-transport-https dirmngr
RUN curl -s https://install.speedtest.net/app/cli/install.deb.sh | bash
RUN apt-get install speedtest

COPY ./run.sh ./run.sh
RUN chmod +x ./run.sh

CMD ["sh", "run.sh"]