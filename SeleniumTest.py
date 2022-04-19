from selenium import webdriver
from threading import Thread
import os
import time
#--------------------------Find_Chromedriver------------------------#
#ChromeDriver="chromedriver.exe"
#for r,d,f in os.walk("C:\\Users\\"):
#    for files in f:
#         if files == ChromeDriver:
#              file_chrome = os.path.join(r,files)
#-------------------------------------------------------------------#

#------------------------Chromedriver_Options-----------------------#
opt = webdriver.ChromeOptions()
opt.headless = True
#-------------------------------------------------------------------#

#----------------------------User_Inputs----------------------------#
kahoot_pin = input("Kahoot Pin:")
option_kahoot = input("Random(1) or Manual(2):")
if(int(option_kahoot)==2):
    name_kahoot_phrase = input("Username Phrase(with spaces):")
    time_sleep = input("Sleep Time(2 to generate phrases correctly ordered or 0 to be fast):")
    name_kahoot = name_kahoot_phrase.split()
    bot_count = len(name_kahoot)
    fill_thread = []
    for x in range(int(bot_count)):
        name = "t"+str(x)
        fill_thread.append(name)
if(int(option_kahoot)==1):
    time_sleep = 0
    name_main = input("Main name:")
    bot_count = input("Bots:")
    name_kahoot = []
    for x in range(int(bot_count)):
        name_test = name_main+str(x)
        name_kahoot.append(name_test)
    fill_thread = []
    for x in range(int(bot_count)):
        name = "t"+str(x)
        fill_thread.append(name)

#-------------------------------------------------------------------#

#----------------------------Kahoot_Info----------------------------#
# pin_id="game-input"                                               #
# pin_send_data_css_selector=".eilXIS"                              #
# name_id="nickname"                                                #
# name_send_data_css_selector=".eilXIS"                             #
#                                                                   #
#-------------------------------------------------------------------#

#------------------------Chromedriver_Start-------------------------#
def connec_kahoot(self,name_kahoot):
    web = webdriver.Chrome("--PATH TO CHROME DRIVER--",options=opt)
    web.get("https://kahoot.it/v2/")
    pin_id = web.find_element_by_id("game-input").send_keys(kahoot_pin)
    pin_send_data_css_selector = web.find_element_by_xpath("/html/body/div/div[1]/div/div[3]/div[2]/main/div/form/button").click()
    time.sleep(5)
    name_id = web.find_element_by_id("nickname").send_keys(name_kahoot)
    name_send_data_css_selector= web.find_element_by_xpath("/html/body/div/div[1]/div/div[3]/div[2]/main/div/form/button").click()
    while 1:
        pass
#-------------------------------------------------------------------#

#------------------------Connections_Thread-------------------------#
y=len(fill_thread)-1
for x in range(len(fill_thread)):
    fill_thread[x] = Thread(target=connec_kahoot,args=(webdriver,name_kahoot[y]))
    fill_thread[x].start()
    time.sleep(int(time_sleep))
    y-=1

#-------------------------------------------------------------------#
