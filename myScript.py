import requests
import logging
from datetime import datetime


logging.basicConfig(filename='app_uptime.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app_url ='https://www.amazon.com/'

def check_app_status(url):
    response = requests.get(url)
    status_code = response.status_code
    if response.status_code == 200:
        logging.info(f'Application is up. Status Code: {status_code}')
        return 'up', status_code
    else:
        logging.info(f'Application is down. Status Code: {status_code}')
        return 'down',status_code

def report(status, status_code):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if status == 'up':
        report_msg = (f"Application is up. Status code: {status_code}. Time:{now}")
    else:
        report_msg = (f"Application is down. Status Code:{status_code}. Time:{now}")

    print(report_msg)
    logging.info(report_msg)

if __name__ == "__main__":
    status, status_code = check_app_status(app_url)
    report(status, status_code)