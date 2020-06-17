FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "export", "FLASK_APP=app.py" ]
CMD [ "export", "FLASK_ENV=development" ]
CMD [ "flask", "run" ]

 
 