# SRE-Bootcamp-Exercise
This repository will cover all the milestones laid out here:- https://playbook.one2n.in/sre-bootcamp/sre-bootcamp-exercises

## Pre-requisites
- Docker
- Make


## To run the api server on local machine

```bash
# clone the repository
git clone https://github.com/avivansh/SRE-Bootcamp-Exercise.git
# change directory to the cloned repository
cd SRE-Bootcamp-Exercise
# bring up the api application on docker using make (check [Makefile](./Makefile))
make
```

## To run the tests

```bash
 pytest -v -s  --disable-warnings
```

## To run the multiple instance of the api server on local machine running behind nginx

```bash
# if you see nginx.conf file, there will be 2 upstream servers defined
# to bring up the api server
docker build -t sre-bootcamp-api .
docker network create sre-bootcamp
docker run -d --name sre-bootcamp-api-1 --hostname sre-bootcamp-api-1 --network sre-bootcamp -p 8001:8000 sre-bootcamp-api
docker run -d --name sre-bootcamp-api-2 --hostname sre-bootcamp-api-2 --network sre-bootcamp -p 8002:8000 sre-bootcamp-api
docker run --name nginx -p 80:80 -v ./nginx.conf:/etc/nginx/nginx.conf --network sre-bootcamp nginx
```

## Resources

- [Fast API Docs](https://fastapi.tiangolo.com/learn/)
- [Fast API tutorial - [Youtube]](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=53s)
- [FastAPI with SQLAlchemy, PostgreSQL and Alembic and of course Docker [Part-1]](https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396)
- [FastAPI with SQLAlchemy, PostgreSQL, Alembic and Docker [Part-2] (asynchronous version)](https://ahmed-nafies.medium.com/tutorial-fastapi-sqlalchemy-postgresql-alembic-and-docker-part-2-asynchronous-version-8a339ce97e6d)



