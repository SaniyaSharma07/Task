FROM python:alpine3.6

# RUN apk add install -y git
RUN apk add --update && apk add -y git

COPY innote-backend/ /innote/

RUN apk add --no-cache gcc

RUN apk add --no-cache git

RUN apk add --update bash && rm -rf /var/cache/apk/*

RUN apk add --no-cache --virtual build-deps \
    libressl-dev \
    make \
    libc-dev \
    musl-dev \
    linux-headers \
    pcre-dev \
    libffi \
    libffi-dev

WORKDIR innote/
RUN ls
RUN pip install --upgrade pip

RUN pip install -r requirements.txt

RUN mkdir -p /var/log/innote_logs

RUN chmod +x start.sh

RUN chmod +x celery_start.sh