import os
from dotenv import load_dotenv
load_dotenv()

SQLALCHEMY_DATABASE_URI = "postgresql://<user>:<password>@localhost:5432/late_show_db"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or "jwt-secret"
