import os
from typing import List
import qrcode
import logging
from pathlib import Path

def list_qr_codes(directory_path: Path) -> List[str]:
    """
    Lists all QR code images in the specified directory by returning their filenames.
    """
    try:
        return [f for f in os.listdir(directory_path) if f.endswith('.png')]
    except FileNotFoundError:
        logging.error(f"Directory not found: {directory_path}")
        raise
    except OSError as e:
        logging.error(f"OS error while listing QR codes: {e}")
        raise

def generate_qr_code(data: str, path: Path, fill_color: str = 'red', back_color: str = 'white', size: int = 10):
    """
    Generates a QR code and saves it to a specified file path.
    """
    logging.debug("Starting QR code generation")
    try:
        qr = qrcode.QRCode(version=1, box_size=size, border=5)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color=fill_color, back_color=back_color)
        img.save(str(path))
        logging.info(f"QR code saved to {path}")
    except Exception as e:
        logging.error(f"Failed to generate/save QR code: {e}")
        raise

def delete_qr_code(file_path: Path):
    """
    Deletes the specified QR code image file.
    """
    try:
        file_path.unlink(missing_ok=True)  # Python 3.8+ allows for missing_ok parameter
        logging.info(f"QR code {file_path.name} deleted")
    except FileNotFoundError:
        logging.error(f"QR code {file_path.name} not found for deletion")
        raise

def create_directory(directory_path: Path):
    """
    Creates a directory if it doesn't already exist.
    """
    logging.debug('Attempting to create directory')
    try:
        directory_path.mkdir(parents=True, exist_ok=True)
        logging.info(f"Directory created or already exists: {directory_path}")
    except PermissionError as e:
        logging.error(f"Permission denied: {directory_path}: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error: {directory_path}: {e}")
        raise
