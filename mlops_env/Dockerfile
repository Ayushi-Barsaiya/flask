FROM python:3.11.9-bookworm
WORKDIR /flask-docker

RUN python3 -m pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ENV FLASK_APP = loan-app.py
COPY . . 

CMD ["python3","-m","flask","run","--host=0.0.0.0"]