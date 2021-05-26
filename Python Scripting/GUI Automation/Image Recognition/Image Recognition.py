import pyautogui, time
loc = pyautogui.locateOnScreen('explorer.png')
center = pyautogui.center(loc)
pyautogui.click(center)
time.sleep(2)
pyautogui.moveTo(231, 52, duration=0.15)
pyautogui.click()
pyautogui.typewrite('INTP')
pyautogui.press('enter')