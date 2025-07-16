FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# 🧠 Run model training script during build
RUN python train_model.py

EXPOSE 8000

CMD ["uvicorn", "iris_api:app", "--host", "0.0.0.0", "--port", "8000"]