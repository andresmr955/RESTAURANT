#Use an python base image
FROM python:3.13.1
# Stablish a directory inside de container
WORKDIR /app
#Copy all files from our app to the container
COPY requirements.txt requirements.txt
#Install all dependencies 
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]