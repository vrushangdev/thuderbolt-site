#Getting Latest Python Runtime As Parrent Image
FROM python:3.7
ENV  PYTHONUNBUFFERED 1
WORKDIR /usr/code/

COPY thunderbolt/requirements.txt /usr/code
RUN pip install -r requirements.txt
COPY . /usr/code/
RUN ls
WORKDIR /usr/code/thunderbolt/
RUN ls

#Depedencies Installed Now Lets Copy All Files To Working Diretory
#ENV NAME Thunder

CMD ["python","manage.py","runserver","0.0.0.0:8000"]
