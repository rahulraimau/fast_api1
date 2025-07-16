# Iris Classifier API FAQ

## 1. What is FastAPI and Why Use It for Model Deployment?
**FastAPI** is a Python framework for building fast web APIs.
- **Why use it**:
  - Creates simple endpoints (e.g., `/predict` for Iris classifier).
  - Handles many requests efficiently (async).
  - Validates inputs (e.g., four Iris measurements) using Pydantic.
  - Auto-generates Swagger UI (`http://localhost:8000/docs`) for testing.
  - Integrates with ML models (e.g., loads `iris_model.pkl`).
  - Scales well with Docker or cloud for production.

## 2. How to Build, Test, and Deploy an API for an ML Model?
**Build**:
- Train a logistic regression model on the Iris dataset and save as `iris_model.pkl`:
  ```python
  from sklearn.datasets import load_iris
  from sklearn.model_selection import train_test_split
  from sklearn.linear_model import LogisticRegression
  import pickle
  iris = load_iris()
  X, y = iris.data, iris.target
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  model = LogisticRegression(max_iter=200)
  model.fit(X_train, y_train)
  with open("iris_model.pkl", "wb") as f:
      pickle.dump(model, f)
  ```
- Create a FastAPI app (`iris_classifier_app.py`) with a `/predict` endpoint:
  ```python
  from fastapi import FastAPI, HTTPException
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
          raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")
  ```
- Install dependencies: `pip install scikit-learn fastapi uvicorn pydantic numpy`.

**Test**:
- Run locally: `python iris_classifier_app.py`.
- Test with PowerShell:
  ```powershell
  Invoke-WebRequest -Uri "http://localhost:8000/predict" -Method Post -Headers @{"Content-Type"="application/json"} -Body '{"sepal_length": 5.1, "sepal_width": 3.5, "petal_length": 1.4, "petal_width": 0.2}' | Select-Object -ExpandProperty Content
  ```
- Or use `http://localhost:8000/docs` in a browser.
- Fix `http://localhost:8000` issues: Ensure server runs, port 8000 is free (`netstat -aon | findstr :8000`), and firewall allows port 8000.

**Deploy** (using Docker in WSL 2 due to Docker Desktop issues):
- Install WSL 2: `wsl --install`.
- Install Docker in WSL 2 (Ubuntu):
  ```bash
  sudo apt update
  sudo apt install -y docker-ce docker-ce-cli containerd.io
  sudo usermod -aG docker $USER
  ```
- Create `Dockerfile`:
  ```dockerfile
  FROM python:3.9-slim
  WORKDIR /app
  COPY . .
  RUN pip install scikit-learn fastapi uvicorn pydantic numpy
  EXPOSE 8000
  CMD ["uvicorn", "iris_classifier_app:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
- Build and run: `docker build -t iris-api . && docker run -p 8000:8000 iris-api`.

## 3. Best Practices for Productionizing ML Models
- **Model**:
  - Validate performance (e.g., accuracy on test set).
  - Version models (e.g., `iris_model_v1.pkl`).
- **API**:
  - Add logging:
    ```python
    import logging
    logging.basicConfig(level=logging.INFO)
    ```
  - Add root endpoint: `@app.get("/")`.
- **Testing**:
  - Unit tests for model and API (use `pytest`, `httpx`).
  - Load test with `locust`.
- **Deployment**:
  - Use Docker in WSL 2 (as above) or cloud (AWS ECS).
  - Ensure port 8000 is open in firewall.
- **Production**:
  - Scale with Kubernetes or load balancers.
  - Monitor with Prometheus/Grafana.
  - Secure with HTTPS, authentication.
  - Update model with new data via CI/CD.