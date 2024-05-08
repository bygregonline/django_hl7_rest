FROM alpine:3.19.1
MAINTAINER Greg Flores <www.aniachitech.com>
WORKDIR /root
RUN apk add git perl
RUN git clone https://github.com/jasonm23/cowsay.git
RUN pwd
WORKDIR /root/cowsay
RUN ./install.sh  /usr/local
RUN /usr/local/bin/cowsay "ITS WORKING"
WORKDIR /home

RUN apk upgrade --update
RUN /usr/local/bin/cowsay "Installing python "
RUN apk add python3 python3-dev py3-pip musl-dev nano
RUN apk add curl gcc
RUN /usr/local/bin/cowsay "Installing compilers  "
RUN apk add linux-headers
RUN apk add  uwsgi-python3 uwsgi openrc sudo nano
RUN /usr/local/bin/cowsay "Installing python dependencies"
RUN rm /usr/lib/python3.11/EXTERNALLY-MANAGED
COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt


RUN /usr/local/bin/cowsay "Installing  nginx and dependencies"

RUN /usr/local/bin/cowsay "Installing app from github"
WORKDIR /home
RUN wget https://github.com/bygregonline/django_hl7_rest/raw/master/app.zip
RUN unzip app.zip
WORKDIR /home/app
RUN wget https://raw.githubusercontent.com/bygregonline/django_hl7_rest/master/run.sh
RUN chmod 777 run.sh
RUN /usr/local/bin/cowsay "ALL DONE"

ENTRYPOINT [ "sh","/home/app/run.sh" ]
EXPOSE 8000



