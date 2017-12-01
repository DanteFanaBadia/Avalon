#Base official python images
FROM python:3

#Setting env variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE Avalon.settings

#Support guy
MAINTAINER Dante Fana <dfana@dfb.com.do>

#Create folder, copy project files, and install packages
COPY /requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt
RUN mkdir -p /usr/Avalon
WORKDIR /usr/Avalon

#Expose project port
EXPOSE 8000

#Command to run app
CMD [ "python", "./manage.py", "runserver"]