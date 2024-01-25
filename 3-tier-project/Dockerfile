FROM public.ecr.aws/docker/library/python:3.9

COPY . /code/
WORKDIR /code
RUN apt update
RUN apt-get install -y python3-dev default-libmysqlclient-dev
RUN apt install -y python3-mysqldb
RUN pip install -r requirements.txt
EXPOSE 1111

CMD ["/bin/bash", "-c", "python3 app.py"]
