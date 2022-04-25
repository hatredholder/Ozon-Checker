FROM python:3.10.4-slim-buster
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . . 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]