import pyautogui
pyautogui.alert('This is a message.', 'Important')
password = pyautogui.password('What is the Password')
print(password)