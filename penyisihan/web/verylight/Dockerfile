FROM ubuntu:focal

RUN apt-get update -y && apt-get install -y python3 python3-pip python3-dev

RUN useradd -m verylight

WORKDIR /home/verylight

COPY app.py .
COPY flag.txt .
COPY 0987364748373737463.txt .
COPY coomme_geeeett_youur_flek /

RUN chmod +rx app.py
RUN chmod +r /coomme_geeeett_youur_flek

RUN pip3 install flask

USER verylight

EXPOSE 1337

ENTRYPOINT ["python3"]

CMD ["/home/verylight/app.py"]
