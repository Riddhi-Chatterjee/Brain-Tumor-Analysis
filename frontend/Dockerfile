FROM python:3.11.7

WORKDIR '/brain_tumor_analysis'
ADD . /brain_tumor_analysis

COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "frontend.py"]
