from flask import Flask, jsonify, request
import sqlite3

app=Flask(__name__)
@app.route('/adduser', methods=['post'])
def add_user():
    data=request.get_json()
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    insert_query = "INSERT INTO users VALUES(?,?)"
    cursor.execute(insert_query, (data['username'],data['password']))
    connection.commit()
    connection.close()
    return jsonify({'message':'user added'})

@app.route('/getuser')
def get_user():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    get_query="SELECT * FROM users"
    result=cursor.execute(get_query)
    users=[]
    for i in result:
        users.append(i)
    return jsonify({"output":users})

app.run(port=5060)
