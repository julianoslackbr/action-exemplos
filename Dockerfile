FROM python:3.8-alpine3.12


COPY app/main.py /app
COPY app/requirements.txt /app
WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["python3", "main.py"]