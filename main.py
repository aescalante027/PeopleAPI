# This is a sample Python script.
from flask import Flask, jsonify, request, abort
from DataModels.Person import Person
from Controllers.MySQLConnector import MySQLConnector

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)
memory: dict[int, Person] = {}
mysql = MySQLConnector("settings.csv")


@app.route('/person/all', methods=['GET'])
def printAllUsers():
    data = mysql.getPeopleData()
    memory = {"data": data}
    return jsonify(memory)


@app.route('/person/<int:id>', methods=['GET'])
def getPersonById(id):
    result = mysql.getPersonById(id)
    if result == None:
        abort(400)
    return jsonify(result)


@app.route('/person/add', methods=['POST'])
def addNewPerson():
    data = request.json
    id = None
    newPerson = Person(id, data["lastname"], data["firstname"], data["age"])
    mysql.addNewPerson(newPerson)
    return jsonify(mysql.getPersonById(id))


@app.route('/person/delete/<int:id>', methods=['DELETE'])
def removePerson(id):
    mysql.removePerson(id)
    return jsonify(mysql.getPeopleData())


@app.route('/person/update/<int:id>/age/<int:age>', methods=['PUT'])
def changeAge(id, age):
    mysql.updateAge(id, age)
    return jsonify(mysql.getPersonById(id))


@app.route('/person/update/<int:id>/lastname/<lastname>', methods=['PUT'])
def changeLastName(id, lastname):
    mysql.updatePersonLastName(id, lastname)
    return jsonify(mysql.getPersonById(id))


if __name__ == '__main__':
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
