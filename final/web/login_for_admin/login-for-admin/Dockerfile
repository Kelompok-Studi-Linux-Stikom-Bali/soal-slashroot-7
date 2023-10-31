FROM php:8.0-apache

RUN docker-php-ext-install mysqli 
RUN chmod 755 -R /var/www/html

# Create and switch to a user called app
RUN useradd -ms /bin/bash app
USER app

COPY --chown=app:app . /var/www/html
# COPY ./config/php.ini /usr/local/etc/php/php.ini