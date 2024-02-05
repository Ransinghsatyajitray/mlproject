from flask import Flask,request,render_template
from numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler

application = Flask(__name__) # entry point
app = application

# Route for the a home page

@app.route('/')
def index():
    return render_template('index.html') # when we use render template it goes and search for templates folder and index.html within it

@app.route('/predictdata', methods=["GET",'POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        pass
    
