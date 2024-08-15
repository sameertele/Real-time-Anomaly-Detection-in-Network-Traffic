#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import joblib
from sklearn.ensemble import IsolationForest
from preprocess import preprocess_data

def train_model():
    data = preprocess_data('../data/UNSW_NB15_training-set.csv')
    
    model = IsolationForest(contamination=0.01)
    model.fit(data)
    
    joblib.dump(model, 'model.pkl')

if __name__ == "__main__":
    train_model()

