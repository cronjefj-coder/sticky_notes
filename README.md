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



