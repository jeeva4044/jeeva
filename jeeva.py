from decimal import Context
from logging import config
from flask import Flask, request
import sqlite3
app=Flask(__name__)
@app.get('/')
def ooi():
    return "Its jee"

@app.patch("/upd")
def update():
    data=request.get_json();
    updates(data);
    return("updated");

def updates(data):
    query=f'update students setname="{data["name"]}" where rollno="{data["rollno"]}"';
    cur= Context.cursor();
    cur.exeute(query);
    config.commit();

   

@app.post('/h')
def hi():
    con = sqlite3.Connection("C:/Users/trc/Desktop/pritheesh/jk/data.db")
    cur=con.cursor()
    data = request.get_json()
    Name=data["Name"]
    Rollno=data["Rollno"]
    Mark=data["Mark"]
    students=(Name,Rollno,Mark)
    cur.execute("create table if not exists students(name varchar(255),Rollno varchar(255),Mark int)")
    cur.execute("insert into students values(?,?,?)",students)
    con.commit()
    con.close()
    print(data)
    return "we got the data of get and post"

@app.patch('/pat/<inputName>')
def patchmethod(inputName):
    data = request.get_json() 
    users = data



    if inputName in users.values():
        users["Name"] = 1000
        res = "Data updated"
        return res
    
    print(f"The data after creation is {users}")
    res = "Data created"

@app.delete("/del/<inputName>")
def deletemethod(inputName):
    data = request.get_json()
    users = data
    if inputName in users.values():
        del users["Name"]
        res = "Data deleted"
        return res
    res = "Data not found"
    return res
app.run(debug=True)




