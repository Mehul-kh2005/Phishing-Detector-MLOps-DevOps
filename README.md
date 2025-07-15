# 🛡️ Network Threat Detection using Machine Learning (Phishing Website Classification)

## 🔍 Project Overview

This project aims to detect phishing websites using machine learning classification models trained on a network security dataset. It follows a robust **end-to-end MLOps + DevOps pipeline** that includes:

✅ **ETL data pipelines** for ingestion, validation, and transformation  
✅ **Model training, evaluation**, and version tracking using **MLflow**  
✅ **Deployment of predictions** through a **FastAPI** web application  
✅ **Data ingestion and storage** via **MongoDB Atlas (Cloud DB)**  
✅ **Full CI/CD automation** using **GitHub Actions**  
✅ **DevOps workflows** for containerization, orchestration, and deployment using **Docker**, **Amazon ECR**, and **EC2**

This integration of both **MLOps** (machine learning lifecycle) and **DevOps** (build → test → deploy → monitor) practices ensures that the solution is **scalable, reproducible, and production-ready**.

---

## 🚀 Key Features

### 🧠 MLOps Capabilities

- ✅ **End-to-End ML Pipeline**: Ingestion, Validation, Transformation, Model Training  
- ✅ **Experiment Tracking** with **MLflow** (hosted on **DagsHub**)  
- ✅ **Modular architecture** with reusable components (`config` / `entity` based structure)  
- ✅ **MongoDB Atlas** for scalable and cloud-based data ingestion  
- ✅ **Auto-logging** of performance metrics (**Accuracy**, **F1**, **Precision**, **Recall**)  

---

### 🌐 Web Application

- ✅ **FastAPI-based REST API** for real-time prediction  
- ✅ **HTML Table rendering** of predictions using **Jinja2 templates**  
- ✅ **Swagger documentation** via `/docs` route for testing the API  

---

### 🛠️ DevOps & CI/CD

- ✅ **Dockerized Application** for cross-platform portability  
- ✅ **Secure Image Build & Push** to **Amazon Elastic Container Registry (ECR)**  
- ✅ **Automatic Deployment to AWS EC2 Instance** using SSH via **GitHub Actions**  
- ✅ **GitHub Secrets** integration for sensitive credentials  
- ✅ **Infrastructure commands** to bootstrap EC2 instance with Docker runtime  
- ✅ **Branch-based GitHub workflow** for CI/CD pipeline  

---

## 🧠 Problem Statement

Phishing attacks are one of the most common and dangerous cyber threats today. This project builds a machine learning-based classification system that detects whether a URL is **🟢 Safe** or **🔴 Malicious (Threat)**.

---

## ⚙️ Tech Stack

| Layer              | Tech Used                                     |
|-------------------|-----------------------------------------------|
| Language           | Python 3                                      |
| Web App            | FastAPI + Jinja2 Templates                    |
| ML Tracking        | MLflow + DagsHub                              |
| Data Storage       | MongoDB Atlas                                 |
| Deployment         | Docker + Amazon ECR + EC2                     |
| CI/CD              | GitHub Actions                                |
| Visualization      | HTML Table with Styled Predictions            |

---

## 🏗️ Project Architecture

```
📦 Network-Phishing-Detection  
│
├── .github/workflows/                      # GitHub Actions for CI/CD
│   └── main.yml                            # CI/CD pipeline to automate test/build/deploy
│
├── data_schema/                            # Contains schema definitions for input data
│   └── schema.yaml                         # Defines expected input data format and types
│
├── final_model/                            # Stores the final model and preprocessor
│   ├── model.pkl                           # Trained ML model
│   └── preprocessor.pkl                    # Fitted preprocessing pipeline (e.g., scaler/encoder)
│
├── Network_Data/                           # Raw or intermediate data used for training
│   └── phisingData.csv                     # Original phishing dataset
│
├── networksecurity/                        # Main project package
│   ├── cloud/                              # For cloud logic like S3, GCS etc.
│   │   └── s3_syncer.py                    # (Optional) to sync artifacts to/from cloud
│
│   ├── components/                         # Core ETL pipeline components
│   │   ├── data_ingestion.py               # Handles data loading from MongoDB/local sources
│   │   ├── data_transformation.py          # Preprocessing, feature engineering logic
│   │   ├── data_validation.py              # Validates schema, nulls, and structure
│   │   └── model_trainer.py                # Contains training logic and evaluation
│
│   ├── constant/                           # Constants used across the pipeline
│   │   └── training_pipeline/              # Training-related constant definitions
│
│   ├── entity/                             # Data classes for config and artifact objects
│   │   ├── artifact_entity.py              # Defines output artifacts for each pipeline stage
│   │   └── config_entity.py                # Holds configuration data for components
│
│   ├── exception/                          # Centralized exception handling
│   │   └── exception.py                    # Custom exception class with traceback logging
│
│   ├── logging/                            # Central logging utility
│   │   └── logger.py                       # Custom logger used across the project
│
│   ├── pipeline/                           # Manages the overall pipeline execution
│   │   └── training_pipeline.py            # Orchestrates the complete training pipeline
│
│   ├── utils/                              # Common utilities for reusability
│   │   ├── main_utils/
│   │   │   └── utils.py                    # General utilities (file I/O, Mongo helpers, etc.)
│   │   └── ml_utils/                       # ML-specific utilities
│   │       ├── metric/
│   │       │   └── classification_metrics.py  # Classification performance metrics
│   │       └── model/
│   │           └── estimator.py            # Custom estimator wrapper class
│
├── prediction_output/                      # Stores model prediction results
│   └── output.csv                          # Output file with predicted results
│
├── templates/                              # HTML templates for FastAPI
│   └── table.html                          # Displays predictions in a styled table
│
├── valid_data/                             # Validated test datasets
│   └── test.csv                            # Test file post-validation
│
├── app.py                                  # FastAPI app to serve predictions via REST API
├── main.py                                 # Script to run the training pipeline end-to-end
├── push_data.py                            # Script to push local data to MongoDB Atlas
├── Dockerfile                              # Docker container definition
├── .env                                    # Stores environment variables and secrets (ignored in .gitignore)
├── requirements.txt                        # Python packages needed to run the project
├── setup.py                                # Makes the project pip-installable
└── README.md                               # You're here! Full documentation and project overview
```

