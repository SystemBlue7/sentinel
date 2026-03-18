import os
from dotenv import load_dotenv

# Cargar variables del .env
load_dotenv()

# Variables del sistema
ENV = os.getenv("ENV")
APP_NAME = os.getenv("APP_NAME")