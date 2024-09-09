# Real-Time Anomaly Detection in Network Traffic

This project implements a real-time anomaly detection system for network traffic using machine learning algorithms, specifically **Isolation Forest**. The system is containerized with **Docker** and orchestrated using **Kubernetes** for scalability. Additionally, **Apache Airflow** is used for automated data pipeline management.

## Project Overview

- **Dataset**: UNSW-NB15 dataset
- **Machine Learning Model**: Isolation Forest
- **Technologies**:
  - **Python** for data processing and model development
  - **Docker** for containerization
  - **Kubernetes** for orchestration
  - **Airflow** for managing the data pipeline
  - **scikit-learn** for machine learning
- **Goal**: To build and deploy a real-time anomaly detection system capable of identifying suspicious or abnormal network traffic.

## Dataset

The dataset used in this project is the **UNSW-NB15** dataset. It contains real network traffic data labeled as either normal or abnormal, with features such as `src_bytes`, `dst_bytes`, `duration`, `sport`, `dport`, and `proto`.

- **Training Data**: `UNSW_NB15_training-set.csv`
- **Test Data**: `UNSW_NB15_test-set.csv`

The dataset can be downloaded from the [UNSW-NB15 Dataset page](https://www.unsw.edu.au/engineering/our-research/research-groups/cybersecurity/unsw-cyber-security/unsw-nb15-dataset).
