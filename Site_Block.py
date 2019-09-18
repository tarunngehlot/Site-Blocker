from datetime import datetime as dt
import time

host_temp='hosts'
host_path='C:\Windows\System32\drivers\etc\hosts'
websites = ['www.google.com','google.com']
redirect = '127.0.0.1'

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,19) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,23,44):
        print('Working Hours....')
        with open(host_path,'r+') as file:
            contents=file.read()
            for website in websites:
                if website in contents:
                    pass
                else:
                    file.write(redirect+" "+website+"\n")
    else:
        print('Fun Hours....')
        with open(host_path,'r+') as file:
            contents=file.readlines()
            file.seek(0)
            for line in contents:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)
