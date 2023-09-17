# Real-Time Joke API

This project provides a real-time Joke API built with Django REST Framework (DRF). It utilizes Django models, serializers, and integrates with Channels, Redis, Celery, and Celery Beat to provide real-time joke data.

## Features

- Retrieve jokes in real-time using WebSocket communication.
- Automatic periodic updates of joke data using Celery Beat.
- Scalable architecture using Channels, Redis, and Celery.

## Technologies Used

- Django REST Framework (DRF)
- Django Channels
- Redis
- Celery
- Celery Beat
- ASGI Server (Daphne)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/hwandev12/django-realtime.git
pip install -r requirements.txt
```
celery -A your_project_name beat -l info
```
celery -A your_project_name worker -l info
```
daphne your_project_name.asgi:application
```

Feel free to customize the README file with your project-specific details, such as your project's name, database configuration, and any additional information or instructions that may be relevant.