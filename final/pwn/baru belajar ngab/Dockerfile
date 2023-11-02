FROM archlinux:latest
RUN pacman -Syu --needed --noconfirm && pacman -Syu socat ncurses --noconfirm

RUN useradd -ms /bin/bash app
WORKDIR /home/app
RUN chown -R app:app /home/app && chmod 750 /home/app

USER app
