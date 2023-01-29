import sqlite3

class DataBase:
    def connectToDatabase():
        try:
            db = sqlite3.connect("data.db")
            cur = db.cursor()
            cur.execute(
                "CREATE TABLE if not exists todos (id INTEGER PRIMARY KEY AUTOINCREMENT, Todo TEXT NOT NULL, Date TEXT NOT NULL)")
            return db
        except Exception as e:
            print(e)

    def readDatabase(db):
        cur = db.cursor()
        cur.execute("SELECT id, Todo, Date From todos")
        records = cur.fetchall()
        return records

    def writeDatabase(db, values):
        cur = db.cursor()
        cur.execute("INSERT INTO todos (Todo, Date) VALUES (?,?)", values)
        db.commit()

    def deleteDatabase(db, id):
        cur = db.cursor()
        # TODO: id would be better as the todo text
        cur.execute("DELETE FROM todos WHERE id=?", (id,))
        db.commit()

    def updateDatabase(db, values):
        cur = db.cursor()
        # print(values)
        cur.execute("UPDATE todos SET Todo=? WHERE id=?", values)
        db.commit()

    def getTodoId(db, value):
        cur = db.cursor()
        cur.execute("SELECT id FROM todos WHERE Todo=?", (value,))
        todo_id = cur.fetchone()
        if todo_id:
            return todo_id[0]
        else:
            return None
