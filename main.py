import ipinfo
import os
import requests

access_token=os.environ.get('TOKEN')
handler= ipinfo.getHandler(access_token)

ip_address = input('Enter the IP: ')
try:
    result = handler.getDetails(ip_address)
    print(f"\nIP : {result.ip} \nCity: {result.city} \nRegion: {result.region} \nCountry : {result.country} \nPostal Code : {result.postal} \nTimezone: {result.timezone}")
except:
    print(' !!ERROR!! \n Encountered an Error. Possible Errors: \n 1. The IP Address is wrong \n 2. Your access token is wrong')



  