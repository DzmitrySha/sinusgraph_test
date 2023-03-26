FROM python:3.11.2-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8585:8000

CMD ["python", "manage.py", "runserver"]
