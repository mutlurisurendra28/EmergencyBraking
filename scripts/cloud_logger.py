import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime, timedelta
import os

# Get absolute path of current file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build path to firebase key
cred_path = os.path.join(BASE_DIR, "firebase_key.json")

# Initialize Firebase
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()


def log_event(object_name, distance, risk):

    # Convert UTC to IST
    ist_time = datetime.utcnow() + timedelta(hours=5, minutes=30)

    data = {
        "object": object_name,
        "distance": distance,
        "risk": risk,
        "time": ist_time
    }

    db.collection("braking_events").add(data)