#General imports
import pandas as pd
import os


#email sending
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#logging
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

#Google Trends & Tweeter  
from pytrends.request import TrendReq
import tweepy

#environment variables
from dotenv import load_dotenv
load_dotenv()

###########

def f_send_mail(mail_content=None, 
                mail_to=None,
                mail_subject=None):
    if mail_to is None:
        mail_to = 'ali.alici84@gmail.com'
        
    if mail_content is None:
        mail_content = 'Just try mail sending logic. No specific content is set.'    
        
    if mail_subject is None:
        mail_subject = 'Test Mail from App'    

    logger.info('Try to send email to {x}'.format(x=mail_to))
    #mail_content = '''Hello,
    #This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    #Thank You
    #'''
    
    #The mail addresses and password
    sender_address = 'cuneytsolmazto@gmail.com'
    sender_pass = os.environ.get('GMAIL_API_SECRET')
    receiver_address = mail_to
    
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = mail_subject   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    try:
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        logger.info('Mail Sent')
    except:
        logger.error('Sent mail has failed !!')
        session.quit()
        

        
###########

def get_tweet_trends_by_loc(v_api, v_loc):
    if v_loc == "TR":
        woeid = 23424969
    elif v_loc == "US":
        woeid = 23424977    

    # fetching the trends
    trends = v_api.trends_place(id = woeid)
    list_tmp = []
    for value in trends:
        for trend in value['trends']:
            list_tmp.append(trend['name'])  
            #print(trend['name'])

    return list_tmp


def tweet_analyze():
    # OAuth process, using the keys and tokens
    consumer_key = os.environ.get('TWEET_CONSUMER_KEY')
    consumer_secret = os.environ.get('TWEET_CONSUMER_SECRET')
    access_token = os.environ.get('TWEET_ACCESS_TOKEN')
    access_token_secret = os.environ.get('TWEET_ACCESS_TOKEN_SECRET')
    logger.info('Try to connect tweeter api')

    try:        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        logger.info('Successfully connected to tweeter api')
    except:
        logger.error('tweeter connection has failed !!')

    tweet_dict = {}
    tweet_dict.update({"TR TREND TOPICS": get_tweet_trends_by_loc(api, "TR")}) 
    tweet_dict.update({"US TREND TOPICS": get_tweet_trends_by_loc(api, "US")}) 
    return tweet_dict
                    
###########
                    





if __name__ == "__main__":
    v_dict = tweet_analyze()
    mail_body = ''
    for key in v_dict:
        mail_body = mail_body + 'For {country} trend topics: '.format(country=key) + '\n'  
        mail_body = mail_body + '\n'.join(v_dict.get(key)) + "\n############## \n\n" 
    f_send_mail(mail_content = mail_body)