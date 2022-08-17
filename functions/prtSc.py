from start import driver
import datetime


def screenshot():
    now = datetime.datetime.now()
    driver.save_screenshot(
        'C:\work\screen_selen\screen_' + str(now.hour) + '.' + str(now.minute) + '.' + str(now.microsecond) + '.png')


def srcShot():
    now = datetime.datetime.now()
    driver.save_screenshot(f'C:\work\screen_selen\screen_{str(now.hour)}_{str(now.minute)}_{str(now.microsecond)}.png')

