import requests
import json
from pprint import pprint
import tkinter as tk

# Variable that stores name on input

# Create TKinter window
window = tk.Tk()
window.title('Bedwars player lookup')
window.geometry('300x300')

canvas1 = tk.Canvas(window, width=400, height=300)
canvas1.pack()

inputfield = tk.Entry(window)
canvas1.create_window(200, 140, window=inputfield)


# Function with an argument 'call' that grabs 'name_link' and inputs and gets the info via the url in the variable 'name_link'
# Grabs stats based from name

    # Function isn't called that's why it throws exception and says that it cannot find player_name_input
# def player_input():
#     global player_name_input
#     player_name_input = inputfield.get()
#     label1 = tk.Label(window, text=get_info(player_name_input))
#     canvas1.create_window(200, 230, window=label1)
#     return player_name_input()





# Search by UUID; Not implemented yet
uuid = 'f5d767ffb1ae4ea19c8cf683ef52e05e'
uuid_dashed = 'f5d767ff-b1ae-4ea1-9c8c-f683ef52e05e'

# API Key accesses Hypixel's API and allows data to be pulled in
API_KEY = "3c29eae3-03d6-4a40-a3f8-aca3d8931fa7"

# Hypixel API JSON files
#name_link = f"https://api.hypixel.net/player?key={API_KEY}&name={player_name_input}"
uuid_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid_dashed}"

#get_info(name_link)

#button1 = tk.Button(text='Get bedwars level', command=get_info(name_link))
#canvas1.create_window(200, 180, window=button1)

window.mainloop()
