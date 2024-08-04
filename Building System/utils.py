import re 
from datetime import datetime 

def extract_email(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\[a-zA-Z]{2,}'
    emails = re.findall(email_pattern)
    return emails 


def get_status_label(posted_date):
    days_since_posted = (datetime.now() - posted_date).days 
    if days_since_posted > 14:
        return "Expired"
    elif 7 < days_since_posted <= 14:
        return "Active"
    
    elif days_since_posted <= 7:
        return "Updated"
    return "Unknown"