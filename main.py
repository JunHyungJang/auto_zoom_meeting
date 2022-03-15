import os
import sys
import time
import threading
import datetime
import json
import webbrowser
from platform import system

def run():
    flag = 0
    while 1:
        date_time = datetime.datetime.now()


        dlist = ["mon", "tue", "wed", "thu", "fri"]

        t = time.localtime()
        y = str(t.tm_year)
        mo = str(t.tm_mon)
        dt = str(t.tm_mday)
        dy = dlist[t.tm_wday]

        now_time = time.strftime("%H%M", t) #1230

        with open("meeting.json") as f:
            meeting = json.load(f)

        # print(meeting)

        next_time = []

        for meeting_time in meeting[dy].keys():
            if now_time <= meeting_time:
                next_time.append(meeting_time)

        next_time = min(next_time)

        full_next_time = y+mo+dt+next_time
        full_next_time = datetime.datetime.strptime(full_next_time, "%Y%m%d%H%M")

        min_left = full_next_time - date_time
        min_left = min_left.seconds/60
        # print(min_left)

        subject = meeting[dy][next_time]["subject"]
        num = meeting[dy][next_time]["num"]
        pw = meeting[dy][next_time]["pw"]

        url = "zoommtg://zoom.us/join?confno={}&pwd={}".format(num,pw)
        # url = "zoommtg://zoom.us/join?confno={}".format(num)


        if 0<=min_left<=5 :
            print("_____________JUN's program start_____________")
            print("Next class", subject)
            print("Time left", int(min_left), "minute(s) left\n")

            webbrowser.open(url)
            flag +=1
            time.sleep(5000)
            # sys.exit()
        
        
        threading.Timer(60,run).start()


        # print("keepgoing")
run()


