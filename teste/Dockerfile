FROM python:latest

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SUPERUSER_USERNAME=admin1234
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_PASSWORD=superuserpassword

WORKDIR /api_service/

# install dependencies  
COPY ./requirements.txt .

RUN pip install -r ./requirements.txt 
#Use requirements.txt to install all the dependencies

COPY . .

RUN chmod 777 ./migratedb.sh

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]