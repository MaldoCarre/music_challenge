# music_challenge , usage steps
### 1) Create a new directory and clone the project
### 2) Create a python virtual environment 'python3 -m venv /path/to/new/virtual/environment'
### 3) Start the virtual environment 'source /path/to/new/virtual/environment/bin/activate'
### 4) Install the requirements using 'pip install -r requirements.txt'
### 5) Excecute 'python manage.py migrate'
### 6) Excecute 'python manage.py runserver'
### 7) Once the server is running you con use you favorite app to thest the 'http://localhost:8000/artist?name=' endpoint (in my case I use insomnia)
### 8) You can also run the unittest excecuting 'python manage.py test music'
