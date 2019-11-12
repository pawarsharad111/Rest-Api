from  flask import  Flask, jsonify,request

app=Flask(__name__)
stores=[
    {
        "name": "my store",
        "items": [{"name": "chair", "price": 100, "weight": "10kg", "height": 20}]
    },
    {
        "name":"dmart",
        "items":[{"name":"table", "price":1000,"weight":"10kg","height":20}]
    }
    ]

@app.route('/getall')
def allstores():
    return jsonify({"Output":stores})

@app.route('/onestore/<string:name>')
def find(name):
    for i in stores:
        if i["name"]==name:
            return jsonify(i)
    else:
        return jsonify({"output":"store not found"})

@app.route('/addstore',methods=['post'])
def addstore():
    d=request.get_json()
    for i in stores:
        if i["name"]==d["name"]:
            return jsonify({"message":"store allready exist"})
    stores.append(d)
    return jsonify({"message":"store added"})

@app.route('/additem/<string:var>',methods=['post'])
def additem(var):
    d = request.get_json()
    for i in stores:
        if i["name"]==var:
            for j in i["items"]:
                if j["name"]==d["name"]:
                    return jsonify({"message":"item all ready exit"})
            i["items"].append(d)
            return jsonify({"message":"item added"})
    return jsonify({"message":"store not found"})

app.run(port=5000)

