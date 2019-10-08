FROM python:alpine3.6

# RUN apk add install -y git
RUN apk add --update && apk add -y git

COPY /var/jenkins_home/workspace/innote-temp/ /innote/