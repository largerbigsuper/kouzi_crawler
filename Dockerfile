FROM python:3

WORKDIR /kouzi_crawler
ADD . .
RUN pip install -r requirements.txt
CMD [ "python", "./run.py"]
