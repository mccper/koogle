import customtkinter
import requests
import json

NOW = "now"
PROFILE = "profile"
SEARCHES = "searches"
MINUTE = "minute"
HOUR = "hour"

data_json = { PROFILE : "profile",
              SEARCHES : "searches",
              MINUTE : "0",
              HOUR : "0"}

profile_file = "D:\WIN10\Documents\koogle\src\profils.json"
url = ("http://127.0.0.1:5000")



def send_data():
    data = {
        PROFILE : data_json[PROFILE],
        SEARCHES : data_json[SEARCHES]
    }
    requests.post(url, json=data)
    


def send_later_data():
    data = {
        NOW : False,
        PROFILE : data_json[PROFILE],
        SEARCHES : data_json[SEARCHES],
        MINUTE : data_json[MINUTE],
        HOUR : data_json[HOUR]
    }
    print(data)
    requests.post(url, json=data)

def data_profile(data):
    data_json[PROFILE] = data
    

def data_searches(data):
    data_json[SEARCHES] = data

def data_minute(data):
    data_json[MINUTE] = data

def data_hour(data):
    data_json[HOUR] = data

def write_json(new_data):
    print(data_json[PROFILE])
    with open(profile_file, encoding='utf-8') as f:
        data = json.load(f)
        data[data_json[PROFILE]].append(new_data)

    with open(profile_file, "w", encoding='utf-8') as x:
        json.dump(data, x, indent=2)
    print(new_data, "added to ",data_json[PROFILE])


def main():
    customtkinter.set_appearance_mode("dark")   
    customtkinter.set_default_color_theme("blue") 


    app = customtkinter.CTk()
    app.geometry("600x600")
    app.title("koogle selection")

    frame_1 = customtkinter.CTkFrame(master=app)
    frame_1.pack(pady=20, padx=60, fill="both", expand=True)

    sidebar_frame = customtkinter.CTkFrame(master=frame_1, width=140)
    sidebar_frame.pack(pady=10, padx=10)
    logo_label = customtkinter.CTkLabel(sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
    logo_label.pack(pady=10, padx=10)

    tabview = customtkinter.CTkTabview(master=frame_1, width=400, height=400)
    tabview.pack(padx=(20, 0), pady=(20, 0))
    tabview.add("start seshen")
    tabview.add("scajuol seshen")
    tabview.add("setings")

    combobox_1 = customtkinter.CTkComboBox(tabview.tab("start seshen"),values=["terrorist", "old dude", "girl"],command=data_profile)
    combobox_1.pack(pady=10, padx=10)
    combobox_1.set("select profil")


    combobox_2 = customtkinter.CTkComboBox(tabview.tab("start seshen"), values=["1", "2", "3"],command=data_searches)
    combobox_2.pack(pady=10, padx=10)
    combobox_2.set("serches")

    button_1 = customtkinter.CTkButton(tabview.tab("start seshen"), command=send_data) #set_search_call
    button_1.pack(pady=10, padx=10)
    button_1.configure(text="start")

    combobox_3 = customtkinter.CTkComboBox(tabview.tab("setings"),values=["terrorist", "old dude", "girl"],command=data_profile)
    combobox_3.pack(pady=10, padx=10)
    combobox_3.set("select profil")

    entry = customtkinter.CTkEntry(tabview.tab("setings"), placeholder_text="wirte value")
    entry.pack(pady=10, padx=10)

    entry_botton = customtkinter.CTkButton(tabview.tab("setings"), text="add",command=lambda: write_json(entry.get()))
    entry_botton.pack(pady=10, padx=10)

    combobox_4_hour = customtkinter.CTkComboBox(tabview.tab("scajuol seshen"),values=[str(x) for x in range(24)],command=data_hour)
    combobox_4_hour.pack(pady=10, padx=10)
    combobox_4_hour.set("select hour")

    combobox_5_minute = customtkinter.CTkComboBox(tabview.tab("scajuol seshen"),values=[str(x) for x in range(61)],command=data_minute)
    combobox_5_minute.pack(pady=10, padx=10)
    combobox_5_minute.set("select minute")

    combobox_6 = customtkinter.CTkComboBox(tabview.tab("scajuol seshen"),values=["terrorist", "old dude", "girl"],command=data_profile)
    combobox_6.pack(pady=10, padx=10)
    combobox_6.set("select profil")

    combobox_7 = customtkinter.CTkComboBox(tabview.tab("scajuol seshen"), values=["1", "2", "3"],command=data_searches)
    combobox_7.pack(pady=10, padx=10)
    combobox_7.set("serches")

    scajuol_botton = customtkinter.CTkButton(tabview.tab("scajuol seshen"), text="book",command=send_later_data)
    scajuol_botton.pack(pady=10, padx=10)

    app.mainloop()


if __name__ == "__main__":
    main()


