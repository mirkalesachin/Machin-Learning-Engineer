FROM python:3.11-slim
WORKDIR /trainer
COPY requirements.txt train.py ./
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python","train.py","--data-uri","mock://customers","--epochs","3"]
