FROM ubuntu:20.04
RUN apt update -y
RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install python3.8 -y
RUN apt install python3-pip -y
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD [ "python3", "server.py"]