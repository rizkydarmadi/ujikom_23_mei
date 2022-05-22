# Ujikom 23 Mei 2022

## Prerequisite
- python -V 3.9.6
- docker[optional]
- Ubuntu OS

## How to install
- Make a virtual environtment `python3 -m venv env`
- Use it `source env/bin/activate`
- Install Thrid party library `pip install -r requirement.txt`

## Migration Database
- init migrations`flask db init`
- migrate database `flask db migrate -m "Initial migration."`
- apply the migration to the database `flask db upgrade`

[official documentation](https://flask-migrate.readthedocs.io/en/latest/)

## Docker set up
- Build all `docker-compose up`

## Flask Start
- Select main files `export FLASK_APP=main`
- Change to Debugging Mode `export FLASK_DEBUG=1`
- Running app :) `flask run`
