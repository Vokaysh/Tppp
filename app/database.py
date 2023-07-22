```python
from firebase_admin import credentials, firestore, initialize_app
from app.config import get_settings

# Initialize Firestore DB
cred = credentials.Certificate(get_settings().firebase_key_path)
default_app = initialize_app(cred)
db = firestore.client()

def get_db():
    return db
```