import os
# # # # # # # # # # # # # # # # # # # #
try:
    import threading
except:
    os.system("pip install threading")
# # # # # # # # # # # # # # # # # # # #
try:
    import ccxt
except:
    os.system("pip install ccxt")
# # # # # # # # # # # # # # # # # # # #
try:
    import pandas as pd
except:
    os.system("pip install pandas")
# # # # # # # # # # # # # # # # # # # #
try:
    import time
except:
    os.system("pip install time")
# # # # # # # # # # # # # # # # # # # #
try:
    import pandas_ta as ta
except:
    os.system("pip install pandas_ta")
# # # # # # # # # # # # # # # # # # # #
try:
    import logging
except:
    os.system("pip install logging")
# # # # # # # # # # # # # # # # # # # #
from datetime import datetime
logging.basicConfig(filename='log.txt', filemode='a', format='%(asctime)s : %(message)s', datefmt='%H:%M:%S')
# exchange = ccxt.coinex({
# "apiKey": "xxxx",
# "secret": "xxxx",
# 'options': {
# 'defaultType': 'spot'
# },
# 'enableRateLimit': True
# })
exchange = ccxt.coinex()
# balance = exchange.fetch_balance()

# get numbers of candle
def get_ohlcv(symbol, interval = '15m', limit=101) -> pd.DataFrame:

    # headers
    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']



    # get candles from exchange
    bars = exchange.fetch_ohlcv(symbol, timeframe=interval, limit=limit)



    # convert list of list to pandas dataframe
    df = pd.DataFrame(bars, columns=columns)



    # convert millisecond to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')





    return df




print ('------------------------------Created By Mr.Reza-Skar------------------------------')
# playsound.playsound('1.wav')
symbol = input("Lotfan Joft Arze Morede Nazar Ra Dar Bazar Crypto Vared Konid : ")
# interval = (self.Timeframe.currentText())
print(f'{symbol}')
market = symbol
amount = 1.0
dataframe = get_ohlcv(symbol, interval = '15m', limit=101)


last_row = len(dataframe.index) - 1

# very simple trader bot!

print ('Bot Is Started!')

def Time():
    global current_time
    global minute
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        m = now.strftime("%M")
        minute = (int(m))
        time.sleep(1)




def main():
    price_aval = 0
    price_dovom = 0
    tafazole_aval_va_dovom = 0
    bought = 0
    Short = 0
    while True:
        if (minute % 15 == 0):
            while True:
                print (current_time)
                dataframe = get_ohlcv(symbol, limit=101)
                last_row = len(dataframe.index) - 2
                last_row_Display = len(dataframe.index) - 1

                # dataframe['signal'] = ta.supertrend(dataframe['high'], dataframe['low'],
                #                                    dataframe['close'], 8, 2)['SUPERTd_8_2.0']

                dataframe['MA100'] = ta.ma("sma", dataframe.close, length=100)
                dataframe['MA20'] = ta.ma("sma", dataframe.close, length=20)




                current_price = dataframe['close'][last_row]
                current_price_for_display = dataframe['close'][last_row_Display]



                MA100 = dataframe['MA100'][last_row]
                MA20 = dataframe['MA20'][last_row]
                # print(dataframe)

                print(f'{current_price_for_display}')

                if (bought == 0):
                    if ( MA100 < MA20 ):
                        print (f'Long signal for {symbol} on {current_price} at {current_time}')
                        # playsound.playsound('1.wav')
                        logging.warning(f'Long signal for {symbol} on {current_price} at {current_time}')
                        # exchange.create_market_buy_order(symbol, amount)
                        bought = 1
                        price_aval = current_price
                if (bought == 1):
                    if not ( MA100 < MA20 ):
                        print (f'Close Long position signal for {symbol} on {current_price} at {current_time}')
                        # playsound.playsound('1.wav')
                        logging.warning(f'Close Long position signal for {symbol} on {current_price} at {current_time}')
                        bought = 0
                        price_dovom = current_price
                        tafazole_aval_va_dovom = price_dovom-price_aval
                        logging.warning("Tafazol = {}".format(tafazole_aval_va_dovom))

                if (Short == 0):
                    if ( MA100 > MA20 ):
                        print (f'Short signal for {symbol} on {current_price} at {current_time}')
                        # playsound.playsound('1.wav')
                        logging.warning(f'Short signal for {symbol} on {current_price} at {current_time}')
                        Short = 1
                        price_sevom = current_price
                        # exchange.create_market_sell_order(symbol, amount)
                if (Short == 1):
                    if not ( MA100 > MA20 ):
                        print (f'Close Short position signal for {symbol} on {current_price} at {current_time}')
                        # playsound.playsound('1.wav')
                        logging.warning(f'Close Short position signal for {symbol} on {current_price} at {current_time}')
                        Short = 0
                        price_chaharom = current_price
                        tafazole_Chaharom_va_sevome = price_chaharom-price_sevom
                        logging.warning("Tafazol = {}".format(tafazole_Chaharom_va_sevome))
                time.sleep(900)


if __name__ == "__main__":
    thread_one = threading.Thread(target = Time)
    thread_two = threading.Thread(target = main)


    thread_one.start()
    thread_two.start()
