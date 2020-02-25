import os,sys,time,random
from progressbar import *

def cut(str):
    return str.strip(" ")

def welcome(appname="",author=""):
    print("Welcome to use "+appname+"!")
    print("This app is made by "+author+".")

def Bye():
    pass

def split():
    print("--------")

def changescrn():
    os.system("clear")

def scs():
    split()
    changescrn()
    split()

def wait(ts=1):
    time.sleep(ts)

def waitForUser():
    input("Press Return to continue...")
    
def load(times=5):
    bar=ProgressBar()
    print("Loading now...")
    print("Please wait.")
    for i in bar(range(times)):
        time.sleep(random.randint(0,3))
