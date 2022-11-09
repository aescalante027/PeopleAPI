# flaskPeopleAPI
-------

Purpose: A REST API using basic people data, backed up by a MySQL db (schema currently not included)

Note: For all tests for this project, see [flaskPeopleAPITests](https://github.com/aescalante027/flaskPeopleAPITests).


## Requirements
The following items are required, which are not included in this repository:

**settings.csv** - CSV file containing the Username and Password for the database login 
. Requires headers *username, password* in the CSV file.


##Endpoints

All operating URLs start at http://127.0.0.1:5000

|Endpoint URL| Protocol | Definition|
|------------|----------|-----------|
|/person/all | GET      | Returns all users in DB |
|/person/{id}| GET      | Return person with id of {id} |
|/person/add | POST     | Add a person from body to table (see "Person" for more info) |
|/person/delete/{id} | DELETE | Removes a person with id of {id} |
|/person/{id}/age/{age} | PUT | Changes a person of id {id} age to {age} |
|/person/{id}/lastname/{lastname} | PUT | Changes a person of id {id} lastname to {lastname} |


## Person

Each person class consists of the following:
```
{
	"id": int,
	"lastname": String,
	"firstname": String,
	"age": int
}
```
NOTE: For endpoint "add", id is NOT provided, as the schema for id in MySQL is autoincremented. An ID will automatically be assigned to it. When adding a body, omit the id data line.


## Start Service
To start service, using python3:

```
python3 main.py
```