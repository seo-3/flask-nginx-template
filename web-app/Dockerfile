
FROM python:3.6

RUN mkdir /var/www
# workdirの指定
WORKDIR /var/www

COPY app/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update \
    && apt-get install -y mysql-client

WORKDIR /var/www/app

CMD ["uwsgi","--ini","/var/www/app/uwsgi.ini"]
