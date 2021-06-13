# SmartCryptoSearchInTrends
Search desired crypto symbols in tweeter trends, google searches' trends (https://trends.google.com/trends/?geo=US) and specific users' tweets. 
Since google search trends and tweeter results are all in text format,  we need to perform a text similarity function to make sure that such results including the crypto symbols that we predefined before. For such similarity issue, levenstein distance handled in fuzzywuzzy package was used. Similarity score is parametric hence can be changed by user.  

Just after search finish it sends an email to pre-defined mail to list.



##Since the app needs to connect tweeter and a mail account setup as well, you need to pass the credentials for such connections. So just after cloning the repo, one should create .env file under project folder and replace its own credentials as environment variables. Keys for env variables are like below:
* GMAIL_FROM_ADDRESS="xxxx@gmail.com"
* GMAIL_API_SECRET="xxxxxxxx"
* TWEETER_CONSUMER_KEY="xxxxxxxx"
* TWEETER_CONSUMER_SECRET="xxxxxxxx"
* TWEETER_ACCESS_TOKEN="xxxxxxxx"
* TWEETER_ACCESS_TOKEN_SECRET="xxxxxxxx"


