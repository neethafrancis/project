from flask import render_template
from app.app import app

def home():
    return render_template('index.html')



#routes
app.add_url_rule("/", view_func=home, methods= ["GET","POST"])