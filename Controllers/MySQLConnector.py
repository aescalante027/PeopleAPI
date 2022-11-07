import MySQLdb
from DataModels.Person import Person

db = MySQLdb.connect(host="localhost",
                         user="<user>",
                         passwd="<pass>",
                         db="people")
cur = db.cursor()

class MySQLConnector:

    def getPeopleData(self):
        cur.execute("SELECT * FROM people")
        row_headers = [x[0] for x in cur.description]
        rv = cur.fetchall()
        json_data = []
        for result in rv:
            json_data.append(dict(zip(row_headers, result)))
        return json_data

    def addNewPerson(self, person: Person):
        query = "INSERT INTO people(id, lastname, firstname, age) VALUES (" + str(person.id) + ", \"" + \
                person.lastname + "\", \"" + \
                person.firstname + "\", " + \
                str(person.age) + ");"
        print(query)
        cur.execute(query)
        db.commit()

    def updatePersonLastName(self, person: Person, lastname: str):
        query = "UPDATE people SET lastname = %s WHERE id = %s"
        val = (lastname, person.id)
        cur.execute(query, val)
        db.commit()

    def updateAge(self, person: Person, age: int):
        query = "UPDATE people SET age = %s WHERE id = %s"
        val = (age, person.id)
        cur.execute(query, val)
        db.commit()

    def removePerson(self, id: int):
        query = "DELETE FROM people WHERE id = %s"
        val = (str(id))
        cur.execute(query, val)
        db.commit()