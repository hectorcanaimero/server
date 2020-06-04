FROM python:3.6
ADD . /app
WORKDIR /app
EXPOSE 4000
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3","index.py"]