import os

from os import system

x = 0

# # # # # # # # # # # # # # # # # # # # # # # # # #

while (x == 0):
    try:
        
        from colorama import Back, Fore, Style
        
        x = 1

    except:
        
        os.system("pip install colorama")
        
        from colorama import Back, Fore, Style  
        
# # # # # # # # # # # # # # # # # # # # # # # # # #

while (x == 1):
    try:
        
        import ccxt
        
        x = 0

    except:
        
        os.system("pip install ccxt")
        
        import ccxt
        
# # # # # # # # # # # # # # # # # # # # # # # # # #
  
while (x == 0):
    try:
        
        from selenium import webdriver

        from selenium.webdriver.common.keys import Keys

        from selenium.webdriver.common.by import By
        
        x = 1

    except:
        
        os.system("pip install selenium")
        
        from selenium import webdriver

        from selenium.webdriver.common.keys import Keys

        from selenium.webdriver.common.by import By

# # # # # # # # # # # # # # # # # # # # # # # # # #

while (x == 1):
    try:
        
        from PIL import Image

        x = 0

    except:
        
        os.system("pip install --upgrade pillow")
        
# # # # # # # # # # # # # # # # # # # # # # # # # #

while (x == 0):
    try:
        
        import telegram

        x = 1

    except:
        
        os.system("pip install python-telegram-bot")
        
# # # # # # # # # # # # # # # # # # # # # # # # # #

import time

import threading

token = input("Enter your BOT token (Agar Nemikhahid Az Tarige Bot Telegram Barayetan Log Ferestade Shavad Inja Chizi Naneveshte Va Faghat Enter Bezanid): ")

if (token != ""):
    
    user_id = input("Enter your Telegram ID (For Example This My Telegram ID : 281375287): ")

    bot=telegram.Bot(token=token)

while True:
    API_KEY = input("Enter your API Key: ")

    API_SECRET = input("Enter your API Secret: ")

    API_PASSWORD = input("Enter your API Password: ")

    size = float(input('Lotfan Megdare ' + Back.GREEN + "(( Lot ))" + Style.RESET_ALL + ' Morede Nazar Ra Vared Konid : '))

    symbol = str(input("Lotfan Arze Morede Nazar Ra Dar KuCoin Vared Konid ( Mesle : XBT (Bitcoin) , ETH (Etherium) , ... ) : ")) + "USDTM"

    levrage = str(input("Levrage Ra Vared Konid : "))

    size2 = float(size) * 2
    
    system("cls")
    
    lenkey = len(API_KEY) + 18
    lensecret = len(API_SECRET) + 21
    lenpassword = len(API_PASSWORD) + 23
    lenlot = len(str(size)) + 14
    lensymbol = len(symbol) + 17
    lenlevrage = len(levrage) + 18
    
    print(lenkey*"-" + "\n|  API KEY : " + Back.GREEN + f" {API_KEY} " + Style.RESET_ALL + "  |\n" + lenkey*"-" + "\n" + lensecret*"-" + "\n|  API SECRET : " + Back.GREEN + f" {API_SECRET} " + Style.RESET_ALL +  "  |\n" + lensecret*"-" + "\n" + lenpassword*"-" + "\n|  API PASSWORD : " + Back.GREEN + f" {API_PASSWORD} " + Style.RESET_ALL +  "  |\n" + lenpassword*"-" + "\n" + lenlot*"-" + "\n|  Lot : " + Back.GREEN + f" {size} " + Style.RESET_ALL +  "  |\n" + lenlot*"-" + "\n" + lensymbol*"-" + "\n|  Symbol : " + Back.GREEN + f" {symbol} " + Style.RESET_ALL + "  |\n" + lensymbol*"-" + "\n" + lenlevrage*"-" + "\n|  Levrage : " + Back.GREEN + f" {levrage} " + Style.RESET_ALL +  "  |\n" + lenlevrage*"-" + "\n")
    x = input("Dar Soorate Tayide Etelaat Adade 1 Ra Vared Konid Dar Gheyre In Soorat Adade Digari Vared Konid : ")

    if (x == "1"):
        system("cls")
        break
    
    else:   
        print("")
    
exchange = ccxt.kucoinfutures({
    "apiKey": API_KEY,
    "secret": API_SECRET,
    "password": API_PASSWORD,
    "enableRateLimit": True,
})

