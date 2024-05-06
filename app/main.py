from fastapi import FastAPI
from app.config import QR_DIRECTORY
from app.routers import qr_code, oauth  # Ensure these imports match your project structure.
from app.services.qr_service import create_directory
from app.utils.common import setup_logging

# Set up logging based on the configuration file.
setup_logging()

# Ensure the directory for storing QR codes is created at startup if it doesn't exist.
create_directory(QR_DIRECTORY)

# Create an instance of FastAPI with specified metadata.
app = FastAPI(
    title="QR Code Manager",
    description="A FastAPI application for creating, listing, and deleting QR codes, with secure OAuth access.",
    version="0.0.1",
    redoc_url=None,  # Disable Redoc documentation
    contact={
        "name": "API Support",
        "url": "http://www.example.com/support",
        "email": "support@example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }
)

# Include routers for QR code management and OAuth authentication.
app.include_router(qr_code.router)  # Managing QR codes
app.include_router(oauth.router)  # OAuth authentication
