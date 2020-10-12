FROM python

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install  -r requirements.txt

COPY producer.py ./

CMD ["python", "producer.py"]
