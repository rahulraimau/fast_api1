A client needs a REST API that predicts flower species based on petal and sepal measurements using the Iris dataset.
We first train a machine learning model (e.g., Logistic Regression or Decision Tree) on the dataset and save it using pickle.
Then, we develop a FastAPI service that loads the model and exposes a /predict endpoint to accept JSON inputs and return predictions.
The API is tested locally using tools like Swagger UI, curl, or Python requests.
Finally, the solution is containerized with Docker and deployed on a cloud platform like Render, Heroku, or AWS for real-time use.
