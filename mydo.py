from flask import Flask,jsonify,request
from flask import Flask
import pymongo
from bson import json_util, ObjectId
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mypro"]
mycol = mydb["deliv"]

# print(myclient.list_database_names())
#
# print(mydb.list_collection_names())

# collist = mydb.list_collection_names()
# if "customers" in collist:
#   print("The collection exists.")

app = Flask(__name__)


#List=[{'name':'fasbook'},{'name':'instgram'},{'name':'telegram'}]
#List={'app':'fasbook',"location":"initial"}
@app.route('/',methods=['GET'])
def test():
    # x = mycol.insert_one(List)
    # y = mycol.find_one()
    # print(y)
    return jsonify({"message":"ok"})

@app.route('/product',methods=['GET'])
def get_prod():
   y = mycol.find_one()
   page_sanitized = json.loads(json_util.dumps(y))
   return (page_sanitized)


@app.route('/find_app',methods=['GET'])
def get_app():
   y = mycol.find({},{"app":"fasbook"})
   for x in y:
       print(x)
   page_sanitized = json.loads(json_util.dumps(x))
   return (page_sanitized)

@app.route('/info',methods=['GET'])
def reternall():
    collist = mydb.list_collection_names()
    if "customers" in collist:
        print("The collection exists.")

    return jsonify({'info':collist})

@app.route('/info/<string:name>',methods=['GET'])
def serch(name):
    mydict = {"name": "John", "address": "Highway 37"}

    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    x=[list for list in list if list['name'] == name]
    return jsonify({'list':x[0]})

@app.route('/info',methods=['POST'])
def addPost():
    orderss = {"name": "Assad Bable",
              "Address":"hilla_ALjamiaea",
              "telphone":"077712604687",
              "email":"delivery@gmail.com",
              "orders":[
                       {
                           "custmares": "ali",
                           "id": "1353272134728652"
                       },
                       {
                           "telphone": "876456789876",
                           "id": "1353269908062208",
                           "tracking":"asd bable hilla"
                       }
                   ],
               }
               # orders[
               # "Id":"11",
               # "custumare":"ali",
               # "telphone":"09876345790",]
    print(orderss)

    list = {'name': request.json['name']}
    list. append(list)
    return jsonify({'list':list})

@app.route('/info/<string:name>',methods=['PUT'])
def editOne(name):


    x = mycol.find_one()

    myquery = {"address": "Park Lane 38"}

    #mydoc = mycol.find(myquery)

    mydoc = mycol.find().sort("name")
    #mydoc = mycol.find().limit(2)

    for x in mydoc:
        print(x)
    # for x in x:
    #     print(x)

    print(x)
    x=[list for list in list if list['name'] == name]
    x[0]['name']= request.json['name']
    return jsonify({'list':x[0]})

@app.route('/info/<string:name>',methods=['DELET'])
def deletOne(name):
    myquery = {"address": {"$regex": "^S"}}
    x = mycol.delete_many(myquery)

    print(x.deleted_count, " documents deleted.")

    mycol.drop()

    x=[list for list in list if list['name']==name]
    list.remove(list[0])
    return jsonify({'list':list})

@app.route('/upload',methods=['update'])
def uploded():
    myquery = {"address": {"$regex": "^S"}}
    newvalues = {"$set": {"name": "Minnie"}}

    x = mycol.update_many(myquery, newvalues)

    print(x.modified_count, "documents updated.")


if __name__ == '__main__':
    app.run(debug=True,port=8080)