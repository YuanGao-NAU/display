#!/usr/bin/python3

from bs4 import BeautifulSoup
from module.i2c import *
import requests
import time
import math
import sys



while True:
    from module.corona import *
    lcd_init()
    time.sleep(1)
    lcd_string((cc)+(" Infected ")+(infections_c),LCD_LINE_1)
    lcd_string(("WW Infected ")+(infections_w),LCD_LINE_2)
    
    time.sleep(10)
    
    lcd_init()
    time.sleep(1)
    lcd_string((cc)+(" ")+(deaths_c)+(" Deaths"),LCD_LINE_1)
    lcd_string(("WW ")+(deaths_w)+(" Deaths"),LCD_LINE_2)
    
    time.sleep(10)
    
    lcd_init()
    time.sleep(1)
    lcd_string((cc)+(" Recoverd ")+(survived_c),LCD_LINE_1)
    lcd_string(("WW ")+(survived_w),LCD_LINE_2)
    
    time.sleep(10)
    
    time.sleep(5)

            
        
