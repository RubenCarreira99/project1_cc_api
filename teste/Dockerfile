FROM python:latest

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SUPERUSER_USERNAME=admin
ENV DJANGO_SUPERUSER_EMAIL=admin@example.com
ENV DJANGO_SUPERUSER_PASSWORD=superuserpassword

WORKDIR /api_service/

# install dependencies  
COPY ./requirements.txt .

RUN pip install -r ./requirements.txt 
#Use requirements.txt to install all the dependencies

COPY . .

#COPY ./.env .

RUN python manage.py migrate --no-input
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('${DJANGO_SUPERUSER_USERNAME}', '${DJANGO_SUPERUSER_EMAIL}', '${DJANGO_SUPERUSER_PASSWORD}')" | python manage.py shell

RUN chmod 777 ./.env
#RUN chmod +x ./migratedb.sh

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
