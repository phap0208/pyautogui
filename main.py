import time
import pyautogui
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
pyautogui.click(777, 1047)
time.sleep(5)
pyautogui.write('facebook.com', interval=0.25)
pyautogui.press('enter')
time.sleep(7)
pyautogui.click(802, 379)
time.sleep(10)
pyautogui.write('test chuong trinh ', interval=0.25)
pyautogui.click(957, 802)
