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

# # Install PyTorch
# RUN pip install torch==2.6.0 torchvision==0.21.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu118

# Install other requirements
RUN pip install -r requirements.txt

RUN pip install gunicorn==23.0.0

# Run Django server
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000", "--noreload"]
 
 
# RUN useradd -m -r appuser && \
#    mkdir /app && \
#    chown -R appuser /app
 
 
# #Switch to non-root user
# USER appuser
 
# Expose the application port
EXPOSE 8000 
 
# # Start the application using Gunicorn
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "2", "backend.wsgi:application"]