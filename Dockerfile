FROM python:3.7-alpine
WORKDIR /opt/app
copy . /opt/app

CMD ["python3","project1.py"]
