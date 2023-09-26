FROM python:3

RUN useradd -m sangchall

WORKDIR /home/sangchall

COPY chall.py .
COPY flag /

RUN chmod +rx chall.py
RUN chmod +r /flag

RUN apt update

RUN apt install -y \
    socat

USER sangchall

EXPOSE 1337

ENTRYPOINT socat tcp-l:1337,fork,reuseaddr exec:"python chall.py"
