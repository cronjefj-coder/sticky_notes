# Sticky Notes Application
## Getting Started

This document provides guidance on how to setup and run Sticky Notes.

## Prerequisites

Python 3.11 is required to be installed on your system.

## Local setup

Take note that this setup is for a Windows operating system using command prompt. If you have a MacOS or Linux setup, the commands will differ. Please refer to MacOS or Linux terminal documentation for equivalent commands. Clone the github repository for the application.

1. **Setup an isolated Python virtual environment:**

To setup a virtual environment on your system, use the following command in command prompt.
```pip -m venv env_name```.

To activate the environment,  run ```env_name\Scripts\activate```. Ensure that you are within the directory where the environment was created.

2. **Upgrade pip and install project dependencies:**

Make sure you have the latest pip version by running ```python -m pip install --upgrade pip```.

Run the following command for project dependencies: ```python -m pip install -r requirements.txt```

3. **Database update:**

Run ```python manage.py migrate``` to ensure the database is up to date.

4. **Admin superuser:**

If you want access to the Django administration section of the application, you will have to create an admin superuser by running ```python manage.py createsuperuser```.

5. **Run the application:**

To run the application use the command ```python manage.py runserver```. This will start the local server http://127.0.0.1:8000/. You can open your preferred browser and navigate to the server url. NOTE to access Django admin, add 'admin/' to the back of the server url.

## Application Features:

When you have navigated to the server url, the application will show notes already created, if any. You will be able to create new notes, update existing notes and delete existing notes.

## After app usage:

Do take note that after you have used the application and closed your browser, the server must be stopped. Within the command prompt terminal, navigate to the bottom and press CTRL-C to stop the server.

Also note to deactivate your virtual environment when you are done with the application. In the command prompt terminal, type ```deactivate``` and the virtual environment will be deactivated.


