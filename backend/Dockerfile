FROM arm64v8/ubuntu:20.04

WORKDIR '/brain_tumor_analysis'
ADD . /brain_tumor_analysis

COPY . .
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 download_models.py

EXPOSE 6000

CMD ["python3", "backend.py"]
