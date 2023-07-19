# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 14:13:26 2023

@author: pasharma
"""
import pandas as pd
from datetime import datetime
import csv
import pickle
import os

import lst_history1 as l

new_row_default={'time': '00:00', 'high':0.0, 'open':0.0,'close':0.0,'low':1000000.0}
stock_master = dict()

#data_default={ "is_in_trade" : False }
directory = l.data_directory

firstTradeAfterCandle = l.firstTradeAfterCandle

for stock in l.stockList:
    master = {'all_rows': pd.DataFrame(), \
              'new_row' : pd.DataFrame(new_row_default, index=[0]), \
                 'trans_data' : [], \
                 'trans_pkl_file' : 'transaction-' + stock['token'] + '-' + stock['stockName'] + '-' + l.dat + '.pkl', \
                 'histDataFile' : 'data-' + stock['token'] + '-' + stock['stockName'] + '-' + l.dat + '.pkl', \
                'finalFiveMinuteDataDoneFlag' : False, \
                 'oldDataLoadedFlag' : False, \
                 'localData' : { "is_in_trade" : False }, \
                     'stockDetail': stock
                 }
    
    stock_master[stock['token']] = master
    

def loadData(fileName, token):
      
    if os.path.isfile(directory + fileName):
        stock_master[token]['all_rows'] = pd.read_pickle(fileName)
    #dataLoad = True
    stock_master[token]['oldDataLoadedFlag'] = True


def getData(message):
    flag = False
    dttime_value = message['exchange_timestamp']
    token = message['token']
    
    '''for ii in stock_master:
        print(stock_master[ii]['histDataFile'])
        print(stock_master[ii]['new_row'])
        print(stock_master[ii]['stockName'])'''
    #currentStock = stock_master[str(token)]
    
    if stock_master[str(token)]['oldDataLoadedFlag'] ==False:
        #stock_master[str(token)]['all_rows'] = old_data_master
        
        stock_master[str(token)]['oldDataLoadedFlag'] = True
        #stock_master[str(token)]['all_rows']['EMA5'] = stock_master[str(token)]['all_rows']['close'].ewm(span= stock_master[str(token)]['stockDetail']['interval'] , adjust=False).mean()
        print(stock_master[str(token)]['stockDetail'])   
        print(stock_master[str(token)]['all_rows'])
        stock_master[str(token)]['finalFiveMinuteDataDoneFlag'] = True
        #loadData(currentStock['histDataFile'], token)
    
    
    dt_obj = datetime.fromtimestamp((dttime_value/1000))
    if token == 42697:
        print(dt_obj, token, stock_master[str(token)]['stockDetail']['stockName'],  message['last_traded_price']/100)
    time = dt_obj.time()
    
    '''if currentStock['new_row'].at[0, 'time'] == '00:00':
        #print("here")
        if time.minute % currentStock['stockDetail']['interval'] ==0:
            currentStock['new_row'].at[0, 'time'] = dt_obj  
            currentStock['new_row'].at[0, 'open'] = message['last_traded_price']/100
            currentStock['new_row'].at[0, 'high'] = message['last_traded_price']/100
            currentStock['new_row'].at[0, 'low'] = message['last_traded_price']/100
            currentStock['new_row'].at[0, 'close'] = message['last_traded_price']/100 
            currentStock['finalFiveMinuteDataDoneFlag'] = True'''
    
    if stock_master[str(token)]['new_row'].at[0, 'time'] == '00:00':
        stock_master[str(token)]['finalFiveMinuteDataDoneFlag'] = True
        stock_master[str(token)]['new_row'].at[0, 'time'] = dt_obj  
        stock_master[str(token)]['new_row'].at[0, 'open'] = message['last_traded_price']/100
        stock_master[str(token)]['new_row'].at[0, 'high'] = message['last_traded_price']/100
        stock_master[str(token)]['new_row'].at[0, 'low'] = message['last_traded_price']/100
        stock_master[str(token)]['new_row'].at[0, 'close'] = message['last_traded_price']/100 
        print('exit')
    elif (stock_master[str(token)]['finalFiveMinuteDataDoneFlag'] ==False and time.minute % stock_master[str(token)]['stockDetail']['interval'] ==0):  
        #print('its here')
        stock_master[str(token)]['new_row'].at[0, 'close'] = message['last_traded_price']/100  
        
        if stock_master[str(token)]['finalFiveMinuteDataDoneFlag'] == False:        
            #print("time ==1 ###############################################3")
            stock_master[str(token)]['new_row'].at[0, 'time'] = dt_obj   
            addDF(stock_master[str(token)]['new_row'], token)
            stock_master[str(token)]['finalFiveMinuteDataDoneFlag'] = True
                
        stock_master[str(token)]['new_row'].at[0, 'open'] = message['last_traded_price']/100
        stock_master[str(token)]['new_row'].at[0, 'high'] = message['last_traded_price']/100
        stock_master[str(token)]['new_row'].at[0, 'low'] = message['last_traded_price']/100
        stock_master[str(token)]['new_row'].at[0, 'close'] = message['last_traded_price']/100    
        
        flag = checkAlert(stock_master[str(token)]['new_row'], token, message['last_traded_price']/100, message['exchange_timestamp'])
    elif (stock_master[str(token)]['finalFiveMinuteDataDoneFlag'] ==True and time.minute % stock_master[str(token)]['stockDetail']['interval'] ==0):
        #print('Data Done')
        stock_master[str(token)]['new_row'].at[0, 'high'] = max(stock_master[str(token)]['new_row'].at[0, 'high'], (message['last_traded_price']/100))    
        stock_master[str(token)]['new_row'].at[0, 'low'] = min(stock_master[str(token)]['new_row'].at[0, 'low'], (message['last_traded_price']/100))
        #print(currentStock['new_row'])
        flag = checkAlert(stock_master[str(token)]['new_row'], token, message['last_traded_price']/100, message['exchange_timestamp'])

    else:     
        stock_master[str(token)]['finalFiveMinuteDataDoneFlag'] = False
        #print('other')
        
        stock_master[str(token)]['new_row'].at[0, 'high'] = max(stock_master[str(token)]['new_row'].at[0, 'high'], (message['last_traded_price']/100))    
        stock_master[str(token)]['new_row'].at[0, 'low'] = min(stock_master[str(token)]['new_row'].at[0, 'low'], (message['last_traded_price']/100))
        #print(currentStock['new_row'])
        flag = checkAlert(stock_master[str(token)]['new_row'], token, message['last_traded_price']/100, message['exchange_timestamp'])
    
    return flag

    
def addDF(row, token):
    fileName = stock_master[str(token)]['histDataFile']
        
    stock_master[str(token)]['all_rows'] = stock_master[str(token)]['all_rows'].append(row)
    
    stock_master[str(token)]['all_rows']['EMA5'] = stock_master[str(token)]['all_rows']['close'].ewm(span= stock_master[str(token)]['stockDetail']['interval'] , adjust=False).mean()
    
    stock_master[str(token)]['all_rows'].to_pickle(directory + fileName)
    print('new DF #############################################', token, stock_master[str(token)]['stockDetail']['stockName'])
    print(stock_master[str(token)]['all_rows'])
    
    
def checkAlert(newRow, token, tradePrice, dtTime): 
    #print(len(stock_master[str(token)]['all_rows']))
    flag = False
    if len(stock_master[str(token)]['all_rows']) > firstTradeAfterCandle:
        EMA5StrategyMohit(newRow, l.dat, token, tradePrice, dtTime)
    
    return flag


def EMA5StrategyMohit(newRow, date, token, tradePrice, dtTime):
    #global data
    #global transData
    #u.printP(True,'Checking 5EMA for ########' + ticker + '###### for date:' + date + ' with target:' + targetRatio)
    #is_in_trade = False
    flag = False
    
    
    #print("check started")
    #print(newRow)
    currentCandle = newRow.iloc[0]
    #print("######################")
    #print(token)
    #print(df)
    
    #print(len(df))
    df = stock_master[str(token)]['all_rows']
    #print('heheheheh')
    data = stock_master[str(token)]['localData']
    #print('heheheheh5678')
    previousCandle = df.iloc[len(df)-1]
    #print('here ######################')
    '''print("got candles")
    print(firstCandle)
    print("#############3")
    print(previousCandle)
    print("##########3")
    print(currentCandle)'''
    if not data['is_in_trade']:
        #print('dataa#####################')            
        data = EMA5StrategyMohitBuyTrade(previousCandle, currentCandle, date, token, tradePrice, dtTime)            
        if data['is_in_trade']:
            print(data)
        
    elif data['is_in_trade']:
        data['diff'] += 1
        #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        #print("trade active", token, stock_master[str(token)]['stockName'], data['type'])
        if data['type'] == "SELL":
            #print("Checking for Trade")
            #print(data['targetPrice'])
            #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
            #print("trade active", token, stock_master[str(token)]['stockName'])
            if data['targetPrice'] > tradePrice: #currentCandle['low']:
                #and \
                #data['targetPrice'] <= currentCandle['high']: 
                    
                print('Buy Share with Target Achieved, Square off @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                #print("Target Achieved")
                print(currentCandle)
                data['soldPrice'] = tradePrice #data['targetPrice']
                #is_in_trade = False
                #data['is_in_trade'] = False
                data['profit'] = 'Yes'
                data['amount'] = data['entryPrice'] - tradePrice #data['targetPrice']
                data['finalCandle'] = currentCandle
                data['finalSoldTime'] = dtTime
                print(stock_master[str(token)]['stockDetail']['stockName'], token, tradePrice)
                stock_master[str(token)]['trans_data'].append(data)
                writeToPKL(stock_master[str(token)]['trans_data'], token)
                #data={}
                data={ "is_in_trade" : False }
                stock_master[str(token)]['localData'] = data
                flag = True
                #if not data['is_in_trade']:                        
                #    data = EMA5StrategyMohitBuyTrade(previousCandle, currentCandle, targetRatio, date, ticker)            
                
            elif data['stopLossPrice'] < tradePrice: #currentCandle['high']:  
                #data['stopLossPrice'] >= currentCandle['low'] and \
                    
                print('Buy Share with SL, Square off @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                #print("SL Hit")
                print(currentCandle)
                data['soldPrice'] = tradePrice # data['stopLossPrice']
                #is_in_trade = False
                #data['is_in_trade'] = False
                data['profit'] = 'No'
                data['amount'] = -(tradePrice - data['entryPrice']) #-(data['stopLossPrice'] - data['entryPrice'])
                data['finalCandle'] = currentCandle
                data['finalSoldTime'] = dtTime
                print(stock_master[str(token)]['stockDetail']['stockName'], token, tradePrice)
                stock_master[str(token)]['trans_data'].append(data)
                writeToPKL(stock_master[str(token)]['trans_data'], token)
                #data={}
                data={ "is_in_trade" : False }
                stock_master[str(token)]['localData'] = data
                flag = True
                #if not data['is_in_trade']:                        
                #    data = EMA5StrategyMohitBuyTrade(previousCandle, currentCandle, targetRatio, date, ticker)            
                
            '''else:
                print('here')
                print(currentCandle)
                target_limit = (data['stopLossGap'] * targetRatio) * 0.6
                print("Target Limit :" + str(target_limit))
                
                if data['entryPrice'] - target_limit >= currentCandle['low'] and \
                data['entryPrice'] - target_limit <= currentCandle['high']:
                    
                 data['targetPrice'] -= data['stopLossGap']
                 data['stopLossPrice'] -= data['stopLossGap']
                 data['targetSwitched'] = 'Yes'  '''
                
        elif data['type'] == "BUY":
            
            #print("Checking for Trade")
            #print(data['targetPrice'])
            
            if data['targetPrice'] < tradePrice: #currentCandle['high']: 
                #data['targetPrice'] >= currentCandle['low'] and \
                    
                print('Sold Share with Target Achieved, Square off @@@@@@@@@@@@@@@@@@@@@@@@@')
                #print("Target Achieved")
                print(currentCandle)
                data['soldPrice'] = tradePrice #data['targetPrice']
                #is_in_trade = False
                #data['is_in_trade'] = False
                data['profit'] = 'Yes'
                data['amount'] =  tradePrice - data['entryPrice']#data['targetPrice'] - data['entryPrice']
                data['finalCandle'] = currentCandle
                data['finalSoldTime'] = dtTime
                print(stock_master[str(token)]['stockDetail']['stockName'], token, tradePrice)
                stock_master[str(token)]['trans_data'].append(data)
                writeToPKL(stock_master[str(token)]['trans_data'], token)
                #data={}
                data={ "is_in_trade" : False }
                stock_master[str(token)]['localData'] = data
                flag = True
                #if not data['is_in_trade']:
                    
                #    data = EMA5StrategyMohitBuyTrade(previousCandle, currentCandle, targetRatio, date, ticker)            
            elif data['stopLossPrice'] > tradePrice: #currentCandle['low']:
                #and \
                #data['stopLossPrice'] <= currentCandle['high']:  
                    
                print('Sold Share with SL, Square off @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
                #print("SL Hit")
                print(currentCandle)
                data['soldPrice'] = tradePrice ##data['stopLossPrice']
                #is_in_trade = False
                #data['is_in_trade'] = False
                data['profit'] = 'No'
                data['amount'] = -(data['entryPrice'] - tradePrice)#data['stopLossPrice'])
                data['finalCandle'] = currentCandle
                data['finalSoldTime'] = dtTime
                print(stock_master[str(token)]['stockDetail']['stockName'], token, tradePrice)
                stock_master[str(token)]['trans_data'].append(data)
                writeToPKL(stock_master[str(token)]['trans_data'], token)
                #data={}
                data={ "is_in_trade" : False }
                stock_master[str(token)]['localData'] = data
                flag = True
                #if not data['is_in_trade']:
                    
                #    data = EMA5StrategyMohitBuyTrade(previousCandle, currentCandle, targetRatio, date, ticker)            
            
            '''else:
                print('here')
                print(currentCandle)
                target_limit = (data['stopLossGap'] * targetRatio) * 0.6
                print("Target Limit :" + str(target_limit))
                
                if data['entryPrice'] + target_limit >= currentCandle['low'] and \
                data['entryPrice'] + target_limit <= currentCandle['high']:
                 data['targetPrice'] += data['stopLossGap']
                 data['stopLossPrice'] += data['stopLossGap']
                 data['targetSwitched'] = 'Yes' '''
    else:
        print("NA")
                                    
            
    #print("finished")
    if flag == True:
        print("########################################################")
        print("########################################################")
        print("########################################################")
        print("########################################################")
        print("########################################################")
        print("########################################################")
        print("########################################################")
        print("########################################################")
        print("########################################################")
        print("########################################################")
        
    return flag

'''def writeData(finalData):
    data_file = open('reports/result_adjust0-5-adani.csv', 'w', newline='')
    csv_writer = csv.writer(data_file)
    
    
    #print(data)
    
    header = finalData.keys()
    csv_writer.writerow(header)
    
    csv_writer.writerow(finalData.values())
    
    data_file.close() '''
    
def writeToPKL(finalData, token):
    fileName = stock_master[str(token)]['trans_pkl_file']
    with open(l.transact_directory + fileName, 'wb+') as fp:
        pickle.dump(finalData,fp)


def EMA5StrategyMohitBuyTrade(previousCandle, currentCandle, date, token, tradePrice, dtTime):
    data={ "is_in_trade" : False }
    #print('herere')
    #print(previousCandle)
    #print(currentCandle)
    #print("#######################3")
    #print(currentCandle['low'])
    #print(previousCandle['low'])
    #print(previousCandle['EMA5'])
    #print(previousCandle['low'] > previousCandle['EMA5'])
    
    #print((currentCandle['low'] < previousCandle['low']))
    #print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    
    if previousCandle['low'] > previousCandle['EMA5'] and \
        tradePrice < previousCandle['low']: 
             #currentCandle['low'] < previousCandle['low']: 
                #and \
                #    currentCandle['low'] < previousCandle['EMA5']:
        if stock_master[str(token)]['stockDetail']['SELL'] == True:
           
            print("Trade Started : Sold###################################33")
            #is_in_trade = True
            entry_price = currentCandle['low']        
            stopLossGap = round((previousCandle['high'] - entry_price), 2)
            target_price = entry_price - (stopLossGap * stock_master[str(token)]['stockDetail']['SELL_Target'])        
            stop_loss_price = entry_price + stopLossGap
            
            data['targetRatio'] = stock_master[str(token)]['stockDetail']['SELL_Target'] #targetRatio        
            data['date'] = date
            data['stock'] = stock_master[str(token)]['stockDetail']['stockName']
            data['entryPrice'] = entry_price
            data['stopLossPrice'] = stop_loss_price
            data['stopLossGap'] = stopLossGap
            data['targetSwitched'] = 'No'
            data['targetPrice'] = target_price
            data['pCandle'] = previousCandle
            data['cCandle'] = currentCandle
            data['datetime'] = dtTime#currentCandle['time']
            data['type'] = "SELL"
            data['is_in_trade'] = True
            data['diff'] = 0
            stock_master[str(token)]['localData'] = data
            print(f"Short Sell at {entry_price} on {dtTime}")
            #print(data)
    elif previousCandle['high'] < previousCandle['EMA5'] and \
        tradePrice > previousCandle['high']:
        #currentCandle['high'] > previousCandle['high']:
            #and \
            #currentCandle['high'] > previousCandle['EMA5']:
        if stock_master[str(token)]['stockDetail']['BUY'] == True:
            print("Trade Started : Bought ######################################33")
            #is_in_trade = True
            entry_price = currentCandle['high']
            stopLossGap =  round((entry_price - previousCandle['low']),2)
            
            target_price = entry_price + (stopLossGap * stock_master[str(token)]['stockDetail']['BUY_Target'])
            stop_loss_price = entry_price - stopLossGap
            
            data['targetRatio'] = stock_master[str(token)]['stockDetail']['BUY_Target'] #targetRatio
            data['date'] = date
            data['stock'] = stock_master[str(token)]['stockDetail']['stockName']
            data['entryPrice'] = entry_price
            data['stopLossPrice'] = stop_loss_price
            data['stopLossGap'] = stopLossGap
            data['targetSwitched'] = 'No'
            data['targetPrice'] = target_price
            data['pCandle'] = previousCandle
            data['cCandle'] = currentCandle
            data['datetime'] = dtTime#currentCandle['time']
            data['type'] = "BUY"
            data['is_in_trade'] = True
            data['diff'] = 0
            stock_master[str(token)]['localData'] = data
            print(f"BUY at {entry_price} on {dtTime}")
            #print(data)
        
    return data
  
    
    
    
    