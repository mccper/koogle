from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import json
import threading
import asyncio
import datetime
from flask import Flask, render_template, request


gmailId = "kooglex33@gmail.com"
passWord = "Hh9JjHh9Jj"
driver_path = "C:\Drivers\chromedriver.exe"
profile_file = "profils.json"


NOW = "now"
PROFILE = "profile"
SEARCHES = "searches"
MINUTE = "minute"
HOUR = "hour"


class Search:

    def __init__(self,jsonim: dict[str,str|bool]) -> None:
        self.now = jsonim.get(NOW,True)
        self.profile = jsonim.get(PROFILE,"old dude")
        self.searches = int(jsonim.get(SEARCHES,1))
        self.minute = int(jsonim.get(MINUTE,0))
        self.hour = int(jsonim.get(HOUR,0))

    
    def start(self):
        thred = threading.Thread(target=self.profile_search)
        thred.daemon = True
        thred.start()

    def profile_search(self):
        if self.now is False:
            seconsd = get_seconds_from_now(self.hour,self.minute)
            asyncio.run(asyncio.sleep(seconsd))
        for obj in open_json(profile_file)[self.profile]:
            search_something(obj,self.searches)


def open_driver(driver_path):
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://www.google.co.il/")
    
def search_something(WhatToSerch,count):
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get("https://www.google.co.il/")
    driver.find_element(By.NAME, "q").click()
    driver.find_element(By.NAME, "q").send_keys(WhatToSerch)
    asyncio.run(asyncio.sleep(0.5))
    driver.find_element(By.NAME, "btnK").click()
    asyncio.run(asyncio.sleep(0.5))

    links = driver.find_elements(By.CSS_SELECTOR, "div[class=yuRUbf] a")
    for link in links:
        if count > 0:
            try:
                ActionChains(driver).move_to_element(link).click(link).perform()
                asyncio.run(asyncio.sleep(0.5))
                driver.back()
                asyncio.run(asyncio.sleep(0.5))
                count -= 1    
            except:
                print("something happened")
                    

    
def open_json(json_file):
    f = open(json_file, encoding='utf-8')
    data = json.load(f)
    f.close()
    return data




def get_seconds_from_now(hour, minute):
    hour, minute = int(hour), int(minute)
    current_time = datetime.datetime.now()
    target_time = current_time.replace(hour=hour, minute=minute, second=0, microsecond=0)

    if target_time < current_time:
        # If the target time is in the past, add one day to the target time
        target_time += datetime.timedelta(days=1)

    time_difference = target_time - current_time
    seconds = time_difference.total_seconds()
    return seconds


app = Flask(__name__)



@app.route('/', methods=['POST'])
def add_book():
    arg = Search(request.get_json())
    arg.start()
   
    return "y"

if __name__ == "__main__":
    app.run(debug=True, port=5000)


