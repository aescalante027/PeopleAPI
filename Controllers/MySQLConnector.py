import MySQLdb
import pandas as pd
from MySQLdb.cursors import Cursor
from DataModels.Person import Person

class MySQLConnector:

    db: MySQLdb = None
    cur: Cursor

    def __init__ (self, filename):
        settings = pd.read_csv(filename, sep=',',header=0)
        username = settings["username"].values[0]
        password = settings["password"].values[0]
        self.db = MySQLdb.connect(host="localhost",
                                    user=username,
                                    passwd=password,
                                    db="people")
        self.cur = self.db.cursor()


    def getPeopleData(self):
        self.cur.execute("SELECT * FROM people")
        row_headers = [x[0] for x in self.cur.description]
        rv = self.cur.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json_data

    def addNewPerson(self, person: Person):
        query = "INSERT INTO people(id, lastname, firstname, age) VALUES (%s, %s, %s, %s);"
        val = (person.id, person.lastname, person.firstname, person.age)
        self.cur.execute(query, val)
        self.db.commit()

    def updatePersonLastName(self, id: int, lastname: str):
        query = "UPDATE people SET lastname = %s WHERE id = %s"
        val = (lastname, id)
        self.cur.execute(query, val)
        self.db.commit()

    def updateAge(self, id: int, age: int):
        query = "UPDATE people SET age = %s WHERE id = %s"
        val = (age, id)
        self.cur.execute(query, val)
        self.db.commit()

    def removePerson(self, id: int):
        query = "DELETE FROM people WHERE id = %s"
        val = (str(id))
        self.cur.execute(query, val)
        self.db.commit()

    def getPersonById(self, id: int):
        query = "SELECT * FROM people WHERE id = %s"
        val = (str(id))
        try:
            self.cur.execute(query, val)
        except(MySQLdb.Error) as e:
            print(e)
            print(query + " (id = " + str(id) + ")")
            return None
        row_headers = [x[0] for x in self.cur.description]
        rv = self.cur.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        person = Person(**json_data[0])
        return person