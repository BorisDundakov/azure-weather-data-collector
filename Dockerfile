FROM python:3.10-slim
COPY application /application/
COPY requirements.txt .
USER root
RUN pip install --no-cache-dir -r requirements.txt 
WORKDIR /application
CMD ["python", "main.py"]