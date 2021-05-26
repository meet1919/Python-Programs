import pyautogui

pyautogui.moveTo(436, 181)
for i in range(8):
    pyautogui.moveRel(-100, 0, duration=0.25)
    pyautogui.moveRel(0, 100, duration=0.25)
    pos = pyautogui.position()
    if pos[0] == 36:
        pyautogui.click()

