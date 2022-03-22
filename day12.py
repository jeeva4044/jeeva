from flask import Flask, request
import sqlite3
app=Flask(__name__)
@app.get('/')
def hi():
    return "good night"
@app.post('/h')
def hi1():
    con = sqlite3.Connection("C:/Users/trc/Desktop/pritheesh/jk/data.db")
    cur=con.cursor()
    data = request.get_json()
    Name=data["Name"]
    Rollno=data["Rollno"]
    Mark=data["Mark"]
    student=(Name,Rollno,Mark)
    cur.execute("create table if not exists student(name varchar(255),Rollno varchar(255),mark int)")
    cur.execute("insert into student values(?,?,?)",student)
    con.commit()
    con.close()
    print(data)
    return "data collected"
@app.patch('/pat/<inputmark>')
def patchmethod(inputmark):
    data = request.get_json()
    users = data
    if inputmark in users.values():
        users["Mark"] = 99
        res = "Data updated"
        return res
    print(f"The data after creation is {users}")
    res = "Data created"
@app.delete("/del/<inputmark>")
def deletemethod(inputmark):
    data = request.get_json()
    users = data
    if inputmark in users.values():
        del users["Mark"]
        res = "Data deleted"
        return res
    res = "Data not found"
    return res
app.run(debug=True)