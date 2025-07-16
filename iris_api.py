from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from sklearn.datasets import load_iris

# Load the saved model
model = pickle.load(open("iris_model.pkl", "rb"))
iris_data = load_iris()

app = FastAPI()

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Species Predictor API!"}

@app.post("/predict")
def predict_species(input: IrisInput):
    data = np.array([[input.sepal_length, input.sepal_width,
                      input.petal_length, input.petal_width]])
    pred = model.predict(data)[0]
    species = iris_data.target_names[pred]
    return {"predicted_species": species}