import os 
from dotenv import find_dotenv, load_dotenv 

load_dotenv(find_dotenv())

password = os.environ.get("mongo_pw")
if not password:
    raise ValueError("MongoDB Password Not Found")

connected_string = f"mongodb+srv://Webdata:{password}@datascraping.aqhdwnr.mongodb.net/"
db_name = 'job_data'
collection_name = 'jobs'

chrome_driver_path = "driver/chromedriver-win64/chromedriver-win64/chromedriver.exe"