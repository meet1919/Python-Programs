import pyautogui, time
print('Press Ctrl-C to quit.')
try:
    while True:
        # Get and print the mouse coordinates.
        pos = pyautogui.position()
        positionStr = '%s, %s' % (pos[0], pos[1])
        color_pixel = pyautogui.screenshot().getpixel((pos[0], pos[1]))
        value = 'X: %s Y: %s || RGB: (%s)' % (pos[0], pos[1], color_pixel)
        print(value, end='')
        time.sleep(0.3)

        print('\b' * len(value), end='', flush=True)

except KeyboardInterrupt:
    print('\nDone.')

