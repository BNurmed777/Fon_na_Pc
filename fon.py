import ctypes
import os
import datetime
import time


def fon(code):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(os.getcwd(), "C:/Python/wallpapers", f"{code}.jpg"), 0)


def time_and_wallpaper():
    time = datetime.datetime.now().hour
    if time >= 5 and time < 6:
        fon("1")
    elif time >= 6 and time < 9:
        fon("2")
    elif time >= 9 and time < 12:
        fon("3")
    elif time >= 12 and time < 16:
        fon("4")
    elif time >= 16 and time < 18:
        fon("5")
    elif time >= 18 and time < 20:
        fon("6")
    else:
        fon("7")


if __name__ == '__main__':
    time_and_wallpaper()
    while True:
        time_and_wallpaper()
        time.sleep(5)
