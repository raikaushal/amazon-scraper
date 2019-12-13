# amazon-scraper

this Scraper uses python and selenium and extracts data(product name,price etc) from amazon using keywords and provides output in json format.

#Dependencies

Python-selenium support few browsers such as chrome and firefox.

I recommend to go with chrome web driver

you can download latest webdriver using following link

link to download chrome webdriver https://sites.google.com/a/chromium.org/chromedriver/downloads

Add the Path of chrome webdriver in Code

#snippet

from selenium import webdriver

# Include Path of your Chrome driver

driver = webdriver.Chrome(r"path\to\your\chomedriver.exe")

This Project also uses BeautifulSoup4 to Parse the Html data and Extract content from it

you can find Beautiful soup documentation here https://www.crummy.com/software/BeautifulSoup/bs4/doc/

the Output of this program will be in json format e.g if You search for "whey Protien" your output will be
list containing multiple products

e.g
{
"ProductUrl": "https://www.amazon.in/dp/B07KY2WP24/",
"ProductName": "Scitron Raw Whey (100% Whey Protein Concentrate,24g Protein, 0g Sugar, 33 Servings,9 Essential Amino Acids, No Flavours & Preservatives) - 2.2 lbs (1 kg)",
"Price": "698.00",
"ProductFeatures": [
"Scitron Raw Whey is an unflavoured and unsweetened protein supplement that provides 24g protein per serving of 30g",
"Loaded with naturally occurring amino acids, it is easily absorbed to maintain and improve lean muscle mass",
"With no added flavour, Scitron Raw Whey can be used as per your individual taste",
"Helps to deliver greater gains in strength, muscle and lean body mass to help you get the most out of your training"
],
"Availibility": "In stock on December 16, 2019.",
"CustomerReviews": "3.5"
}

You can also specify the Maximum pages to which you want to scrape the data.

Thanks
