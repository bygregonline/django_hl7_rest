FROM alpine:3.11.5
MAINTAINER Greg Flores <www.aniachitech.com>
WORKDIR /root
RUN apk add git perl
RUN git clone https://github.com/jasonm23/cowsay.git
RUN pwd
WORKDIR /root/cowsay
RUN ./install.sh  /usr/local 
RUN /usr/local/bin/cowsay "ITS WORKING"
WORKDIR /
RUN apk upgrade --update
RUN /usr/local/bin/cowsay "Installing python "
RUN apk add python3 python3-dev  musl-dev nano
RUN apk add curl gcc
RUN /usr/local/bin/cowsay "Installing compilers  "
RUN apk add linux-headers
RUN /usr/local/bin/cowsay "Installing python dependencies"
RUN pip3 install --upgrade pip
RUN pip3 install django numpy
RUN pip3 install py-common-fetch gunicorn
RUN pip3 install json2html dicttoxml hl7apy pyyaml 
RUN /usr/local/bin/cowsay "Installing  nginx and dependencies"
RUN apk add  uwsgi-python3 uwsgi openrc sudo nano
RUN /usr/local/bin/cowsay "Installing app from github"
WORKDIR /home
RUN wget https://github.com/bygregonline/django_hl7_rest/raw/master/app.zip
RUN unzip * 
WORKDIR /home/app
RUN wget https://raw.githubusercontent.com/bygregonline/django_hl7_rest/master/run.sh
RUN chmod 777 run.sh
RUN /usr/local/bin/cowsay "ALL DONE"

ENTRYPOINT [ "sh","/home/app/run.sh" ]
EXPOSE 8000



