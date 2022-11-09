import MySQLdb
import pandas as pd
from MySQLdb.cursors import Cursor
from DataModels.DBStringConstants import DBStringConstants as dbsc
from DataModels.Person import Person


class PersonController:
    db: MySQLdb = None
    cur: Cursor

    def __init__(self, filename):
        settings = pd.read_csv(filename, sep=',', header=0)
        username = settings["username"].values[0]
        password = settings["password"].values[0]
        self.db = MySQLdb.connect(host="localhost",
                                  user=username,
                                  passwd=password,
                                  db="people")
        self.cur = self.db.cursor()

    def getPeopleData(self):
        self.cur.execute(dbsc.getAllPeople)
        row_headers = [x[0] for x in self.cur.description]
        rv = self.cur.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json_data

    def addNewPerson(self, person: Person):
        val = (person.id, person.lastname, person.firstname, person.age)
        self.cur.execute(dbsc.addNewPerson, val)
        self.db.commit()

    def updatePersonLastName(self, id: int, lastname: str):
        val = (lastname, id)
        self.cur.execute(dbsc.updateLastName, val)
        self.db.commit()

    def updateAge(self, id: int, age: int):
        val = (age, id)
        self.cur.execute(dbsc.updateAge, val)
        self.db.commit()

    def removePerson(self, id: int):
        val = (str(id))
        self.cur.execute(dbsc.delete, val)
        self.db.commit()

    def getPersonById(self, id: int):
        val = (str(id))
        try:
            self.cur.execute(dbsc.getPersonById, val)
        except MySQLdb.Error as e:
            print(e)
            print(dbsc.getPersonById + " (id = " + str(id) + ")")
            return None
        row_headers = [x[0] for x in self.cur.description]
        rv = self.cur.fetchall()
        if len(rv) == 0:
            print("No person found with ID " + str(id))
            return None
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        person = Person(**json_data[0])
        return person