params = ({
    "leverage": levrage,
})

options = webdriver.ChromeOptions() 

options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=options)

driver.maximize_window()

driver.get("https://www.tradingview.com/chart/8kyOeZdd/")

driver.find_element(By.CSS_SELECTOR,".variant-primary-YKkCvwjV").click() #Accept All Cookies

driver.find_element(By.CSS_SELECTOR,".button-Nx2kr8lm").click() # Start Free Trial Button

time.sleep(4)

driver.find_element(By.XPATH,"""//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div/span""").click() # Email Button

time.sleep(1)

user = driver.find_element(By.NAME,"username")

user.send_keys("xxxx")

pas = driver.find_element(By.NAME,"password")

pas.send_keys("xxxx")

pas.send_keys(Keys.ENTER)

system("cls")

print("***Ebteda Dar Bargeye TradingView Kelid Zarbdar Ra Bezanid Sepas Dar Inja Enter Bezanid***")

system("pause") # Close Button

try:
    
    driver.find_element(By.CSS_SELECTOR,".button-glKypJku:nth-child(1)").click()

except:
    
    pass

try:

    driver.find_element(By.CSS_SELECTOR,".title-eYOhHEJX").click()

except:
    
    pass

try:
    
    driver.find_element(By.XPATH,"""//*[@id="bottom-area"]/div[4]/div/div[1]/div[3]/div/div/div/div/div/button[3]""").click()

except:
    
    pass

system("cls")

try:
    image = Image.open('images/1.png')

    image.show()

except Exception as e:

    print(e)

print("Agar Safheye TradingView Shoma Manande Akse Namayan Shode Ast Inja Yeki Az Klid Ha Ra Feshar Dahid")

system("pause")

system("cls")

