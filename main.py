from fastapi import FastAPI, HTTPException, Request, Body
from DataModels.Person import Person
from Controllers.PersonController import PersonController
import uvicorn

app = FastAPI()
personController = PersonController("settings.csv")


@app.get('/person/all')
def print_all_users():
    data = personController.getPeopleData()
    memory = {"data": data}
    return memory


@app.get('/person/{id}')
async def get_person_by_id(id):
    result = personController.getPersonById(id)
    if result is None:
        raise HTTPException(status_code=404, detail="User not found")
    return result


@app.post('/person/add')
async def add_new_person():
    data: dict = Body(...)
    print(data.values())
    id = None
    newPerson = Person(id, data["lastname"], data["firstname"], data["age"])
    personController.addNewPerson(newPerson)
    return personController.getPeopleData()


@app.delete('/person/delete/{id}')
async def remove_person(id):
    personController.removePerson(id)
    return personController.getPeopleData()


@app.put('/person/{id}/age/{age}')
async def change_age(id, age):
    personController.updateAge(id, age)
    return personController.getPersonById(id)


@app.put('/person/{id}/lastname/{lastname}')
async def change_last_name(id, lastname):
    personController.updatePersonLastName(id, lastname)
    return personController.getPersonById(id)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)