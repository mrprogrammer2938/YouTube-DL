#!/usr/bin/python3
# This code write by Mr.nope
# YouTube Cloner
import os
import time
import sys
import platform
try:
    from pytube import YouTube
except ImportError:
    os.system("pip3 install pytube")
system = platform.uname()[0]
def title():
    if system == 'Linux':
        os.system("printf '\033]2;YouTube Cloner\a'")
    elif system == 'Windows':
        os.system("title YouTube Cloner")
    else:
        print("\nPlease, Run This Programm as Root!")
        sys.exit()
def cls():
    if system == 'Linux':
        os.system("clear")
    elif system == 'Windows':
        os.system("cls")
    else:
        print("\nPlease, Run This Programm as Root!")
        sys.exit()
def main():
    title()
    cls()
    print("Usage: Ctrl + C To Exit (～￣▽￣)～\n")
    link = input("\nEnter youtube link: ")
    time.sleep(1)
    run = YouTube(link)
    print(run)
    print("----------------------------------\n" + run)
    try1()
def try1():
    try_to = input("\npress Enter...")
    if try_to == '':
        main()
    else:
        main()
if __name__ == '__main__':
    try:
        if sys.version_info < (3,0):
            print("Python3 clone.py")
        else:
            main()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nExiting...")
        sys.exit()
