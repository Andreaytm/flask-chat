import os 
from datetime import datetime
from flask import Flask, redirect, render_template, session, request, url_for

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "randomstring123")
messages = []

def add_message(username, message):
    """Add message to the `messages` list"""
    now = datetime.now().strftime("%H:%M:%S")
    messages.append({"timestamp": now, "from": username, "message": message})

@app.route('/', methods = ["GET", "POST"])
def index():
    """Main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]
    
    if "username" in session:
        return redirect(url_for("user", username = session["username"]))
        
    return render_template("index.html")
    
@app.route('/chat/<username>', methods =["POST", "GET"])
def user(username):
    """Add and display chat messages"""
    if request.method == "POST":
        username = session["username"]
        message = request.form["message"]
        add_message(username, message)
        return redirect(url_for("user", username = session["username"]))
    return render_template("chat.html", username = username, chat_messages = messages)
    
app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', '5000')), debug=False)