def get_data():

   while True:

        global signal
        
        global a

        try:
            report = driver.find_element(By.CSS_SELECTOR,".reports-content")

            signal = (report.text[report.text.index("Exit"):report.text.index("Open")-1])
                
            m1 = float(driver.find_element(By.CSS_SELECTOR,".objectsTreeCanBeShown-OYqjX7Sg+ .sources-OYqjX7Sg .blockHidden-cdtqi65y+ .invisibleHover-OYqjX7Sg .valueItem-OYqjX7Sg:nth-child(1) .valueValue-OYqjX7Sg").text)

            m2 = float(driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/div/div[1]/div/table/tr[1]/td[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div[8]/div").text)

            price = float(driver.find_element(By.CSS_SELECTOR,".invisibleHover-OYqjX7Sg+ .invisibleHover-OYqjX7Sg .valueValue-OYqjX7Sg").text)
            
            if (m1 > price and m2 > price):
                a = "Sell"
            elif (m1 < price and m2 < price):
                a = "Buy"
            else:
                a = "Close"
        
        except Exception as e:

            print(e)

            if (token != ""):
                
                bot.send_message(chat_id=user_id, text=f"{e}")

def main():

    buy = 0

    short = 3

    error_counter = 0

    time.sleep(3)

    print("Working")

    if (token != ""):
        
        bot.send_message(chat_id=user_id, text="Bot Is Started On VPS")

    while True:

        if ( buy == 0 ):

            if ( signal == "Exit Long" and a == "Buy"):

                print ("Long Signal")
                
                if (token != ""):
                    
                    bot.send_message(chat_id=user_id, text="Long Signal")

                try:
                    
                    order_id = exchange.create_market_buy_order(symbol, size, params)    

                    buy = 1

                    short = 0

                    print("Ordere " + Back.GREEN + f"{order_id}" + Style.RESET_ALL + " Ba Movafaghiat Sabt Gardid")
                    
                    if (token != ""):
                    
                        bot.send_message(chat_id=user_id, text=f"Ordere {order_id} Ba Movafaghiat Sabt Gardid")
                    
                    error_counter = 0

                except Exception as error:

                    print(Fore.RED + "** Error : Hengame Sabte Order Moshkeli Pish Amade **" + Style.RESET_ALL)
                    
                    print(Fore.RED + f"{error}" + Style.RESET_ALL)
                    
                    if (token != ""):
                    
                        bot.send_message(chat_id=user_id, text=f"{error}")
                    
                    error_counter += 1
                    
                    time.sleep(10)
                    
                    if (error_counter == 10):
                        
                        print("Bish Az Hade Mojaz Talash Gardid!")
                        
                        driver.quit()
                        
                        break
                    
                    

        if ( short == 0 ):

            if ( signal == "Exit Short" ):

                print ("Short Signal")
                
                if (token != ""):
                
                    bot.send_message(chat_id=user_id, text="Short Signal")
                
                try:
                    
                    order_id = exchange.create_market_sell_order(symbol, size2, params)    

                    short = 1

                    buy = 2

                    print("Ordere " + Back.GREEN + f"{order_id}" + Style.RESET_ALL + " Ba Movafaghiat Sabt Gardid")
                    
                    if (token != ""):
                    
                        bot.send_message(chat_id=user_id, text=f"Ordere {order_id} Ba Movafaghiat Sabt Gardid")

                    error_counter = 0
                    
                except Exception as error:

                    print(Fore.RED + "** Error : Hengame Sabte Order Moshkeli Pish Amade **" + Style.RESET_ALL)
                    
                    print(Fore.RED + f"{error}" + Style.RESET_ALL)
                    
                    if (token != ""):
                        
                        bot.send_message(chat_id=user_id, text=f"{error}")

                    error_counter += 1
                    
                    time.sleep(10)
                    
                    if (error_counter == 10):
                        
                        print("Bish Az Hade Mojaz Talash Gardid!")
                        
                        driver.quit()
                        
                        break
                    
        if ( buy == 2 ):

            if ( signal == "Exit Long" ):

                print ("Long Signal")
                
                if (token != ""):
                    
                    bot.send_message(chat_id=user_id, text="Long Signal")

                try:
                    
                    order_id = exchange.create_market_buy_order(symbol, size2, params)

                    buy = 1

                    short = 0

                    print("Ordere " + Back.GREEN + f"{order_id}" + Style.RESET_ALL + " Ba Movafaghiat Sabt Gardid")
                    
                    if (token != ""):
                        
                        bot.send_message(chat_id=user_id, text=f"Ordere {order_id} Ba Movafaghiat Sabt Gardid")
                    
                    error_counter = 0

                except Exception as error:

                    print(Fore.RED + "** Error : Hengame Sabte Order Moshkeli Pish Amade **" + Style.RESET_ALL)        
                    
                    print(Fore.RED + f"{error}" + Style.RESET_ALL)
                    
                    if (token != ""):
                     
                        bot.send_message(chat_id=user_id, text=f"{error}")

                    error_counter += 1
                    
                    time.sleep(10)
                    
                    if (error_counter == 10):
                        
                        print("Bish Az Hade Mojaz Talash Gardid!")
                        
                        driver.quit()
                        
                        break
                    
        if (a == "Close" and buy == 1):
            
            try:
            
                print("Close Signal")
                
                if (token != ""):
                    
                    bot.send_message(chat_id=user_id, text="Close Signal")
                
                order_id = exchange.create_market_sell_order(symbol, size, params)
                
                if (token != ""):
                    
                    bot.send_message(chat_id=user_id, text=f"Ordere {order_id} Ba Movafaghiat Sabt Gardid")
                
                buy = 0
                
                short = 3
            
            except Exception as e:
                
                print(Fore.RED + "** Error : Hengame Sabte Order Moshkeli Pish Amade **" + Style.RESET_ALL)      
                
                print(e)
                
                if (token != ""):
                    
                    bot.send_message(chat_id=user_id, text=f"{error}")
                
        if (a == "Close" and short == 1):
            
            try:
            
                print("Close Signal")
                
                if (token != ""):
                    
                    bot.send_message(chat_id=user_id, text="Close Signal")
                
                order_id = exchange.create_market_sell_order(symbol, size, params)
                
                if (token != ""):
                    
                    bot.send_message(chat_id=user_id, text=f"Ordere {order_id} Ba Movafaghiat Sabt Gardid")
                
                buy = 0
                
                short = 3
            
            except Exception as e:
                
                print(Fore.RED + "** Error : Hengame Sabte Order Moshkeli Pish Amade **" + Style.RESET_ALL)      
                
                print(e)
                
                if (token != ""):
                                
                    bot.send_message(chat_id=user_id, text=f"{error}")

thread_one = threading.Thread(target = get_data)
thread_two = threading.Thread(target = main)
thread_one.start()
thread_two.start()
    
