FROM python

WORKDIR /app
COPY . /app

RUN set -xe \
    && apt-get update \
    && apt-get install python3-pip -y

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8080

RUN python3 insert_data.py
RUN python3 app.py