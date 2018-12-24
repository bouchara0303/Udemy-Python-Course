#This program does it's job of updating the hosts file on OSX, however,
#this is not a effective method of blocking websites in general...

import time
from datetime import datetime as dt

#Hosts file path will likely be different on different OS
hostsPath = '/private/etc/hosts'
redirect = '127.0.0.1'
redirectIPV6 = '::1'

#Change to desired websites to be blocked. Include both www version and non www version of url
#(eg. ['www.example.com', 'example.com']).
websiteBlockList = ['youtube.com', 'www.youtube.com']

while True:
        #Establish datetime objects
        now = dt.now()

        #Change hours of date time object to specify hours of website blocking
        start = dt(now.year, now.month, now.day, 10)
        finish = dt(now.year, now.month, now.day, 12)
        
        if (start < now < finish):
            print('You should be working...')
            with open(hostsPath, 'r+') as hosts:
                buffer = hosts.read()
                for website in websiteBlockList:
                    if website in buffer:
                        pass
                    else:
                        hosts.write(redirectIPV4 + '    ' + website + '\n')
                        hosts.write(redirectIPV6 + '    ' + website + '\n')
        else:
            print('Time for some fun!')
            with open(hostsPath, 'r+') as hosts:
                buffer = hosts.readlines()
                hosts.seek(0)
                for lines in buffer:
                    if not any(websites in lines for websites in websiteBlockList):
                        hosts.write(lines)
                hosts.truncate()
        #Checks every 5 seconds
        time.sleep(5)
