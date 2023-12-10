FROM python:3.11.7

WORKDIR '/brain_tumor_analysis'
ADD . /brain_tumor_analysis

COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN python3 download_models.py

EXPOSE 3500

CMD ["python3", "backend.py"]
