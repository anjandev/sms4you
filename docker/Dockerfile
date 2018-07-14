FROM debian:stretch-slim

# update and upgrade
RUN export DEBIAN_FRONTEND=noninteractive \
    && apt-get update -y && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    gammu \
    # gammu-smsd \
    python-gammu \
    python-pip \
    python-virtualenv \
    unzip \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

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
COPY files/gammu-smsdrc /etc/gammu-smsdrc
COPY files/gammurc /root/.gammurc

ENTRYPOINT ["/start.sh"]
