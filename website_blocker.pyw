"""
The host file in /etc is updated to redirect a given url to 127.0.0.1 to block it
Changing extension of file from .py to .pyw makes it run in background. This is run from Pythonw.exe instead of python.exe
"""
import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect="127.0.0.1"
website_list=["www.facebook.com","www.instagram.com"]

while True:
    if dt(dt.now().year,dt.now().month, dt.now().day, 16) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day, 18):
        print("Working Hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass #do not do anything, go to next lines
                else:
                    file.write(redirect +" "+ website+"\n")

    else:
        with open(hosts_path,'r+') as file:
            content=file.readlines() #Pointer reaches end of file Windows
            file.seek(0)#go to start of file
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line) #Add all lines but the lines that block a url
            file.truncate() #delete all lines below
        print("Fun Hours...")
    time.sleep(5)#Sleep for 5 seconds

"""
To always run this script on startup -
Open Task Scheduler
Create Task
- Name the Task
- Configure for windows 10
- Check Run with highest privileges
- Under triggers tab, click New..., Begin task at startup
- Under Actions tab, click New..., Create an action to start a program, and browse the script to Run
- Under Conditions tab, Uncheck the "Start the task only if the computer is on AC power" option
- Click Ok
- Run the task from the tab in the right.
"""
