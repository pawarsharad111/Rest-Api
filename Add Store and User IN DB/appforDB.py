from flask import Flask, request, jsonify
import sqlite3
app=Flask(__name__)

@app.route('/adduser', methods=['post'])
def adduser():
    data=request.get_json()
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    insert_query="INSERT INTO user VALUES(?,?)"
    cursor.execute(insert_query,(data['id'],data['password']))
    connection.commit()
    connection.close()
    return jsonify({"message":"user added"})

@app.route('/alluser')
def alluser():
    connection=sqlite3.connect('data.db')
    cursor=connection.cursor()
    select_query="SELECT * FROM user"
    result=cursor.execute(select_query)
    result=list(result)
    return jsonify({"users":result})

@app.route('/check',methods=['post'])
def check():
    data=request.get_json()
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    select_query = "SELECT * FROM user"
    result = cursor.execute(select_query)
    result = list(result)
    for i in result:
        if i[0]==data['id']:
            if i[1]==data['password']:
                return jsonify({"message":"Success"})
    return jsonify({"message":"not found"})


app.run(port=5000)




