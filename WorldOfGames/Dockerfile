FROM python:alpine3.14
WORKDIR /app
COPY . /app
EXPOSE 8777
RUN pip install flask
RUN pip install requests
CMD ["python", "MainScore.py"]
