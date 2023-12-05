FROM --platform=linux/arm64/v8 python:alpine

WORKDIR '/brain_tumor_analysis'
ADD . /brain_tumor_analysis

COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install torch===1.6.0 torchvision===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN python3 download_models.py

EXPOSE 6000

CMD ["python3", "backend.py"]
