import pyautogui, time, subprocess

# Open Paint
subprocess.Popen('C:\\WINDOWS\\system32\\mspaint.exe')
time.sleep(4)
pyautogui.moveTo(140, 242)
pyautogui.click() # click to put drawing program in focus
distance = 200
while distance > 0:
    pyautogui.dragRel(distance, 0) # move right
    distance = distance - 5
    pyautogui.dragRel(0, distance) # move down
    pyautogui.dragRel(-distance, 0) # move left
    distance = distance - 5
    pyautogui.dragRel(0, -distance) # move up