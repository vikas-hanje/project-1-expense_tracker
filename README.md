# Personal Expense Tracker

A lightweight web application built with Python and Flask for logging, categorizing, and managing daily expenses. This project was developed to practice full-stack fundamentals, focusing on raw SQL queries, relational database design, and server-side rendering.

Features

    Full CRUD Operations: Seamlessly create, read, update, and delete expenses.

    Relational Database Design: Expenses are strictly linked to separate Categories using Foreign Keys, ensuring data integrity.

    Raw SQL Implementation: Connects to MySQL using mysql-connector-python to execute custom SQL queries directly.

    Secure Configuration: Environment variables (.env) are used to keep database credentials out of the source code.

Tech Stack

    Backend: Python, Flask

    Database: MySQL

    Frontend: HTML5, CSS3 (Flexbox/Grid), Jinja2 Templating

Getting Started

    Clone this repository to your local machine.

    Create and activate a virtual environment:
    Bash

    python -m venv env
    source env/bin/activate  # On Windows use: env\Scripts\activate

    Install the required dependencies:
    Bash

    pip install -r requirements.txt

    Create a .env file in the root directory and add your MySQL database credentials.

    Set up your database by running the queries found in schema.sql.

    Start the Flask server:
    Bash

    python app.py

    Open your browser and navigate to (http://127.0.0.1:5000).