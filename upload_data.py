import os
import sqlalchemy
import pandas as pd
from dotenv import load_dotenv

# Load environment data
dirname = os.path.dirname(__file__)
dotenv_path = os.path.join(dirname, ".env")
load_dotenv(dotenv_path)

DATASETS_PATH = os.environ.get("DATASETS_PATH")
DATABASE_NAME = os.environ.get("DATABASE_NAME")
USER          = os.environ.get("USER")
PASSWORD      = os.environ.get("PASSWORD")
HOST          = os.environ.get("HOST")
PORT          = os.environ.get("PORT")

# Load datasets
datasets_path = os.path.join(dirname, DATASETS_PATH)
datasets_collection = {}

# Iterate over datasets folder
for file in os.listdir(datasets_path):
    filename, file_extension = os.path.splitext(file)
    if file_extension == ".csv":
        # Load dataset into dataframe
        file_path = os.path.join(datasets_path, file)
        data = pd.read_csv(file_path)
        datasets_collection[filename] = data
        print(f"{filename} loaded as dataframe in RAM")

# Upload data using SQLAlchemy
try:
    db_connection_string = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE_NAME}"
    engine = sqlalchemy.create_engine(db_connection_string, echo=True)
    for dataset_name, data in datasets_collection.items():
        data.to_sql(dataset_name, engine, if_exists="replace", index=False)
except Exception as e:
    print(f"[ERROR] During connection to database cought following error: {e}.")