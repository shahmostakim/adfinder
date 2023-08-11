FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

RUN python3 nltkdownloader.py  

RUN python3 manage.py makemigrations

RUN python3 manage.py migrate

EXPOSE 8000 

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"] 