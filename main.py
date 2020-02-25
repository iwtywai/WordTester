import defines,os,sys,time,random

class Word:
    def __init__(self,wordName="NaN",def="NaN"):
        self.wordName=wordName
        self.def=def
    def showMeaning():
        print(self.def)
    def showWordSelf():
        print(self.wordName)
    def change(wordName="NaN",def="NaN"):
        self.wordName=wordName
        self.def=def

wordOperating=Word()

split()
welcome("WordRecite","iwtywai")
split()
wait(1)
scs()

load(random.randint(1,15))
changescrn()

def passInCheck():
    return True
    ##pass

def Add():
    pass

def Edit():
    pass

def Del():
    pass

def Test():
    pass

while True:
    split()
    print("What is your choice?")
    print("0.Exit")
    print("1.Add word")
    print("2.Edit word")
    print("3.Delete word")
    print("4.Custom Test")
    choice=cut(input(" --> "))
    if choice=="0":
        Bye()
    elif choice=="1":
        Add()
    elif choice=="2":
        Edit()
    elif choice=="3":
        Del()
    elif choice=="4":
        Test()
    waitForUser()
    changescrn()
