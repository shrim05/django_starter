FROM python:3.8-slim-buster AS builder
RUN apt-get update &&  apt-get install -y apt-utils vim gcc default-libmysqlclient-dev
COPY django_start.sh /
COPY wait-for-db.sh /
COPY wait-for-db.py /

WORKDIR /app
COPY    requirements/   /app/requirements/
RUN    pip install -r /app/requirements/dev.txt

COPY . /app
RUN chmod +x /django_start.sh
RUN chmod +x /wait-for-db.sh
# CMD ["/django_start.sh"]
