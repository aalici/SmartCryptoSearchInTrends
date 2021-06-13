# SmartCryptoSearchInTrends
Search desired crypto symbols in tweeter trends, google searches' trends (https://trends.google.com/trends/?geo=US) and specific users' tweets. 
Since google search trends and tweeter results are all in text format,  we need to perform a text similarity function to make sure that such results including the crypto symbols that we predefined before. For such similarity issue, levenstein distance handled in fuzzywuzzy package was used. Similarity score is parametric hence can be changed by user.  

Just after search finish it sends an email to pre-defined mail to list. Mail structure is like below:

![SmartCryptoSearchInTrends_Results](https://user-images.githubusercontent.com/32384466/121808751-b1fde580-cc62-11eb-9e12-9d5b49e0d849.PNG)


## You need to make some updates once cloning the repo like below:

* Since the app needs to connect tweeter and a mail account setup as well, you need to pass the credentials for such connections. So just after cloning the repo, one should create **.env** file under project folder and replace its own credentials as environment variables. Keys for env variables are like below:
  * GMAIL_FROM_ADDRESS="xxxx@gmail.com"
  * GMAIL_API_SECRET="xxxxxxxx"
  * TWEETER_CONSUMER_KEY="xxxxxxxx"
  * TWEETER_CONSUMER_SECRET="xxxxxxxx"
  * TWEETER_ACCESS_TOKEN="xxxxxxxx"
  * TWEETER_ACCESS_TOKEN_SECRET="xxxxxxxx"

* Need to change **project_constants.py** for setting the tweeter users you want to follow and mail_to list. 


## Items in progress (Since the development is in progress state, all dev code is in a private repo):
* Fetching real-time prices from binance API and perform a time-series prediction model to guess the direction of price movement.
* Coins having relatively small market cap has a good potential to steep price increase like Doge, Shiba etc. CoinMarketCap API provides the ranking of each coin in real-time. Following the ranking of each coin in crypto currency domain (currently there are thousands of coins available) and detecting the immediate market cap change might be a good indicator of a potentially new "hero" coin. Launching such early-detection logic is also under development stage for now.   

