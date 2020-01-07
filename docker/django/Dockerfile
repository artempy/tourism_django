FROM python:3.6
ENV PYTHONUNBUFFERED 1

COPY ./src /www/src
WORKDIR /www/src

RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["/www/src/entrypoint.sh"]
