class DBStringConstants:

    getAllPeople = "SELECT * FROM people"
    getPersonById = "SELECT * FROM people WHERE id = %s"
    addNewPerson = "INSERT INTO people(id, lastname, firstname, age) VALUES (%s, %s, %s, %s);"
    updateLastName = "UPDATE people SET lastname = %s WHERE id = %s"
    updateAge = "UPDATE people SET age = %s WHERE id = %s"
    delete = "DELETE FROM people WHERE id = %s"