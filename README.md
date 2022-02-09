# A financial dashboard application
<br /> The application is a portal/dashboard for storing and displaying details of a user's financial assets. 
<br /> It is intended for use by members of a family or a group.

<br /> This application use the base created by:
<br /> (i) https://github.com/thalesbruno/fastapi-boilerplate
<br /> (ii) https://fastapi.tiangolo.com/tutorial/sql-databases/

## Structure
<br /> The backend is a RESTful API application built in FastAPI and a PostgreSQL database.
<br /> The application is run inside a Docker container.

## Usage
<br /> Stage One completed: 7.2.2022
<br /> Working features: 
<br /> (i) Creation of a user account
<br /> (ii) Addition of an asset by a user
<br /> (iii) Searching assets by a specific value belonging to all users 


### How to run this project:
<br /> You would need to install Docker and some IDE (eg Visual Studio Code) to run this application.
<br /> Basic knowledge of using the command line and your IDE would be required. 
<br /> 
1. **Clone this project**
<br /> In a command prompt:
```bash
git clone https://github.com/adikele/financial-dashboard.git
```

2. **Start the container**
<br /> Start the Docker Desktop by clicking on the Docker logo.
<br /> In a command prompt, run the container from the directory containing the docker-compose file: 
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
<br /> 

4. **Move the upgrade_and_downgrade_functions.py file from alembic/versions folder to the alembic folder**
<br /> The path for the **alembic** folder is financial-dashboard/backend/app/app/alembic.
<br /> From another command prompt (since the container is running in the “first” command prompt):
```
$ cd alembic/
$ mv versions/upgrade_and_downgrade_functions .
$ ls
README					env.py					script.py.mako				upgrade_and_downgrade_functions	versions
```

5. **Get the containerID of the server**
<br /> From the “second” command prompt (or some other command prompt), get the containerID of the container running the server:
```
docker ps 
```
The containerIDs of the server and the postgreSQL containers will be displayed, similar to what is shown below:
<br /> NOTE: Your container IDs will be different from the ones below:
```
CONTAINER ID   IMAGE                     
4158461bc778   financial-dashboard_app   
e64439804308   postgres:12.4             
```
Copy 4158461bc778
<br /> NOTE: Copy the container ID generated for your container, not 4158461bc778
<br /> 

6. **Enter the container and generate migration scripts**
<br /> From the “second” command prompt (or some other command prompt), go to the directory containing the Docker compose file:
 ```
$ ls
README.md		backend			db_data			docker-compose.yml
```
Enter the container with the command: docker exec -it [containerID] bash
```
docker exec -it 4158461bc778  bash
```
The output would read something like this:
```
root@860d70de3701:/app# 
```
Note: The **app** directory has the alembic.ini file
```
root@860d70de3701:/app# ls
Dockerfile  __pycache__  alembic.ini  app  main.py  requirements
```
Generate the first migration script:
```
root@860d70de3701:/app# alembic revision -m "revision_tables"
```
A **xxx_revision_tables** file will be generated in the **versions** folder. 
Path to the folder: financial-dashboard/backend/app/app/alembic/versions
This file will have empty upgrade and downgrade functions. 
<br /> 
<br /> 
7. **Run the migrations**
<br /> In order to generate the database tables needed for this application, the upgrade and downgrade functions (see step 6) must have information about the creation of these tables. The content for the upgrade and downgrade functions file is provided in a file which (in step 4) has been moved to: financial-dashboard/backend/app/app/alembic
<br /> <br /> Using your IDE (Integrated Development Editor), copy the contents of the upgrade and downgrade functions file and paste the contents in the **xxx_revision_tables** file by replacing the empty functions in the **xxx_revision_tables** file.
<br />  <br /> In the command prompt where we have entered the container, write the command:
```
root@4158461bc778:/app# alembic upgrade head
```
The database tables required for this application should now be ready.
<br /> 
<br /> 
8. **Test the application manually**
<br /> To check if the application is working as expected:
<br /> Step 1: 
<br /> Go to the address http://127.0.0.1:8001/docs in your browser
<br /> Enter user details through the POST /users/ tab.
<br /> Note the id generated in the ”response” table.
<br /> Step 2: 
<br /> Enter asset details through the POST /users/{user_id}/assets/ tab.
<br /> For ”user id” field, enter the id generated in the ”response” table in step 1.
<br /> Also make a note of the amount you enter for the ”original value” field.
<br /> Step 3:
<br /> Go to the GET/manyAssetsOfSameValue/{original_value} tab
<br /> Enter the same value for ”original value” as entered in step 1.
<br /> The response should be the asset detail as entered in step 2.

## TO DO:
<br />
Stage Two:
1. Create tests
2. Host on the cloud
<br /> <br />
Stage Three:
3. Store results to the cloud
4. Build a frontend 
5. Add functionalities
