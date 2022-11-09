# This is a sample Python script.
from flask import Flask, jsonify, request, abort
from DataModels.Person import Person
from Controllers.PersonController import PersonController

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)
personController = PersonController("settings.csv")


@app.route('/person/all', methods=['GET'])
def printAllUsers():
    data = personController.getPeopleData()
    memory = {"data": data}
    return jsonify(memory)


@app.route('/person/<int:id>', methods=['GET'])
def getPersonById(id):
    result = personController.getPersonById(id)
    if result == None:
        abort(400)
    return jsonify(result)


@app.route('/person/add', methods=['POST'])
def addNewPerson():
    data = request.json
    id = None
    newPerson = Person(id, data["lastname"], data["firstname"], data["age"])
    personController.addNewPerson(newPerson)
    return jsonify(personController.getPeopleData())


@app.route('/person/delete/<int:id>', methods=['DELETE'])
def removePerson(id):
    personController.removePerson(id)
    return jsonify(personController.getPeopleData())


@app.route('/person/<int:id>/age/<int:age>', methods=['PUT'])
def changeAge(id, age):
    personController.updateAge(id, age)
    return jsonify(personController.getPersonById(id))


@app.route('/person/<int:id>/lastname/<lastname>', methods=['PUT'])
def changeLastName(id, lastname):
    personController.updatePersonLastName(id, lastname)
    return jsonify(personController.getPersonById(id))


if __name__ == '__main__':
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
