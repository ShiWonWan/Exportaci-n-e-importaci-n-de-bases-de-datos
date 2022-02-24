from flask_cors import CORS
from flask import Flask, jsonify, request
from datetime import datetime
from flask_pymongo import MongoClient, ObjectId


app = Flask(__name__)
CORS(app)

# PyMongo config
connection_str = 'mongodb://localhost/'
client = MongoClient(connection_str)
db = client.dataBaseHomeWork

"""
        BLOGS
"""
# Create a new blog /blog
@app.route('/blog', methods=['POST'])
def newBlog():
    id = db.blog.insert_one({
        'title' : request.json['title'],
        'text' : request.json['text'],
        'date' : datetime.today()
    })

    return jsonify({'_id' : str(ObjectId(id.inserted_id))})

# Get all blogs /blog
@app.route('/blog')
def getAllBlogs():
    docs = []

    for doc in db.blog.find():
        docs.append({
            'title' : doc['title'],
            'text' : doc['text'],
            'date' : doc['date'],
            '_id' : str(ObjectId(doc['_id']))
        })

    return jsonify(docs)

"""
        NOTE
"""
# Create a new note /note
@app.route('/note', methods=['POST'])
def newNote():
    id = db.note.insert_one({
        'text' : request.json['text'],
        'date' : datetime.today()
    })

    return jsonify({'_id' : str(ObjectId(id.inserted_id))})

# Get all notes /note
@app.route('/note')
def getAllNotes():
    docs = []

    for doc in db.note.find():
        docs.append({
            'text' : doc['text'],
            'date' : doc['date'],
            '_id' : str(ObjectId(doc['_id']))
        })

    return jsonify(docs)

"""
        TASK
"""
# Create a new task /task
@app.route('/task', methods=['POST'])
def newTasks():
    id = db.task.insert_one({
        'task' : request.json['task'],
        'date' : datetime.today()
    })

    return jsonify({'_id' : str(ObjectId(id.inserted_id))})

# Get all task /task
@app.route('/task')
def getAllTasks():
    docs = []

    for doc in db.task.find():
        docs.append({
            'task' : doc['task'],
            'date' : doc['date'],
            '_id' : str(ObjectId(doc['_id']))
        })

    return jsonify(docs)



if __name__ == '__main__':
    app.run(debug = True)