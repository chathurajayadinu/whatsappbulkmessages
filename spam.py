import pyautogui
import webbrowser as wb
import time
wb.open("web.whatsapp.com")
time.sleep(30)
for i in range(100):
    pyautogui.prress("H")
    pyautogui.press("i")
    pyautogui.press("enter")