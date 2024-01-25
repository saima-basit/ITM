FROM public.ecr.aws/docker/library/python:3.9

COPY . /code/
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 8000

CMD ["/bin/bash", "-c", "python3 app.py"]
