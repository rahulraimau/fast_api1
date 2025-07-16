FastAPI for ML Model Deployment
Slide 1: Welcome to FastAPI

Title: Deploying ML Models with FastAPI
Content: 
Learn to build and deploy an Iris classifier API.
For beginners with Python/ML basics.
Analogy: FastAPI is like a waiter serving ML predictions to users.


Visual: Chef (model) and waiter (FastAPI) in a restaurant.
Reference: FastAPI Docs

Slide 2: What is FastAPI?

Content:
Python framework for fast, modern web APIs.
Key features:
Fast: Async for high performance.
Easy: Simple code, auto-docs at /docs.
Reliable: Validates inputs, handles errors.


Ideal for serving ML models (e.g., Iris predictions).


Visual: Diagram: User → Request → FastAPI → Response.
Reference: DataCamp Tutorial

Slide 3: Why FastAPI for AI?

Content:
Turns ML models into APIs for apps/users.
Integrates with scikit-learn (e.g., Iris model).
Scales with Docker/cloud (AWS, Azure).
Provides Swagger UI for easy testing (http://localhost:8000/docs).


Visual: Flowchart: ML Model → FastAPI → API → Users.
Reference: GeeksforGeeks FastAPI

Slide 4: Iris Classifier Example

Content:
Goal: Predict Iris flower type (setosa, versicolor, virginica).
Analogy: Florist (API) identifies flowers from measurements.
Model: Logistic regression on Iris dataset.
Code: Train and save model:from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
with open("iris_model.pkl", "wb") as f:
    pickle.dump(model, f)




Visual: Iris flower with labeled measurements.

Slide 5: Building the FastAPI App

Content:
Create /predict endpoint to load model and predict.
Code (in iris_classifier_app.py):from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
app = FastAPI()
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
@app.post("/predict")
async def predict_iris(data: IrisInput):
    try:
        with open("iris_model.pkl", "rb") as f:
            model = pickle.load(f)
        input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
        prediction = model.predict(input_data)
        return {"prediction": iris.target_names[prediction[0]]}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Prediction error")




Visual: Diagram: JSON Input → FastAPI → Model → JSON Output.
Reference: TestDriven.io

Slide 6: How the Model Works

Content:
Logistic Regression:
Inputs: 4 measurements (sepal/petal length/width).
Calculates scores: ( z = w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4 + b ).
Softmax for probabilities: ( P(\text{class}) = \frac{e^z}{\sum e^z} ).
Picks highest-probability class (e.g., setosa).


Analogy: Florist guessing flower type from measurements.


Visual: Graph of Iris data with decision boundaries.
Reference: YouTube: Deploy ML

Slide 7: Testing the API

Content:
Run: python iris_classifier_app.py (in C:\Users\DELL\PycharmProjects\PythonProject12).
Test with PowerShell:Invoke-WebRequest -Uri "http://localhost:8000/predict" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}'


Or use Swagger UI: http://localhost:8000/docs.
Fix Issues: Check port 8000 (netstat -aon | findstr :8000), allow firewall (TCP 8000).


Visual: Screenshot of Swagger UI response.
Reference: YouTube: REST API

Slide 8: Deploying with Docker (WSL 2)

Content:
Why: Docker ensures consistency (no dependency issues).
Since Docker Desktop fails: Use WSL 2.
Steps:
Install WSL 2: wsl --install.
Install Docker in Ubuntu: sudo apt install -y docker-ce.
Create Dockerfile:FROM python:3.9-slim
WORKDIR /app
COPY . C:\Users\DELL\PycharmProjects\PythonProject12
RUN pip install scikit-learn fastapi uvicorn pydantic numpy
EXPOSE 8000
CMD ["uvicorn", "iris_classifier_app:app", "--host", "0.0.0.0", "--port", "8000"]


Build/run: docker build -t iris-api . && docker run -p 8000: C:\Users\DELL\PycharmProjects\PythonProject128000 iris-api.




Visual: Diagram: Code → Docker → Cloud.
Reference: FastAPI Docker

Slide 9: Production Best Practices

Content:
Validate: Test model accuracy.
Monitor: Add logging:import logging
logging.basicConfig(level=logging.INFO)


Scale: Use Kubernetes/AWS ECS.
Secure: Add HTTPS, OAuth2.
Update: Retrain model via CI/CD.


Visual: Checklist: Validate, Monitor, Scale, Secure.
Reference: Northflank Guide

Slide 10: Get Started!

Content:
Practice: Build/test Iris API locally.
Explore: Add logging, cloud deployment.
Resources:
FastAPI Docs
YouTube: FastAPI & Docker


Deploy your ML models with confidence!


Visual: Roadmap: Build → Test → Deploy → Scale.
