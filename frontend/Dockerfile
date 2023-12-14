FROM python:3.11.7
# python 3.11.7 is used as the base image.

#set the working directory inside the container to /brain_tumor_analysis.
WORKDIR '/brain_tumor_analysis'
ADD . /brain_tumor_analysis
# Adds the entire current directory into the /brain_tumor_analysis directory within the container.

COPY . . 
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
# Upgrades pip and installs the Python dependencies listed in requirements.txt using pip3.

EXPOSE 3000
#Exposes port 3000 to allow communication with the container from the host system.

CMD ["python3", "frontend.py"]
# specifies the command to run when the container starts.