FROM python:3.11

RUN mkdir -p /home/app

COPY . /home/app

EXPOSE 3000

CMD ["python","home/app/main.py"]