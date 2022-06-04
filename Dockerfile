FROM python:3

ENV DJANGO_CLEARBIT_APIKEY: ${DJANGO_CLEARBIT_APIKEY}

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

CMD ["/bin/bash"]