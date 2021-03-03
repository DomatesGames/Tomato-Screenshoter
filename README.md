# Tomato-Screenshoter
A screenshot program in Python.
Most people search like this:

How to take make create write screenshot in Python, How to create make write take screenshoter screenshot with Python 3

Actually it's easy to take screenshots with PyAutoGUI.
(type ```pip install PyAutoGUI``` and ```pip install Pillow``` in cmd/terminal)
```
import PyAutoGUI 
pyautogui.screenshot("screenshot.png")
```


But when the program is open it takes a screenshot, first let the user minimize the program.

```import pyautogui
import time
time.sleep(3)
pyautogui.screenshot(screenshot.png")
```

Hah! Good now! But maybe the user wants to wait differently.

```
import pyautogui
import time
waiting = int(input ("Waiting time:"))
time.sleep(waiting)
pyautogui. screenshot ("screenshot.png")
```

Nice!

Maybe the user wants to name the screenshot herself/himself.
```import pyautogui
import time
waiting = int(input("Waiting time: "))
name = input("Name of the Screenshot? ")
time.sleep(waiting)
pyautogui.screenshot(name + ".png")
```
Done now! Very nice!
