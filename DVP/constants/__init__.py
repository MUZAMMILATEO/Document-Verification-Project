import os
from datetime import date

DATABASE_NAME = "US_VISA_DATASET.db"

COLLECTION_NAME = "visa_data"

MONGIDB_URL_KEY = "mongodb+srv://khanm:khanm@cluster0.zizpbkz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

PIPELINE_NAME:str = "usvisa"

ARTIFACT_DIR:str = "artifact"

MODEL_FILE_NAME = "model.pkl"