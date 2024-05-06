import os
from pathlib import Path
from dotenv import load_dotenv
import logging

load_dotenv()

def get_env_variable(var_name, default_value):
    value = os.getenv(var_name, default_value)
    if value == default_value:
        logging.warning(f"{var_name} is not set. Using default value: {value}")
    return value

QR_DIRECTORY = Path(get_env_variable('QR_CODE_DIR', './qr_codes'))
if not QR_DIRECTORY.exists():
    QR_DIRECTORY.mkdir(parents=True, exist_ok=True)
    logging.info(f"Created directory at {QR_DIRECTORY}")

FILL_COLOR = get_env_variable('FILL_COLOR', 'red')
BACK_COLOR = get_env_variable('BACK_COLOR', 'white')
SERVER_BASE_URL = get_env_variable('SERVER_BASE_URL', 'http://localhost:80')
SERVER_DOWNLOAD_FOLDER = get_env_variable('SERVER_DOWNLOAD_FOLDER', 'downloads')
SECRET_KEY = get_env_variable("SECRET_KEY", "secret-getenvkey")
ALGORITHM = get_env_variable("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(get_env_variable("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
ADMIN_USER = get_env_variable('ADMIN_USER', 'admin')
ADMIN_PASSWORD = get_env_variable('ADMIN_PASSWORD', 'secret')
