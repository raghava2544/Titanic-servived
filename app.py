
from flask import Flask, render_template,request


import pandas as pd
from sklearn.linear_model import LogisticRegressionCV
import pickle

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
   if request.method=='POST':
      Pclass= request.form['Pclass']
      Sex = request.form['Sex']
      Parch=  request.form['Parch']
      data=[[int(Pclass),int(Sex),int(Parch)]]



      clf_model = pickle.load(open("Tit1.pkl",mode="rb"))


      prediction=clf_model.predict(data)[0]
      final=""
      if prediction==1:
         final="Person is survived"
      else:
         final = "Person is not survived"
      return render_template('index.html',prediction=final)

if __name__ == '__main__':
   app.run()