FROM python:latest

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /api_service/

# install dependencies  
COPY ./requirements.txt .

RUN pip install -r ./requirements.txt 
#Use requirements.txt to install all the dependencies

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
