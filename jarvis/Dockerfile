FROM python:3.11-slim

ENV APP_HOME=/jarvis

RUN mkdir -p $APP_HOME
WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip


COPY requirements.txt $APP_HOME/

RUN pip install -r requirements.txt

COPY . $APP_HOME/

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]