# import random
# l1 = ['A', 'B', 'C', 'D']
# matched_indexes = []
# i = 0
# length = len(l1)
# rnglist = []
# for i in range(100):
#     randomLetter = random.choice(l1)
#     rnglist.append(randomLetter)
# print(rnglist)
# count = rnglist.count('A')
# print(f"Tienes {count} A")
# print ("Menor que la media" if count < 25 else "Mayor que la media")
# count = rnglist.count('B')
# print(f"Tienes {count} B")
# print ("Menor que la media" if count <= 25 else "Mayor que la media")
# count = rnglist.count('C')
# print(f"Tienes {count} C")
# print ("Menor que la media" if count <= 25 else "Mayor que la media")
# count = rnglist.count('D')
# print(f"Tienes {count} D")
# print ("Menor que la media" if count <= 25 else "Mayor que la media")

# from datetime import datetime

# hoy = datetime.now()
# print(hoy.year)
# print(hoy.month)
# print(hoy.day)
# print(hoy.hour)
# print(hoy.minute)
# print(hoy.second)
# print(hoy.microsecond)
# print(hoy.strftime("%Y/%F/%d"))
# print(hoy)

import webbrowser

import webbrowser
chrome = webbrowser.get('google-chrome') # or webbrowser.get('chrome')
chrome.open_new_tab('chrome://newtab',"www.google.com")