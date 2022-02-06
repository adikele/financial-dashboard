# FastAPI boilerplate (with PostgreSQL)
![example workflow name](https://github.com/thalesbruno/fastapi-boilerplate/workflows/Tests/badge.svg)

A boilerplate RESTFul application code using FastAPI and PostgreSQL

## Structure
The backend is a RESTful API application built in FastAPI and a PostgreSQL database.

## Usage

### With docker-compose
1. Clone this project:
→ in a command prompt:
```bash
git clone ​​https://github.com/adikele/financial-dashboard.git
```

2. Start the container: 
→ go to the directory containing the docker-compose file and run the container: 
```bash
$ ls
financial-dashboard
$ cd financial-dashboard/
$ ls 
README.md		backend			docker-compose.yml
$ docker-compose up
```

3. Check if the container is ready:
→ by visiting http://127.0.0.1:8001/docs on the browser
When ready, the Web page will show the project’s documentation page.
A snapshot of the "documentation" page is provided in the files: documentation.jpg

4. Move the upgrade_and_downgrade_functions.py file from alembic/versions folder to the alembic folder:
The path for alembic folder is financial-dashboard/backend/app/app/alembic
From another command prompt (let’s call this “second” command prompt):
→ go to the alembic folder and provide the mv command to move the file
```
$ cd alembic/
$ mv versions/upgrade_and_downgrade_functions.py .
$ ls
README					env.py					script.py.mako				upgrade_and_downgrade_functions.py	versions

```

```
docker-compose exec app pytest
```

```
docker-compose exec app pytest
```

```
docker-compose exec app pytest
```
### Tests
**To run the tests:**

```
docker-compose exec app pytest
```

**To re-run the tests**, firstly, we recreate the database because there are unit tests which create resources, so if it already exists the test will fail:

Remove the data files before recreate the container
```
rm -fr db_data/*
```
Recreate the db service:

```docker
docker-compose stop db
docker-compose rm db
docker-compose up -d db
```

Finally, re-run the migration and the tests:
```
docker-compose exec app alembic upgrade head
docker-compose exec app pytest
```

<!--
### With python virtual environment
If you want to run the application from your terminal, you may create a python virtual environment, install the dependencies and run it using uvicorn:

```bash
python3 -m venv .venv
source ./venv/bin/activate
(.venv) pip install -r requirements/dev.txt
(.venv) cd backend
(.venv) uvicorn main:app --reload
```
-->
