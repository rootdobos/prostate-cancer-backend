# prostate-cancer-backend


## Setup Instructions

### 1. Initialize Git Submodules
```bash
git submodule init
git submodule update --init --recursive
```

### 2. Setup .env

Create a .env file based on the .env.example provided in the root folder.

Modify the STORAGE variable in the .env file to set your desired storage path.

Example storage is in the root folder

### 3. Create and activate venv

```bash
python -m venv venv
run venv/Scripts/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```
Install the Pytorch version good for your system [Pytorch](https://pytorch.org/get-started/locally/)

Pytorch 2.6.0 with cuda 11.8 was used in development

### 5. Run the server

```bash
python manage.py runserver
```