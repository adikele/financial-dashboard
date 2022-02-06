# FastAPI boilerplate (with PostgreSQL)
![example workflow name](https://github.com/thalesbruno/fastapi-boilerplate/workflows/Tests/badge.svg)

A boilerplate RESTFul application code using FastAPI and PostgreSQL

## Structure
The backend is a RESTful API application built in FastAPI and a PostgreSQL database.

## Usage

### With docker-compose
1. **Clone this project**
<br /> In a command prompt:
```bash
git clone ​​https://github.com/adikele/financial-dashboard.git
```

2. **Start the container**
<br /> In the same command prompt, run the container from the directory containing the docker-compose file: 
```bash
$ ls
financial-dashboard
$ cd financial-dashboard/
$ ls 
README.md		backend			docker-compose.yml
$ docker-compose up
```

3. **Check if the container is ready**
<br /> When the container is ready, it will show the project’s documentation page in your browser at the address http://127.0.0.1:8001/docs


4. **Move the upgrade_and_downgrade_functions.py file from alembic/versions folder to the alembic folder**
<br /> The path for the **alembic** folder is financial-dashboard/backend/app/app/alembic.
<br /> From another command prompt (since the container is running in the “first” command prompt):
```
$ cd alembic/
$ mv versions/upgrade_and_downgrade_functions.py .
$ ls
README					env.py					script.py.mako				upgrade_and_downgrade_functions.py	versions
```

5. **Get the containerID of the server**
<br /> From the “second” command prompt (or some other command prompt), get the containerID of the container running the server:
```
docker ps 
```
The containerIDs of the server and the postgreSQL containers will be displayed:
```
CONTAINER ID   IMAGE                     
4158461bc778   financial-dashboard_app   
e64439804308   postgres:12.4             
```
Copy 4158461bc778


6. **Enter the container and generate migration scripts**
<br /> From the “second” command prompt (or some other command prompt), go to the directory containing the Docker compose file:
 ```
$ ls
README.md		backend			db_data			docker-compose.yml
```
<br /> Enter the container with the command: docker exec -it [containerID] bash
```
docker exec -it 4158461bc778  bash
```
<br /> The output would read something like this:
```
root@860d70de3701:/app# 
```
<br /> Note: The **app** directory has the alembic.ini file
```
root@860d70de3701:/app# ls
Dockerfile  __pycache__  alembic.ini  app  main.py  requirements
```
<br /> Generate the first migration script:
```
root@860d70de3701:/app# alembic revision -m "revision_tables"
```
<br /> A **xxx_revision_tables** file will be generated in **versions** folder. This file will have empty upgrade and downgrade functions. 


7. **Run the migrations**
<br /> In order to generate the database tables needed for this application, the upgrade and downgrade functions (see step 6) must have information about the creation of these tables. The content for the upgrade and downgrade functions file is provided in a file which (in step 4) has been moved to: financial-dashboard/backend/app/app/alembic
<br /> Using your IDE (Integrated Development Editor), copy the contents of the upgrade and downgrade functions file and paste the contents in the **xxx_revision_tables** file by replacing the empty functions in the **xxx_revision_tables** file.
<br /> In the command prompt, where we have entered the container:
```
root@4158461bc778:/app# alembic upgrade head
```

