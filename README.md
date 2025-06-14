# prostate-cancer-backend
create a .env based on the .env.example and modify the storage directory in it (example provided in the root folder)
create a python virtual environment: python -m venv venv
run venv/Scripts/activate
install dependencies: pip install -r requirements.txt
you have to install separately the Pytorch from https://pytorch.org/get-started/locally/
Pytorch 2.6.0 with cuda 11.8 was used in development
run the server with python manage.py runserver