from flask import Flask, request, render_template 
  
app = Flask(__name__)   
  

@app.route('/hello', methods =["GET", "POST"])

def first():
    return(render_template("home.html"))

@app.route('/second',methods=["POST"])

def second():
    name=request.form["name"]
    return" Hello "+name