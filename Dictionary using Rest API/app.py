from flask import Flask, jsonify, request
import json

data=json.load(open('data.json'))
app=Flask(__name__)

@app.route('/getword',methods=['POST'])

def get_word():
    data1=request.get_json()
    print('\n\n',data1,'\n\n')
    word= data1["word given"]
    for i in data:
        if i==word.lower():
            return jsonify({"meaning":data[i]})
    return  jsonify({'message':' word not found'})


app.run(port=5060)