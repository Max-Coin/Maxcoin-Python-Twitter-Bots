# Python Script Created By Oliver Morris
# Python Script Is used on GetMaxcoinPrice Twitter Account

#!/usr/bin/env python
# encoding=utf8
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')

from twython import Twython, TwythonError

## Setting these as variables will make them easier for future edits
app_key =  ''
app_secret = ''
oauth_token = ''
oauth_token_secret = ''

## Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break


import json
from coinmarketcap import Market
import threading

coinmarketcap = Market()


def run_total_id():
    threading.Timer(1200, run_total_id).start()
    s = coinmarketcap.ticker('maxcoin/?convert=GBP&limit=10')
    
    n = coinmarketcap.ticker('maxcoin/?convert=RUB')

    l = coinmarketcap.ticker('maxcoin/?convert=CNY')

#    s = json.loads(s)
    total_id = ('Maxcoin Price ' + '\n' + '@getmaxcoin')

#    price_gbp = ('PGBP: ' + '£' + s[0]['price_gbp'])

    price_rub = ('RUB: ' + n[0]['price_rub'])

    price_cny = ('CNY: ' + l[0]['price_cny'])

    rank = ('Rank: ' + s[0]['rank'])

    price_usd = ('USD: ' + s[0]['price_usd'])

    price_btc = ('BTC: ' + s[0]['price_btc'])

    txt1 = (total_id + str ('\n' + '\n' + 'Price: ' + '\n' + price_usd + '\n' + price_btc + '\n' + price_rub + '\n' + price_cny + '\n' + '\n' + 'MaxcoinProject.org' +  '\n' + '\n' + rank))

   # photo = open('/var/www/apistuffwithtux/maxcoincode/Maxcoin.jpg')
  #  response = twitter.upload_media(media=photo)
    try:
        s = twitter.update_status(status=txt1)
    except TwythonError, e:
       if e.error_code == 403:
	   pass
    print txt1    



run_total_id()



