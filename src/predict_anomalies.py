#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import joblib
from preprocess import preprocess_data

def predict_anomalies(file_path):
    # Load the model
    model = joblib.load('model.pkl')
    
    data = preprocess_data(file_path)
    
    predictions = model.predict(data)
    
    return predictions

if __name__ == "__main__":
    print(predict_anomalies('../data/UNSW_NB15_testing-set.csv'))

