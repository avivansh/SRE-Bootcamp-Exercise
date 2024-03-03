#!/bin/sh

## https://medium.com/@johnidouglasmarangon/using-migrations-in-python-sqlalchemy-with-alembic-docker-solution-bd79b219d6a
## https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396

alembic upgrade head

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
