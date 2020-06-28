FROM python:3.8.2

ENV PYTHONUNBUFFERED 1

EXPOSE 8081

RUN mkdir /cats-server
WORKDIR /cats-server

COPY . /cats-server/
RUN pip install -r requirements.txt



