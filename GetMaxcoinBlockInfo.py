# Python Script Created By Oliver Morris
# Python Script Is used on GetMaxcoinBlockInfo Twitter Account

#!/usr/bin/env python
import sys
import time
reload(sys)
sys.setdefaultencoding('utf8')


import urllib2
import json

from twython import Twython, TwythonError

## Setting these as variables will make them easier for future edits
app_key =  ''
app_secret = ''
oauth_token = ''
oauth_token_secret = ''

## Prepare your twitter, you will need it for everything
twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
#The above should just be a single line, without the break
 


import urllib2
import json
import threading


def run_total_id():
    threading.Timer(1200, run_total_id).start()

    total_id = ('Maxcoin Block Info ' + '@getmaxcoin ' )

    url = urllib2.urlopen('http://api.maxcoinhub.io/Blockchain/GetBlockCount')

    url = url.read()

    j = json.loads(url)

    s = j['result']

    new = str(s)

    newurl = urllib2.urlopen('http://api.maxcoinhub.io/Blockchain/GetMiningInfo')

    newurl = newurl.read()

    j1 = json.loads(newurl)

    hello = j1['result']['difficulty']

    new1 = str(hello)

    hello1 = j1['result']['networkhashps']

    new2 = str(hello1)

    newhello = j1['result']['createdOn']

    newblock = str(newhello)

    blockapi = urllib2.urlopen('http://api.maxcoinhub.io/Blockchain/GetBlockHash/' + new)

    blockapi = blockapi.read()

    gettingjson = json.loads(blockapi)

    results = gettingjson['result']

    newcode1 = str(results)

    blockcode = urllib2.urlopen('http://api.maxcoinhub.io/Blockchain/GetBlock/' + newcode1)

    blockcode = blockcode.read()

    blockjson = json.loads(blockcode)

    blockresults = blockjson['result']['merkleRoot']

    blocktxt = str(blockresults)

    blocks = (total_id + '\n' + 'Blocks: ' + new + '\n' + 'Block Hash: ' + newcode1 + '\n' + 'Merkle Root: ' + blocktxt + '\n' + 'Difficulty: ' + new1 + '\n' + 'Block Created On: ' + newblock)

    txt1 = str(blocks)

    try:
        s = twitter.update_status(status=blocks)
    except TwythonError, e:
       if e.error_code == 403:
           pass
    print blocks



run_total_id()


