from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "AI Civic Hazard Detection & Safety Assistant"
    upload_dir: str = "storage/uploads"
    max_upload_size_mb: int = 10

settings = Settings()
