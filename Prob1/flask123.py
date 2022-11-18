#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle


# In[2]:


app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
Prediction_check = pd.read_csv('Final_Prediction_Output.csv')

@app.route('/')
def home():
    return render_template('predict.html')

@app.route('/predict',methods=['POST'])
def predict():
    Customer_ID = request.form.get('CustomerID')
    print(Customer_ID)
    Customer_Data = Prediction_check.query("CustomerID == @Customer_ID")["Fraud_Yes_No"].iloc[0]
    
    output = str(Customer_Data)
    if output == 'NO' :
        output = 'Not Fraud'
    else :
        output = 'Fraud'
    print("OUTPUT  ",output)
    return render_template('predict.html', prediction_text='The given CustomerIDs claim is {output_pred}'.format(output_pred=output))


if __name__ == "__main__":
    app.run(debug=True)

