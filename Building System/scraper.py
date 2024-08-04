from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait 
from datetime import datetime 
from utils import extract_email, get_status_label 

def scrape_page(driver):
    job_cards = driver.find_elements(By.CLASS_NAME, 'base-search-card')
    page_data = []
    for job_card in job_cards:
        try:
            company = job_card.find_element(By.CLASS_NAME, 'base-search-card__subtitle').text 
            job_title =job_card.find_element(By.CLASS_NAME, 'base-search-card__title').text 
            location = job_card.find_element(By.CLASS_NAME, 'job-search-card__location').text 

            try:
                job_date_text = job_card.find_element(By.CLASS_NAME, 'job-search-card_listdate').text 
                job_date = datetime.strptime(job_date_text, "%d %b")
                job_date = job_date.replace(year = datetime.now().year)

            except:
                job_date = datetime.now() 
            
            anchor_tags = job_card.find_elements(By.TAG_NAME, 'a')
            job_link = anchor_tags[0].get_attribute('href') if anchor_tags else "N/A"
            emails = extract_email(job_link)
            email_str = ", ".join(emails) if emails else "Not Provided"


            job_data = {
                "company" : company,
                "job_title" : job_title,
                "location" : location,
                "job_date" : job_date.isoformat(),
                "job_link" : job_link,
                "email" : email_str,
                "status" : get_status_label(job_date)
            }
            page_data.append(job_data)
        except Exception as e:
            print(f"Error Occurring: {e}")
            continue 

    return page_data 


def load_all_results(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    all_job_data = []
    while True:
        try:
            page_data = scrape_page(driver)
            all_job_data.extend(page_data)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(5)


            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                print(f"End of Page Reached: {last_height}")
                break 
            last_height = new_height 
            print(f"Scrolled To : {new_height}")
        except Exception as e:
            print(f"Error Occurring as {e}")
            break 
    return all_job_data 


