FROM python:3.6.8-alpine
ENV PYTHONUNBUFFERED 1  

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add fish postgresql-dev postgresql-client bash && \
    apk add openssl libressl libc-dev linux-headers libffi-dev \
    libxml2-dev libxml2 libxslt-dev openssh-client openssh-sftp-server

RUN mkdir /config  
ADD /config/requirements.txt /config/  
RUN pip install -r /config/requirements.txt
RUN mkdir /src
WORKDIR /src

