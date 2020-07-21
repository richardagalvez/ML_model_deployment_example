FROM python:3.7-stretch

COPY ./app/requirements.txt /app/

RUN pip3 install -r app/requirements.txt
RUN pip3 install -f http://h2o-release.s3.amazonaws.com/h2o/latest_stable_Py.html h2o
RUN apt-get update -q -y
RUN apt-get install -y openjdk-8-jdk

COPY . /app
COPY app/data.csv /app/data.csv
WORKDIR /app
# RUN pip3 install -e .

EXPOSE 5000

CMD ["python", "app/deploy.py"]