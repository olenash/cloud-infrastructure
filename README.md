### This repository contain the solution for Cloud infrastructure basics. How to scale applications 2019 I am taking at Ukrainian Catholic University.
Here we will be building high load flask service that need a lot of resources and need future scaling.

Building the docker image
```sh
docker build -t flask-service:0.1 .
```

Run docker container
```sh
docker run -p 80:5000 --name service flask-service:0.1
```
The service should be available at
```sh
0.0.0.0:80
```
