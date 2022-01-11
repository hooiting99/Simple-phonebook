from os import name
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/phonebook'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Phonebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    phoneNo = db.Column(db.String(11))

    def __init__(self, name, phoneNo):
        self.name = name
        self.phoneNo = phoneNo

class PhonebookSchema(ma.Schema):
    class Meta:
        fields =('id', 'name', 'phoneNo')

phonebook_schema = PhonebookSchema()
phonebooks_schema = PhonebookSchema(many = True)

@app.route('/get', methods =['GET'])
def get_phonebook():
    all_contacts = Phonebook.query.all()
    results = phonebooks_schema.dump(all_contacts)
    return jsonify(results)

@app.route('/get/<id>/', methods =['GET'])
def display_contact(id):
    contact = Phonebook.query.get(id)
    return phonebook_schema.jsonify(contact)

@app.route('/add', methods =['POST'])
def add_phonebook():
    name = request.json['name']
    phoneNo = request.json['phoneNo']

    phonebooks = Phonebook(name, phoneNo)
    db.session.add(phonebooks)
    db.session.commit()
    return phonebook_schema.jsonify(phonebooks)





if __name__ =="__main__":
    app.run(debug=True)