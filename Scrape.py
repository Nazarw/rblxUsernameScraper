import requests
import threading
import string
import random
import ctypes
import os

foo = ['4','5','6','7','8','9']

os.system("cls")

Found = 0
Failed = 0

APIURL = "https://api.roblox.com/"
UserAPI = APIURL + "users/"

def generate(len):
    return ''.join(random.choice('1234567890') for x in range(int(len)))


def GetName(UserID): #robloxpy
    response = requests.get(UserAPI + str(UserID))
    try:
        return response.json()['Username']
    except:
        return 'User not found'

def Check():
    global Found
    global Failed

    user = generate(random.choice(foo))
    check = (GetName(user))

    r = requests.get('https://www.roblox.com/users/'+ user +'/profile')

    if "content=https://www.roblox.com/users/" + user +"/profile" in r.text:
        Found += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f'ROBLOX Scraper | Found: {Found} | Failed: {Failed}')
        print("\u001b[32m[+]: " + user + " | " + check)
        with open("profiles.txt","a") as names_gen:
            names_gen.write(check + "\n")
    else:
        Failed += 1
        ctypes.windll.kernel32.SetConsoleTitleW(f'ROBLOX Scraper | Found: {Found} | Failed: {Failed}')
        print("\u001b[31m[-]: " + user + " | " + "Not Found")

while True:
    while threading.active_count() < int(250):
        threading.Thread(target=Check()).start()


input()