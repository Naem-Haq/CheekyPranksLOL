#!/usr/bin/python
import pyautogui
import webbrowser
import time

#This is what will be sent. 
message = input("What message do you want to keep sending? (Leave this blank if you want to paste your clipboard)  ")

#go ham honestly, i do a cheeky lil hundo.
repeats = int(input("How many times do you want to send the message?  "))

#100 milliseconds between each message worked best for me.
delay = int(input("How many milliseconds do you want to wait in between each message?  "))

#Now enjoy it!
isLoaded = input("Press Enter when your messaging app is loaded up.")


#Select the chat box of app and select it. (wont work if you leave the app, i just do split screen)
print("You have five seconds to refocus the text input area of your messaging app")

time.sleep(5)


for i in range(0,repeats):         #Message sending loop
	if message != "":
		pyautogui.typewrite(message)     
		pyautogui.press("enter")
	else:
		pyautogui.hotkey('ctrl', 'v')      
		pyautogui.press("enter")

	time.sleep(delay/1000)


print("Done\n")
