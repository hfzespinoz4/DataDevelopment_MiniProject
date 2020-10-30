import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env 


app = Flask(__name__)

# Adding enviroment properties to the project, all this is seted up in Heroku
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

# Adding Mongo Construtor
mongo = PyMongo(app)

@app.route("/")
@app.route("/get_tasks")

def get_tasks():
    tasks = mongo.db.tasks.find()
    # with the rendering of the template, we'll pass that tasks 
    # variable through to the template: tasks=tasks. The first 'tasks'
    # is what the template will use, and that's equal to the second 'tasks',
    # which is our variable defined above.
    return render_template("tasks.html", tasks=tasks)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
