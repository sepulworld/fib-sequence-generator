FROM tiangolo/uwsgi-nginx-flask:python3.6

ARG VCS_REF

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/sepulworld/fib-sequence-generator"

COPY ./fib-sequence-generator /app
