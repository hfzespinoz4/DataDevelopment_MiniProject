import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "task_manager"
app.config["MONGO_URI"] = 'mongodb+srv://hfzespinoz4:hf.939013@myfirstcluster.xvtwi.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
# When the application is run the default function that will be called will be get_tasks because of the / decorator
@app.route('/get_tasks')
def get_task():
    # We are going to supply a task collection, wich will be returned from making a call directly to Mongo
    # We use find() method, wich will return everything in our tasks collection
    return render_template("tasks.html", tasks=mongo.db.tasks.find())
    

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)