To get this project up and running locally the following steps must be completed:

*It is recommended to create a virtual python environment - https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/*

0. cd into the backend folder.

1. Import requirements with 'pip install -r requirements.txt'. NOTE: You must be logged in as the admin to do this.

2. Update the database_path variable in models.py to point to database that will be used.  

3. Run 'flask db init', 'flask db migrate', then 'flask db upgrade'. This will create the tables needed in the db specified in the previous step.  

4. To run the server type 'flask run'.