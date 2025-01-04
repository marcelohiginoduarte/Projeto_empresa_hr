FROM python:3.10-slim

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


EXPOSE 8001


CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]