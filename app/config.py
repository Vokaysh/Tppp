```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    firebase_api_key: str
    firebase_auth_domain: str
    firebase_database_url: str
    firebase_storage_bucket: str

    class Config:
        env_file = ".env"

settings = Settings()
```