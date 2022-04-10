from flask import Flask
from flask import jsonify,request
from bson.json_util import dumps
from pymongo.database import Database
from pymongo import MongoClient
from bson.objectid import objectid #استرداد id عشوائي
import pymongo
import json


#################################من هنا يبدا الكود#########

app = Flask(name)
#############################استدعاء المونكوو##########
myclient  = MongoClient()
mydb= myclient .new_db
Database(MongoClient('localhost', 27017), 'mydata')
mydb.db.mydata.find
#########################لداله طباعه الرساله الترحيبيه############
@app.route('/',methods=['GET'])
def test():
    return jsonify({'massge': 'Iam a Python programmer'+' '+'Iam Mester_iT'})
###########داله اضافه يوزر ############
@app.route('/add',methods=['POST'])
def add_user():
    _json=request.json
    _name=_json['name']
    _email=_json['email']
    _address=_json['address']
    if _name and _email and _address and request.method == 'POST':
        id =mydb.posts.insert_one({'name':_name,'email':_email,'address':_address})
        resp =jsonify("good add.........")
        resp.status_code = 200
        return resp
    else:
        return not_found()
###############داله طاعه الداتا#########
@app.route('/info')
def info():
    users = mydb.db.mydata.find()
    resp = dumps(users)
    return jsonify(resp)

@app.errorhandler(404)
def not_found(eroor=None):
    massage={
    'status':404,
    'massage':'not_found'+request.url
    }
    resp=jsonify(massage)
    resp.status_code
####################
# @app.route('/delete/<id>',methods=['DELET'])
# def deletOne(id):
#     mydb.db.user.deleteOne({'id':object(id)})
#     resp=jsonify("usser delet successfully")
#     resp.status_code=200
#     return resp
# @app.route('/update/<id>',methods=['PUT'])
# def update(id):
#     _json = request.json
#     _name= _json['name']
#     _email= _json['email']
#     _addres= _json['addres']
#     if _name and _addres and _email  and request.method=='put':
#         mydb.db.user.update({'_id[$oid]'if'$oid'in _id})
#         return

########هذه الداله مهمه للطباعه العمل #########
if name == 'main':
    app.run(debug=True,port=8080)