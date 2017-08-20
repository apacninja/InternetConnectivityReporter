import requests
import logging
import time

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO, filename='CrestwoodMediacom.log')

while True:
    time.sleep(60)

    try:
        conn = requests.get('http://google.com')
        # print conn.status_code
        logging.info('Internet Connected: ' + str(conn.status_code))
    except requests.exceptions.ConnectionError as e:
        logging.warning('No internet connection')
    except Exception as e:
        logging.error('Exception Occurred: ' + str(e))