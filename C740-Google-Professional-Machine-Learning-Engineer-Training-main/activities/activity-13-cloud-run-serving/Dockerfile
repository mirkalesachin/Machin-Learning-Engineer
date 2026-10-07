FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt app.py ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["gunicorn","-b",":8080","app:app"]
