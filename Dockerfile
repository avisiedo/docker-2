# https://docs.docker.com/reference/dockerfile/
FROM docker.io/python:3.15.2-alpine3.23

ENV MI_CALCULO=2+2

COPY calculadora.py calculadora.py

ENTRYPOINT ["python3", "-m", "calculadora"]

