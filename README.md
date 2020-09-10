To get this project up and running locally the following steps must be completed:

*It is recommended to create a virtual python environment - https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/*

0. cd into the backend folder.

1. Import requirements with 'pip install -r requirements.txt'. NOTE: You must be logged in as the admin to do this.

2. Update the database_path variable in models.py to point to database that will be used.  

3. Run 'flask db init', 'flask db migrate', then 'flask db upgrade'. This will create the tables needed in the db specified in the previous step.  

4. To run the server type 'flask run'.

## Endpoints
All but '/' endpoints return JSON objects.

Endpoints:
GET '/'
GET '/resources'
POST '/resources'
DELETE '/resources/{resource_id}'
GET '/capabilities'
POST '/capabilities'
DELETE '/capabilities'

```

GET '/'
This endpoint just returns hello.

GET '/resources'
- Returns a JSON of all the resources
- Request arguments: none
- Returns whether if was successful and all the resources
- example response:
{
    success: true,
    items:[
        {
            id: 1,
            projectName: 'My first project',
            duration: 10,
            resourceName: 'Isaac',
            status: 'active',
            updatedDate: 'Wed, 02 Sep 2020 18:47:29 GMT'
        }
    ]
}

POST '/resources'
- Creates a new resources
- Request Arguments: a JSON object with at least a projectName, duration, and resourceName. 
- example request JSON:
    {
        "projectName": "test",
        "duration": 12,
        "resourceName" : "Jonny"
    } 
- Returns whether the request was successful and the id of the created resource
- example response: 
    {
        success: true,
        created: 1
    }

DELETE '/resources/{resource_id}', 
       '/capabilities/{capability_id}'
- Deletes the specified resource
- Request arguements: none
- Returns whether it was deleted or not and the id of the deleted resource.
- example response: 
    {
        success: true,
        deleted: 1
    }

GET '/capability'
- Returns a JSON of all the capabilties
- Request arguments: none
- Returns whether if was successful and all the resources
- example response:
{
    success: true,
    items: [
        {
            id: 1,
            number: 12,
            name: "My first capability",
            size: 34,
            status: "active",
            length: 1,
            dependency: "N/A"
        }
    ]
}

POST '/capability'
- Creates a new capabiltiiy
- Request Arguments: a JSON object with a number, name, size,
status and length. 
- example request JSON:
    {
        "number": 12
        "name": "test",
        "size": "Medium",
        "length" : 34,
        "status" : "ACTIVE",
    } 
- Returns whether the request was successful and the id of the created resource
- example response: 
    {
        success: true,
        created: 1
    }

To connect to the heroku database use: psql -h hostname -d databasename -U username