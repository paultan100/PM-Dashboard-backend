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
GET '/future_capabilities'
POST '/future_capabilities'
PATCH '/future_capabilities'
DELETE '/future_capabilities'
GET '/scopes'
POST '/scopes'


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

GET '/future_capabilities'
- Shows all future capabilities. 
- Request arguments: None
- Returns all the future capabilities
- Example response:
{
    "items": [
        {
            "capabilities_count": 10,
            "id": 3,
            "points": 2,
            "size": "M"
        },
    ],
    "success": true
}

POST '/future_capabilities'
- Creates a new future capabilty
- Request arguments: A JSON with a points, size, and capabilities_count arguments.
- Example request:
{
    "points": 1,
    "size": "S",
    "capabilities_count": 4
}
- Returns a JSON with the id of the object created.
- Example response: 
{
    "created": 7,
    "success": true
}

PATCH '/future_capabilities/{item_id}'
- updates the specified future_capability
- Request arguements: A JSON with any fields which are desired to update.
- example request: 
{
    "points": 2,
    "capabilities_count": 5
}
- Returns a JSON with the id of the updated object
- example response:
{
    "success": true,
    "updated": 7
}

DELETE '/future_capabilties/{item_id}
- Deleted the specified future_capability
- Request arguments: None
- Returnes the id of the deleted item
- Example reponse:
{
    "deleted": "7",
    "success": true
}

GET '/scopes'
- Gets all the scopes. A scope is an object which represents a point in time of the burn up velocity.
- Request arguments: none
- Returns all the scopes
- Example response:
{
    "items": [
        {
            "average": 4,
            "high": 6,
            "id": 37,
            "low": 2,
            "points": 64,
            "week": 1
        }
    ],
    "success": true
}

POST '/scopes'
- This endpoint creates all the scopes for the burn up chart.
- Request arguments: the total number of points for an 8 week period. This number will be used to create data points for a burn up chart using velocities of 2, 4, and 6. 
- Example request: {
    "points": 20
}
- returns the number of created scopes.
- Example response: 
{
    "success" : true,
    "number of created scopes" : 9
}


To connect to the heroku database use: psql -h hostname -d databasename -U username