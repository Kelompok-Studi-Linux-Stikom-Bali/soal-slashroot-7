FROM ubuntu:20.04

RUN apt-get update && apt-get install -y xinetd && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/xinetd.d/*
RUN useradd -U -m heaphop && mkdir -p /home/heaphop
RUN chown -R root:heaphop /home/heaphop && chmod 750 /home/heaphop

CMD /usr/bin/startchall
