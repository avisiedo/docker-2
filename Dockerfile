# https://docs.docker.com/reference/dockerfile/
FROM docker.io/python:3.15.2-alpine3.23@sha256:32f06114a111c2467804d06194c5584f16804a78cfaf427fb1fcbb0b3391d0f1

ENV MI_CALCULO=2+2

COPY calculadora.py calculadora.py

ENTRYPOINT ["python3", "-m", "calculadora"]

