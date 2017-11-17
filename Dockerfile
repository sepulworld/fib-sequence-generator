FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./fib-sequence-generator /app
