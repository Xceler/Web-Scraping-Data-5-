import time 
from db import get_mongo_db
from driver import create_chrome_driver 
from scraper import load_all_results 
from config import connected_string, db_name, collection_name 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 


def update_mongodb():
    collection = get_mongo_db()
    driver = create_chrome_driver()
    try:
        url = "https://www.linkedin.com/jobs/search/?currentJobId=3983808475&distance=25.0&geoId=104305776&keywords=food%20%26%20beverage&origin=HISTORY"
        driver.get(url)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (
                    By.CLASS_NAME, 'results-context-header__job-count'
                )
            )
        )
        all_job_data = load_all_results(driver)
        for job in all_job_data:
            try:
                existing_job = collection.find_one({'job_link' : job['job_link']})


                if not existing_job:
                    collection.insert_one(job)
                    print(f"Inserted New Job: {job['job_link']}")
                else:
                    collection.update_one(
                        {'job_link' : job['job_link']},
                        {'$set' : job}
                    )
                    print(f'Job Updated: {job["job_link"]}')
            
            except Exception as e:
                print(f"Error Occurring as {e}")
            
        print(f"{len(all_job_data)} jobs scraped and checked for duplicates")
    finally:
        driver.quit()

    

def main():
    try:
        print("Starting Jobs Scraping...")
        update_mongodb()
        print("Data Scraping And Updated Completed")

    
    except Exception as e:
        print(f"Error Occurring as {e}")
    
  

if __name__ == '__main__':
    main() 