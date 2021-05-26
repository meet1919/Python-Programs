import pyautogui, time, webbrowser

webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform')
time.sleep(2)
pyautogui.click(402, 402)
pyautogui.typewrite('Meet Gondaliya' + '\t')
pyautogui.typewrite('Public Speaking' + '\t')
pyautogui.typewrite(['enter'])
pyautogui.press('down')
pyautogui.typewrite(['enter'])
pyautogui.typewrite(['\t'])
pyautogui.typewrite(['right', 'right'])
pyautogui.typewrite(['\t', '\t'])
pyautogui.typewrite('No comments')
pyautogui.typewrite(['\t', 'enter'])


