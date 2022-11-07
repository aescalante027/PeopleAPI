# This is a sample Python script.
from flask import Flask, jsonify, request
from DataModels.Person import Person
from Controllers.MySQLConnector import MySQLConnector

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)
memory: dict[int, Person] = {}
mysql = MySQLConnector()

@app.route('/all', methods=['GET'])
def printAllUsers():
    return jsonify(memory)

@app.route('/add', methods=['POST'])
def addNewPerson():
    data = request.json
    id = len(memory)
    while id in memory:
        id += 1
    newPerson = Person(id, data["lastname"], data["firstname"], data["age"])
    memory[id] = newPerson
    mysql.addNewPerson(newPerson)
    return jsonify(memory)

@app.route('/delete/<int:id>', methods=['DELETE'])
def removePerson(id):
    if id in memory:
        memory.pop(id, None)
        mysql.removePerson(id)
    return jsonify(memory)

@app.route('/update/<int:id>/age/<int:age>', methods=['PUT'])
def changeAge(id, age):
    if id in memory:
        person = memory[id]
        person.age = age
        memory[id] = person
        mysql.updateAge(person, age)
    return jsonify(memory)

@app.route('/update/<int:id>/lastname/<lastname>', methods=['PUT'])
def changeLastName(id, lastname):
    if id in memory:
        person = memory[id]
        person.lastname = lastname
        memory[id] = person
        mysql.updatePersonLastName(person, lastname)
        return jsonify(memory[id])
    return jsonify(None)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = mysql.getPeopleData()
    for x in range(0,len(data)):
        person = Person(**data[x])
        memory[x] = person
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
