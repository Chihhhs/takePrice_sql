FROM python

WORKDIR /app
COPY . /app
RUN ["pip", 'install', '-r', 'requirements.txt']
EXPOSE 8080
RUN ["python", "app.py"]