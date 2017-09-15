FROM python:3.6
ADD ./ /code
RUN cd /code && pip install -r requirements.txt
WORKDIR /code

EXPOSE 8080
ENTRYPOINT ["python3", "main.py"]
