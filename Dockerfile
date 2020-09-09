FROM python:3.8-alpine

RUN apk -U add --no-cache ca-certificates build-base git openssh libffi-dev && \
    pip install locust==1.2.3

RUN mkdir /app
WORKDIR /app

COPY ./locustfile.py /app/locustfile.py

EXPOSE 8089
ENTRYPOINT [ "locust" ]
