FROM ubuntu:20.04

RUN apt-get update && apt-get install -y xinetd && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*
RUN useradd -U -m lealpop && mkdir -p /home/lealpop
RUN chown -R root:lealpop /home/lealpop && chmod 750 /home/lealpop

CMD /usr/bin/startchall
