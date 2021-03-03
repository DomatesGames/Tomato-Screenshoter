import pyautogui
import time
waiting = int(input("Waiting time: "))
name = input("Name of the Screenshot? ")
time.sleep(waiting)
pyautogui.screenshot(name + ".png")
