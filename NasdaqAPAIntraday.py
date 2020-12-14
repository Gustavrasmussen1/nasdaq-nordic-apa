# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:34:38 2020

@author: GURA
"""
import urllib
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt

today = dt.datetime.today().strftime('%Y-%m-%d')


# API ENDPOINT
url = "http://www.nasdaqomxnordic.com/webproxy/DataFeedProxy.aspx"

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36"


data = {}
data['FromDate'] = today
data['ToDate'] = today
data['SubSystem'] = "Prices"
data['Action'] = "GetTrades"
data['Exchange'] = "NMF"
data['ext_xslt'] = "/nordicV3/apa_tradelist.xsl"
data['ext_xslt_lang'] = "en"
data['ext_xslt_tableId'] = "apatradelisttable"
data['ext_xslt_notlabel'] = "fnm"
data['ext_xslt_hiddenattrs'] = "insname,mktid"
data['Instrument'] = "XOPV43385"
data['t.a'] = "32,24,5,1,2,18,27,19"
data['showall'] = "1"
# Change between ./intrady

data['app'] = "/nasdaq-apa/intraday"

data = urllib.parse.urlencode(data)
full_url = url + "?" + data
response = requests.get(full_url, headers = headers)


soup = BeautifulSoup(response.content,'xml')
raw_df = pd.read_html(soup.prettify())[0]