"""
This program does it's job of updating the hosts file on mac, however,
this is not a effective method of blocking websites in general...
"""

import time
from datetime import datetime as dt

hostsPath = '/private/etc/hosts'
redirect = '127.0.0.1'
redirect1 = '::1'

websiteBlockList = ['youtube.com', 'www.youtube.com', 'http://www.youtube.com', 'https://www.youtube.com', 'http://youtube.com', 'https://youtube.com']

while True: 
        # Establish multiple datetime objects
        now = dt.now()
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
                        hosts.write(redirect + '    ' + website + '\n')
                        hosts.write(redirect1 + '    ' + website + '\n')    
        else:
            print('Time for some fun...')
            with open(hostsPath, 'r+') as hosts:
                buffer = hosts.readlines()
                hosts.seek(0)
                for lines in buffer:
                    if not any(websites in lines for websites in websiteBlockList):
                        hosts.write(lines)
                hosts.truncate()
        time.sleep(5)
