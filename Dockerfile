FROM python:3-slim

COPY setup.py /src/
COPY sb8200_exporter /src/sb8200_exporter/

RUN pip install --upgrade /src

EXPOSE 9195

CMD ["/usr/local/bin/sb8200_exporter"]
