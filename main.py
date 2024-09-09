from tkinter import *
import os
t = Tk()
t.geometry("1080x1080")
t.resizable(0,0)
t.title("School Tools")
def openprogram1():
    os.system(f"python number.py")
def openprogram2():
    os.system(f"python timer.py")
numbu=Button(t, text="랜덤 번호 뽑기", font="맑은고딕 20", command=openprogram1)
numbu.pack()
timbu=Button(t, text="스톱워치", font="맑은고딕 20", command=openprogram2)
timbu.pack()
t.mainloop()
