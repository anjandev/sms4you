FROM python:2.7-onbuild

ENV DEBIAN_FRONTEND noninteractive
ENV SHELL /bin/bash
ENV TERM xterm

# default necessary packages
RUN \
  apt-get update && \
  apt-get install -y curl && \
  apt-get install -y python && \
  apt-get install -y git-core && \
  apt-get install -y libmysqlclient-dev && \
  apt-get install -y cmake

# installing gammu
RUN \
  mkdir -p /usr/src/gammu && \
  mkdir -p /var/log/gammu && \
  git clone https://github.com/gammu/gammu.git /usr/src/gammu && \
  (cd /usr/src/gammu; git checkout tags/1.39.0 -b 1.39.0) && \
  (cd /usr/src/gammu; ./configure) && \
  (cd /usr/src/gammu; make) && \
  (cd /usr/src/gammu; make install)
# fixing error gammu-smsd: error while loading shared libraries: libGammu.so.7:
# cannot open shared object file: No such file or directory
# http://comments.gmane.org/gmane.linux.drivers.gammu/10260
RUN ldconfig

# python app port
EXPOSE 5000

# running python app
CMD ["bin/run"]


FROM debian:strech

VOLUME ["/etc/postfix"]
VOLUME ["/var/spool/gammu"]

EXPOSE 25

# apt-get install postfix liblog-log4perl-perl gammu ddclient

# postmap /etc/postfix/virtual 
# /etc/gammu-smsdrc
# /usr/local/bin/sms2mail.pl
# /usr/local/bin/smsgw.pl
# chmod o+rx /usr/local/bin/smsgw.pl
# chmod 700 /usr/local/bin/sms2mail.pl 
 
# /etc/init.d/gammu-smsd restart
 
tail -f /var/log/mail.log 


# mail -s "Test mail" -r 017696189204@sms.delattre.de sms@delattre.de < foo.txt 



ENV DEBIAN_FRONTEND noninteractive


CMD [ "start.sh", "start" ]