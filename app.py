from flask import Flask, request, render_template, redirect
from pymongo import MongoClient

app = Flask(__name__)

#connection between mongo and docker network

client = MongoClient("mongodb://mongo:27017/")
db = client["newdatabase"]
collection = db["newcollection"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        name = request.form["name"]
        email = request.form["email"]
        collection.insert_one({"name":name , "email":email})
        return redirect("/data")
    return render_template("form.html")

@app.route("/data")
def data():
    users = collection.find()
    return render_template("data.html", users=users)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)