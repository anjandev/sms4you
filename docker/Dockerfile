FROM debian:stretch-slim

# update and upgrade
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -y && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    cron \
    gammu \
    python-gammu \
    python-pip \
    python-virtualenv \
    unzip

# add cron for regular execution of sms4you
ADD files/crontab /etc/cron.d/sms2you
RUN chmod 0644 /etc/cron.d/sms2you
RUN mkfifo --mode 0666 /var/log/cron.log \
# make pam_loginuid.so optional for cron
# see https://github.com/docker/docker/issues/5663#issuecomment-42550548
    && sed --regexp-extended --in-place \
    's/^session\s+required\s+pam_loginuid.so$/session optional pam_loginuid.so/' \
    /etc/pam.d/cron

# install sms4you
ADD https://github.com/xamanu/sms4you/archive/master.zip sms4you.zip
RUN unzip sms4you.zip \
    && rm sms4you.zip \
    && mv /sms4you-master /sms4you

WORKDIR /sms4you

RUN pip install setuptools
RUN pip install -e .

ADD files/start.sh /start.sh
COPY files/sms.py /sms.py
COPY files/gammurc /root/.gammurc

ENTRYPOINT ["/start.sh"]
CMD ["daemon"]

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
