# import required libraries

import requests
import re
import smtplib
from bs4 import BeautifulSoup

# add multiple or single url to check for the price 

url = 'https://www.flipkart.com/aple-macbook-air-core-i5-8th-gen-8-gb-256-gb-ssd-mac-os-mojave-mref2hn-a/p/itmfb9vw4kykhape?pid=COMFB9VWGA9XHMSQ&lid=LSTCOMFB9VWGA9XHMSQDZAVA7&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&fm=SEARCH&iid=3e2e891f-53fd-4018-8e11-1f08a7cebb05.COMFB9VWGA9XHMSQ.SEARCH&ppt=sp&ppn=sp&ssid=uu80g9lk6o0000001595266154665&qH=b61d62051d5441f9'

def check_price():
    '''Function to check the price of the product'''
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    title = soup.find_all(class_ = '_35KyD6')[0].get_text() #class to get the  exact title
    price = soup.find(class_='_1vC4OE _3qQ9m1').get_text()  #class for getting exact price of product
    price = price[1:]
    price = re.sub(',','',price)
    price = float(price)
    print(title,',',price)
    if price<150000: #add your desired price
        sendEmail()

def sendEmail():
    '''Function to send the mail through personal mailid to anyone'''
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('your mail id','your password') #make sure you change your settings in gmail to allow mail from less secure apps
    subject = 'check the price' #subject
    # body
    body = 'Click to purchase https://www.flipkart.com/apple-macbook-air-core-i5-8th-gen-8-gb-256-gb-ssd-mac-os-mojave-mref2hn-a/p/itmfb9vw4kykhape?pid=COMFB9VWGA9XHMSQ&lid=LSTCOMFB9VWGA9XHMSQDZAVA7&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&fm=SEARCH&iid=3e2e891f-53fd-4018-8e11-1f08a7cebb05.COMFB9VWGA9XHMSQ.SEARCH&ppt=sp&ppn=sp&ssid=uu80g9lk6o0000001595266154665&qH=b61d62051d5441f9 '
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail('from mail id','to mail id',msg)
    print('email sent')
    server.quit()

check_price()
