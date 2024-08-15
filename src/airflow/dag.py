#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src.predict_anomalies import predict_anomalies

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 10),
    'retries': 1,
}

dag = DAG(
    'anomaly_detection_dag',
    default_args=default_args,
    description='A DAG for anomaly detection',
    schedule_interval='@daily',
)

def run_anomaly_detection():
    result = predict_anomalies('/app/data/UNSW_NB15_testing-set.csv')
    print(result)

task = PythonOperator(
    task_id='predict_anomalies',
    python_callable=run_anomaly_detection,
    dag=dag,
)