---

## 🧪 ML Pipeline (ETL)

| Stage              | Description |
|-------------------|-------------|
| `Data Ingestion`  | Loads raw data, pushes to MongoDB, reads from it |
| `Validation`      | Validates schema, checks nulls etc.              |
| `Transformation`  | Applies encoding, imputation, scaling            |
| `Model Trainer`   | Trains multiple models, performs grid search     |
| `Evaluation`      | Uses `accuracy`, `F1`, `Precision`, `Recall`     |
| `Prediction`      | Outputs `Safe` / `Threat` label (with emoji 🟢/🔴) |

All experiments are logged to **MLflow via DagsHub**.

---

## 🌐 Web Application (FastAPI)

A lightweight and styled FastAPI app to:
- ✅ Trigger model training
- ✅ Upload `.csv` file for predictions
- ✅ See styled prediction output in tabular form

🔗 Visit `/docs` for Swagger UI.  
🔍 Visit `/view-prediction` to visually inspect predictions.

---

## 🌍 MongoDB Atlas Integration

1. **Push Data from Local**:
   ```bash
   python push_data.py
   ```

2. **Read from MongoDB Atlas**:  
   Automatically handled in data ingestion using:

   ```python
   client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=certifi.where())
   ```

---

## 🐳 Docker Setup

To build and run locally:

```bash
# Build image
docker build -t Phishing-Detector-MLOps-DevOps .

# Run container
docker run -p 8000:8000 Phishing-Detector-MLOps-DevOps
```

---

## 🚀 AWS Deployment (ECR + EC2)

### 🔐 GitHub Secrets

Set these secrets in your GitHub repository:

```env
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=
AWS_ECR_LOGIN_URI=
ECR_REPOSITORY_NAME=
```

### 💡 EC2 Setup (One-Time)

Run the following on a fresh EC2 instance:

```bash
# Optional
sudo apt update -y && sudo apt upgrade -y

# Docker Installation
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add current user to Docker group
sudo usermod -aG docker ubuntu
newgrp docker
```

---

## 🛠️ GitHub Actions

Workflow file: `.github/workflows/main.yml`

It performs:

- ✅ Builds Docker Image  
- ✅ Pushes Image to Amazon ECR  
- ✅ SSH into EC2  
- ✅ Pulls Image on EC2  
- ✅ Runs Docker Container  

---

## 🔁 CI/CD Flow

```vbnet
Push to Main Branch
    ↓
GitHub Actions Triggered
    ↓
Build Docker Image
    ↓
Push to Amazon ECR
    ↓
SSH into EC2
    ↓
Pull & Run Docker Container
    ↓
App Live on Port 8080! 🚀
```

---

## 🧪 How to Run Locally

### 🐍 Setup Virtual Environment

```bash
# 1. Create the virtual environment named `mlops_env`
conda create -n mlops_env python=3.10 -y

# 2. Activate the environment (on Linux/Mac)
conda activate mlops_env

# Install dependencies
pip install -r requirements.txt
```

---

## 🧠 Train the Model

```bash
python main.py
```

---

## 🌐 Run the Web App

```bash
uvicorn app:app --reload
```

### Visit:

- http://localhost:8000/docs  
- http://localhost:8000/view-prediction

---

## 📈 MLflow + DagsHub

Integrated with DagsHub for model tracking.  
No extra steps needed — all metrics are automatically logged via:

```python
dagshub.init(
    repo_owner="Mehul-kh2005", 
    repo_name="Phishing-Detector-MLOps-DevOps", 
    mlflow=True
)
```

---

## 🙋 Author

### Mehul Khandelwal - 🔗 [GitHub](https://github.com/Mehul-kh2005/Phishing-Detector-MLOps-DevOps) | [LinkedIn](https://www.linkedin.com/in/mehulkhandelwal2005/)

📝 *This project was developed as part of a machine learning, MLOps, and DevOps exercise focused on classification modeling for detecting phishing websites. It integrates a complete ETL pipeline, model training, a FastAPI-based web application, containerization with Docker, and CI/CD deployment to AWS using GitHub Actions — delivering a real-world, production-ready implementation of modern data science and DevOps workflows.*