# THIS SCRIPT IS AUTOGENERATED FROM scheduler.ipynb. 


# export
import schedule
import time
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




# export

def job():
    logger.info("Scheduler kick offs new job!")
    gf.send_mails_with_matches(85)
    print("I'm working...")

#schedule.every(10).seconds.do(job)
#schedule.every(15).minutes.do(job)
schedule.every().hour.do(job)
#schedule.every().day.at("10:30").do(job)
#schedule.every(5).to(10).minutes.do(job)
#schedule.every().monday.do(job)
#schedule.every().wednesday.at("13:15").do(job)
#schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(10)
