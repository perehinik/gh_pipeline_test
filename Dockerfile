FROM python:3.8-alpine
#RUN mkdir /app
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt
#COPY pipeline_test.py ./
#ADD . /app
#WORKDIR /app
#COPY pipeline_test.py ./
WORKDIR /usr/local/bin
COPY pipeline_test.py .
CMD ["python", "pipeline_test.py"]