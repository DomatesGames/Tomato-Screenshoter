import pyautogui
import time
bekletme = int(input("Bekletme süresi (sayı olarak yazın): "))
isim = input("Ekran alıntısının ismi? ")
time.sleep(bekletme)
pyautogui.screenshot(isim + ".png")
