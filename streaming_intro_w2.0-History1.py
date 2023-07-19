# -*- coding: utf-8 -*-
"""
Angel One - Streaming tick level data websocket2.0

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

from SmartApi.smartWebSocketV2 import SmartWebSocketV2
from SmartApi import SmartConnect
import os
import urllib
import json
from pyotp import TOTP
import numpy as np
from datetime import datetime, timedelta
import time
import pandas as pd


import lst_history1 as l
import SocketStrategy_History1 as ss


obj=SmartConnect(api_key=l.clientKey)
data = obj.generateSession(l.clientId,l.clientPin,TOTP(l.tOPT).now())
feed_token = obj.getfeedToken()

'''instrument_url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
response = urllib.request.urlopen(instrument_url)
instrument_list = json.loads(response.read())'''

sws = SmartWebSocketV2(data["data"]["jwtToken"], l.clientKey, l.clientId, feed_token)


correlation_id = "stream_1" #any string value which will help identify the specific streaming in case of concurrent streaming
action = 1 #1 subscribe, 0 unsubscribe
mode = 1 #1 for LTP, 2 for Quote and 3 for SnapQuote


#token_list = [{"exchangeType": 1, "tokens": ["99926009"]}]
# for NFO

#np.set_printoptions(legacy='1.13')
count =0
def on_data(wsapp, message):
    global count
    
    #print(message)
    flag = False
    if not "{}".format(message).startswith('b'):   
        flag = ss.getData(message)
     #   count += 1 
    if flag == True:
        sws.unsubscribe(correlation_id, mode, l.finalStockList)
    #if count >=2:
    #   sws.unsubscribe(correlation_id, mode, token_list)


def on_open(wsapp):
    print("on open")
    if action == 1:
        #print(l.finalStockList)
        sws.subscribe(correlation_id, mode, l.finalStockList)
    else:
        sws.unsubscribe(correlation_id, mode, l.finalStockList)


def on_error(wsapp, error):
    print(error)






# Assign the callbacks.
sws.on_open = on_open
sws.on_data = on_data
sws.on_error = on_error

sws.connect()



old_data_master = dict()

for stock in l.stockList:
    if stock['enabled'] == True:                
        old_data_master[stock['token']] = getOldData(obj, stock['exchangeInString'], stock['token'], stock['interval'], stock['intervalInString'])
    
    print(stock['token'], len(old_data_master[stock['token']]))
    #print(len(old_data_master[stock['token']]))



def getOldData(obj, exchange, token, interval, intervalInString):
    df = pd.DataFrame()
    totalDays = 3
    delta = timedelta(days=1)
    end = datetime.now()
    start = end + timedelta(days = -totalDays )
    #print(start)
    
    date = start
    while date<=end:
        print(date)    
        #print(end)            
        #try:              
        if date.strftime("%Y-%m-%d") != end.strftime("%Y-%m-%d"):
            #print('dont match')
            sdt = date.strftime("%Y-%m-%d")+ " 09:15"
            edt = date.strftime("%Y-%m-%d")+ " 15:30"
            
        else:
            #print('match')
            #### Get Hour and Min
            finalDtTime = end + timedelta(minutes= (interval- (end.time().minute % interval)) )    
            lastDtHour = finalDtTime.hour
            lastDtMin = finalDtTime.minute
            #print(lastDtHour)
            #print(lastDtMin)
            #print(finalDtTime)
            ######################
            sdt = date.strftime("%Y-%m-%d")+ " 09:15"
            edt = date.strftime("%Y-%m-%d")+ " " + str(lastDtHour) + ":" + str(lastDtMin)
            
        
        df = df.append(hist_data_intraday(obj, exchange, sdt, edt, intervalInString, token), ignore_index = True)
        
        time.sleep(1/8)
            
        #except:
        #    print("Error : ", token,date)
        date+=delta
    return df
        
def hist_data_intraday(obj, exchange, sdt, edt, interval, token):
    
    params = {
             "exchange": exchange,
             "symboltoken": token,
             "interval": interval,
             "fromdate": sdt,
             "todate": edt
             }
    #print(params)
    hist_data = obj.getCandleData(params)
    #print("###################")
    #print(hist_data["data"])
    #print(type(hist_data["data"]))
    df1 = pd.DataFrame(hist_data["data"],
                           columns = ["time","open","high","low","close","volume"])
    df_data = df1[["time","open","high","low","close"]].copy()
    #print(df_data)
    return df_data

