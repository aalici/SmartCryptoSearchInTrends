# THIS SCRIPT IS AUTOGENERATED FROM scheduler.ipynb. 


# export
import schedule
import time
import random, string
import sys
sys.path.append('../src/')
import project_constants 
import GeneralFunctions as gf


import logging

# Gets or creates a logger
logger = logging.getLogger(__name__)  

# set log level
logger.setLevel(logging.INFO)

# define file handler and set formatter
file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)

print(','.join(project_constants.mail_to_list))




# export

def job():
    key = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    logger.info("Scheduler kick offs new job! key is {key}".format(key=key))
    mail_to = ','.join(project_constants.mail_to_list)
    gf.send_mails_with_matches(v_score_match = 75, 
                               v_mail_subject = "WEB Trend Analysis - SmartCryptoAnalysis with key:{key}".format(key=key),
                               v_to_address = mail_to )

#schedule.every(30).seconds.do(job)
schedule.every(15).minutes.do(job)
#schedule.every(240).minutes.do(job_load_cmc_data)
#schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)

while True:
    #logger.info("Scheduler works!")
    schedule.run_pending()
    time.sleep(10)
