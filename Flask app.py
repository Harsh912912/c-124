from flask import Flask,jsonify,request

app = Flask(__name__)
data = [
    {
        'Contact':"9987644456",
        'Name':"Raju"
        'done':"false"
        "id":'1'
    },
    {
        'Contact':u'9786532123',
        'Name':u'Akshay',
        'done': 'False',
        'id':'2'
    }
]

@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)

    task = {
        'id':tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',""),
        'done':False
    }
    tasks.append(task)
    return jsonify({
        "data": tasks
    })

@app.route("/get-data") 
def get_task():
    return jsonify({
        "data":tasks
    })

if (__name__=="__main__"):
    app.run(debug = True)