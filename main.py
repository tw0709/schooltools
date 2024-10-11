from tkinter import *
import sys
import subprocess
t = Tk()
t.geometry("1080x1080")
t.resizable(0,0)
t.title("School Tools")
la1=Label(t,text="원하는 기능을 선택해주세요!",font="맑은고딕 30")
la1.pack()
def openprogram1():
    subprocess.Popen(["python","number.py"])
    sys.exit()
def openprogram2():
    subprocess.Popen(["python","timer.py"])
    sys.exit()
def openprogram3():
    subprocess.Popen(["python","timer1.py"])
    sys.exit()
def openprogram4():
    subprocess.Popen(["python","teams.py"])
    sys.exit()
numbu=Button(t, text="랜덤 번호 뽑기", font="맑은고딕 20", command=openprogram1)
numbu.pack()
timbu=Button(t, text="스톱워치", font="맑은고딕 20", command=openprogram2)
timbu.pack()
tim2bu=Button(t, text="타이머", font="맑은고딕 20", command=openprogram3)
tim2bu.pack()
teambu=Button(t,text="팀 짜기",font="맑은고딕 20",command=openprogram4)
teambu.pack()
t.mainloop()
