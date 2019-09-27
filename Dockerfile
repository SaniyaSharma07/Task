FROM jenkins/jenkins:lts
USER root
FROM python:alpine3.6

# RUN apk add install -y git
RUN apk add --update && apk add -y git


RUN apk add --no-cache gcc

RUN apk add --no-cache git

RUN apk add --update bash && rm -rf /var/cache/apk/*


