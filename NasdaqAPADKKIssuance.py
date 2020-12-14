# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 10:36:02 2020

@author: GURA
"""

import urllib
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

today = dt.datetime.today().strftime('%Y-%m-%d')


# API ENDPOINT
url = "http://www.nasdaqomxnordic.com/webproxy/DataFeedProxy.aspx"

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36"


data = {}
data['FromDate'] = "2020-09-01"
data['ToDate'] = today
data['SubSystem'] = "Prices"
data['Action'] = "GetTrades"
data['Exchange'] = "NMF"
data['ext_xslt'] = "/nordicV3/t_table_simple.xsl"
data['ext_xslt_lang'] = "en"
data['ext_xslt_tableId'] = "danish-bond-trade-history-table"
data['t__a'] = "1,2,4,6,7,8,18"
data['Instrument'] = "XCSE0:5NDASDRO50" # Need to change this param to change bonds
data['showall'] = "1"
data['app'] = "/bonds/denmark/microsite"

data = urllib.parse.urlencode(data)
full_url = url + "?" + data
response = requests.get(full_url, headers = headers)


soup = BeautifulSoup(response.content,'xml')
raw_df = pd.read_html(soup.prettify())[0]

transactions = ["OTC-Primary Transaction","OTC-Loan Payment"]
df = raw_df.loc[raw_df['Trade type'].isin(transactions)]

df.set_index('Time', inplace=True)

df = df[['Volume','Trade type']]