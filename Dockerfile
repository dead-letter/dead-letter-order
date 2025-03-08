FROM python:3.11-alpine

# configure app
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN apk add curl
COPY . .

# run app
ENV PYTHONUNBUFFERED=1
CMD ["python", "main.py"]
