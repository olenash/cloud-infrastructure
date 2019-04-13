FROM python:3
MAINTAINER Olena Shevchenko "o.shevchenko@ucu.edu.ua"
#RUN apt-get update -y
#RUN apt-get install -y python-pip python-dev build-essential
COPY ./service_loc /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["Service.py"]
