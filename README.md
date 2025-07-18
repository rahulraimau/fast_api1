��#   f a s t _ a p i 1 
 
Deploying Machine Learning Models with
FastAPI

📦 FastAPI Model Deployment – Project Summary
🧠 Project Title:
Iris Species Prediction API using FastAPI

🎯 Objective:
To build and deploy a machine learning model using FastAPI, enabling real-time predictions of Iris flower species from petal and sepal measurements via a REST API.

🔧 Project Workflow:
1.Data & Model Training

Used the Iris dataset from scikit-learn

Trained a Logistic Regression model for multi-class classification

Saved the trained model as iris_model.pkl using pickle

2. API Development

Built a FastAPI application with a /predict POST endpoint

Defined a Pydantic model to validate incoming data

Loaded the trained model at startup and returned predictions in JSON format

3.Local Testing

Tested API using Swagger UI at /docs and curl requests

Ensured the model returns correct species based on user input

4.Dockerization

Created a Dockerfile to containerize the FastAPI app

Enabled consistent deployment across environments

Ran container with docker run -p 8000:8000 iris-api

🚀 Outcome:
Developed a production-ready REST API for ML predictions

Learned end-to-end model deployment with FastAPI and Docker

Gained experience in real-time API testing, packaging, and scaling fundamentals



video link-https://www.loom.com/share/2479023ba9504c4ab0d4399757e1ccfd?sid=8e5c06fa-067d-43bf-8e4e-ef1814a5b6df
