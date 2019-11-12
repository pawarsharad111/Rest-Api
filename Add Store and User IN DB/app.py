from  flask import  Flask, jsonify

app=Flask(__name__)
## app.debug=True  ## it reflect the changes when we refesh
stores=[
    {
        "name":"dmart",
        "items":[{"name":"table", "price":1000,"weight":"10kg","height":20}]
    }
        ]
@app.route('/allstores')
def allstores():
    return jsonify({"Output":stores})

@app.route('/onestore/<string:name>')
def find(name):
    for i in stores:
        if i["name"]==name:
            return jsonify(i)
    else:
        return jsonify({"output":"store not found"})

@app.route('/items/<string:sname>/<string:iname>')
def item(sname, iname):
    for each_store in stores:
        if each_store["name"]==sname:

            for each_item in each_store["items"]:
                if each_item["name"]==iname:
                    return jsonify(each_item)

            else:
                return jsonify({"Output":"Item not found"})
    else:
        return jsonify({"Output":" Store not found "})


app.run(port=5080)
