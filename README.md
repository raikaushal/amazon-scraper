# amazon-scraper

this Scraper uses python and selenium and extracts data(product name,price etc) from amazon using keywords and provides output in json format.

# Dependencies

Python-selenium support few browsers such as chrome and firefox.

I recommend to go with chrome web driver

you can download latest webdriver using following link

link to download chrome webdriver https://sites.google.com/a/chromium.org/chromedriver/downloads

Add the Path of chrome webdriver in Code

#snippet

from selenium import webdriver

#Include Path of your Chrome driver

driver = webdriver.Chrome(r"path\to\your\chomedriver.exe")

This Project also uses BeautifulSoup4 to Parse the Html data and Extract content from it

you can find Beautiful soup documentation here https://www.crummy.com/software/BeautifulSoup/bs4/doc/

the Output of this program will be in json format e.g if You search for "whey Protien" your output will be
list containing multiple products


You can also specify the Maximum pages to which you want to scrape the data.

Thanks
