
import time 
from datetime import datetime 
import pyautogui
from pynput.keyboard import Controller
from pynput.keyboard import Key
import webbrowser as wb
lst=[
    ['https://teams.microsoft.com/l/meetup-join/19%3ameeting_YjEwOWNmZDMtMmQ5MC00NDM5LWFhZWUtMTY5NjZmZjJhMGI2%40thread.v2/0?context=%7b%22Tid%22%3a%226d28e4fb-9074-4a0b-a5b8-9a89f632cc60%22%2c%22Oid%22%3a%22377bd695-6601-4d9d-9bb1-bbd5cafd3784%22%7d','10:10','12.29']
#input lecture stats in form of list ......
# ["Link","start_time","end_time"]
# give time in 24 hrs format...
]
keyboard= Controller()

is_class_started =False
for lecture  in lst:
    while True :
        if is_class_started==False:
            if  (datetime.now().hour >= int(lecture[1].split(':')[0]) and 
                datetime.now().minute >= int(lecture[1].split(':')[1])):
                wb.open(lecture[0])
                is_class_started=True
                time.sleep(20)
                #pyautogui.moveTo(845,585)
                pyautogui.press('right')
                time.sleep(1)
                pyautogui.press('enter')
                time.sleep(5)
                pyautogui.hotkey('ctrl','shift','m')

                #time.sleep(1)
                #pyautogui.click()
                #time.sleep(1)
                #pyautogui.moveTo(1160,580)
                #time.sleep(1)
                #pyautogui.click()
                #(845,585),(1160,580)
                break
                
        #else :
            #(datetime.now().hour == int(lecture[2].split(':')[0]) and
             #  datetime.now().minute == int(lecture[2].split(':')[1])):
  
              #  time.sleep(60)
               # Keyboard.press(key.enter)