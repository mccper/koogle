from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import json
import customtkinter
import threading
import asyncio
import datetime

gmailId = "kooglex33@gmail.com"
passWord = "Hh9JjHh9Jj"
driver_path = "C:\Drivers\chromedriver.exe"
profile_file = "profils.json"

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


def profile_search(wait):
    if wait:
        profile = combobox_6.get()
        serches = int(combobox_7.get())
        seconsd = get_seconds_from_now(combobox_4_hour.get(),combobox_5_minute.get())
        asyncio.run(asyncio.sleep(seconsd))
    else:
        profile = combobox_1.get()
        serches = int(combobox_2.get())
    for obj in open_json(profile_file)[profile]:
        search_something(obj,serches)
        

def set_search(wait=False):
    thred = threading.Thread(target=profile_search, args=(wait,))
    thred.daemon = True
    thred.start()


def write_json():
    new_data = entry.get()
    with open(profile_file, encoding='utf-8') as f:
        data = json.load(f)
        data[combobox_3.get()].append(new_data)

    with open(profile_file, "w", encoding='utf-8') as x:
        json.dump(data, x, indent=2)

    print(new_data, "added to ",combobox_3.get())


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


def set_search_scjul_serch():
    set_search(True)


customtkinter.set_appearance_mode("dark")   
customtkinter.set_default_color_theme("blue") 

app = customtkinter.CTk()
app.geometry("600x600")
app.title("koogle selection")

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

sidebar_frame = customtkinter.CTkFrame(master=frame_1, width=140)
sidebar_frame.pack(pady=10, padx=10)
logo_label = customtkinter.CTkLabel(sidebar_frame, text="KOOGLE", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label.pack(pady=10, padx=10)

tabview = customtkinter.CTkTabview(master=frame_1, width=400, height=400)
tabview.pack(padx=(20, 0), pady=(20, 0))
tabview.add("Start Session")
tabview.add("Schedule Session")
tabview.add("Setings")

combobox_1 = customtkinter.CTkComboBox(tabview.tab("Start Session"),values=["terrorist", "old dude", "girl"])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("Select profil")

combobox_2 = customtkinter.CTkComboBox(tabview.tab("Start Session"), values=["1", "2", "3"])
combobox_2.pack(pady=10, padx=10)
combobox_2.set("Searches")

button_1 = customtkinter.CTkButton(tabview.tab("Start Session"), command=set_search)
button_1.pack(pady=10, padx=10)
button_1.configure(text="start")

combobox_3 = customtkinter.CTkComboBox(tabview.tab("Setings"),values=["terrorist", "old dude", "girl"])
combobox_3.pack(pady=10, padx=10)
combobox_3.set("select profil")

entry = customtkinter.CTkEntry(tabview.tab("Setings"), placeholder_text="wirte value")
entry.pack(pady=10, padx=10)

entry_botton = customtkinter.CTkButton(tabview.tab("Setings"), text="add value", command=write_json)
entry_botton.pack(pady=10, padx=10)

combobox_4_hour = customtkinter.CTkComboBox(tabview.tab("Schedule Session"),values=["1", "2", "3","4","5","6","7","8","9","10"
                                                                                  ,"11","12","13","14","15","16","17","18","19","20","21","22","23","24"])
combobox_4_hour.pack(pady=10, padx=10)
combobox_4_hour.set("select hour")

combobox_5_minute = customtkinter.CTkComboBox(tabview.tab("Schedule Session"),values=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'
                                                                                     , '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'
                                                                                     , '22', '23', '24', '25', '26', '27', '28', '29', '30',
                                                                                       '31', '32', '33', '34', '35', '36', '37', '38', '39', '40'
                                                                                       , '41', '42', '43', '44', '45', '46', '47', '48', '49', '50'
                                                                                       , '51', '52', '53', '54', '55', '56', '57', '58', '59', '60'])
combobox_5_minute.pack(pady=10, padx=10)
combobox_5_minute.set("select minute")

combobox_6 = customtkinter.CTkComboBox(tabview.tab("Schedule Session"),values=["terrorist", "old dude", "girl"])
combobox_6.pack(pady=10, padx=10)
combobox_6.set("select profil")

combobox_7 = customtkinter.CTkComboBox(tabview.tab("Schedule Session"), values=["1", "2", "3"])
combobox_7.pack(pady=10, padx=10)
combobox_7.set("serches")

scajuol_botton = customtkinter.CTkButton(tabview.tab("Schedule Session"), text="Book Session",command=set_search_scjul_serch)
scajuol_botton.pack(pady=10, padx=10)

app.mainloop()


#write_json("fgg")
#open_json("D:\WIN10\Desktop\koogle\profils.json")
#loop_search('terrorist')
#loop_search("old dude")

