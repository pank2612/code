# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 14:33:32 2023

@author: pasharma
"""
from datetime import date

tOPT="C36OQQ2D4B4YPZJY3Q4XQY2BOM"
clientId="N51778255"
clientKey="2IZKKCeA"
clientPin = "2409"

###Shoonya
vendorCode = "FA139088_U"
IMEI = "abc1234"
apiKey = "eaa510b962dbcf7aa74b963b19b75136"

'''token_list = [{"exchangeType": 2, "tokens": ["42697", "51097"]}, {"exchangeType": 1, "tokens": ["10637", "19913"]}]
stockName = {"42697" : "NIFTYFUT", \
             "10637" : "OLECTRA", \
                 "19913":"DMART", \
                     "51097" : "FINNIFTY"} '''
    
stockList = [
    {"token": "42697", "stockName" : "NIFTYFUT", "exchange" : 2, "exchangeInString" : "NFO", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": False, "SELL_Target" : 2, "BUY_Target" : 2},
    {"token": "42692", "stockName" : "BANKNIFTYFUT", "exchange" : 2, "exchangeInString" : "NFO", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": False, "SELL_Target" : 2, "BUY_Target" : 2},
    {"token": "51097", "stockName" : "FINNIFTY", "exchange" : 2, "exchangeInString" : "NFO", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": False, "SELL_Target" : 2, "BUY_Target" : 2},
    {"token": "10637", "stockName" : "OLECTRA", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 4, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 4, "BUY_Target" : 4},
    {"token": "19913", "stockName" : "DMART", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 5, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 5, "BUY_Target" : 5},
    {"token": "25", "stockName" : "ADANIENT", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 7, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 7, "BUY_Target" : 7},    
    {"token": "17869", "stockName" : "JSWENERGY", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": False, "SELL_Target" : 2, "BUY_Target" : 2},
    {"token": "236", "stockName" : "ASIANPAINT", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 4, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "3456", "stockName" : "TATAMOTORS", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "2885", "stockName" : "RELIANCE", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "12487", "stockName" : "CYIENT", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "8479", "stockName" : "TVSMOTOR", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "9683", "stockName" : "KPITTECH", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "20242", "stockName" : "OBEROIRLTY", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "3918", "stockName" : "NATCOPHARM", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "7929", "stockName" : "ZYDUSLIFE", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "1186", "stockName" : "GLAND", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "15083", "stockName" : "ADANIPORTS", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "3563", "stockName" : "ADANIGREEN", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "22", "stockName" : "ACC", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "14894", "stockName" : "CentralBank", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "1270", "stockName" : "AMBUJACEMENT", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "10794", "stockName" : "CANARABANK", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "4668", "stockName" : "BANKBARODA", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "2181", "stockName" : "BOSCHLTD", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "3506", "stockName" : "TITAN", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "2535", "stockName" : "PGHH", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "18921", "stockName" : "VBL", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "685", "stockName" : "CHOLAFIN", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "1624", "stockName" : "IOC", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "2031", "stockName" : "M&M", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "23650", "stockName" : "MUTHOOTFIN", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "21808", "stockName" : "SBILIFE", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "3063", "stockName" : "VEDL", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "3518", "stockName" : "TORNTPHARM", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "694", "stockName" : "CIPLA", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "305", "stockName" : "BAJAJHLDNG", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "3045", "stockName" : "SBIN", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    {"token": "13", "stockName" : "ABB", "exchange" : 1, "exchangeInString" : "NSE", "enabled" : True, "target" : 2, "interval" : 5, "intervalInString" : "FIVE_MINUTE", "SELL" : True, "BUY": True, "SELL_Target" : 2, "BUY_Target" : 2}, 
    
            ]

finalStockList = []
tokenlst1=[]
tokenlst2=[]

for stock in stockList:    
    if stock['exchange'] == 1 and stock['enabled'] == True:
        tokenlst1.append(stock['token'])
    elif stock['exchange']==2  and stock['enabled'] == True:
        tokenlst2.append(stock['token'])

finalStockList.append({"exchangeType": 2, "tokens": tokenlst2})
finalStockList.append({"exchangeType": 1, "tokens": tokenlst1})

data_directory = "./data1/"
transact_directory = "./Transact1/"

dat = date.today().strftime("%Y%m%d")

firstTradeAfterCandle =6

