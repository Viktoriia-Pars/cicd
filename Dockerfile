FROM python:3.9

COPY ./database_phone /src
COPY ./database_phone/requirements.txt /src/requirements.txt
RUN pip3 install --no-cache-dir --upgrade -r /src/requirements.txt

EXPOSE 6060

WORKDIR src

RUN chmod +x /src/phone_script.sh
RUN /src/phone_script.sh

CMD ["python3", "manage.py", "runserver", "0.0.0.0:6060"]