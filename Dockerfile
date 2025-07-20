### STAGE 1 BUILD

FROM pytorch/pytorch:2.6.0-cuda11.8-cudnn9-runtime AS builder

RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev 

WORKDIR /app
COPY . /app

# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 

RUN pip install -r requirements.txt

RUN pip install gunicorn==23.0.0

EXPOSE 8000 
 