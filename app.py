#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from flask import Flask, request, render_template
import pickle
import warnings
warnings.filterwarnings('ignore')


# In[2]:


app = Flask(__name__)


# In[3]:


model = pickle.load(open('model.pkl','rb'))


# In[4]:


model


# In[5]:


@app.route('/')
def home():
    return render_template('index.html')


# In[6]:


@app.route('/predict',methods=['POST'])
def predict():
    int_features = [ int(x) for x in request.form.values() ]
    final_features = [ np.array(int_features) ]
    prediction = model.predict(final_features)
    
    output = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


# In[7]:


if __name__ == '__main__':
    app.run(debug=True)

