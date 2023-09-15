FROM python:3-alpine

WORKDIR /var/www/html

COPY . /var/www/html/

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "./api.py" ]