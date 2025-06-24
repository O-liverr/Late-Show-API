# Late-Show-API

# Phase 4 Code Challenge (2)

## Setup
1. Install dependencies:
    ```
    pipenv install flask flask_sqlalchemy flask_migrate flask-jwt-extended psycopg2-binary
    pipenv shell
    ```
2. Create the database:
    ```
    CREATE DATABASE late_show_db;
    ```
3. Export environment variables in `server/config.py`.
4. Migrate:
    ```
    export FLASK_APP=server/app.py
    flask db init
    flask db migrate -m "initial migration"
    flask db upgrade
    python server/seed.py
    ```

## Routes
- POST /register → register user
- POST /login → obtain JWT
- GET /episodes
- GET /episodes/<id>
- DELETE /episodes/<id> (JWT required)
- GET /guests
- POST /appearances (JWT required)

## Auth Flow
Send JWT token as:
