from tkinter import *
import time
import subprocess
t=Tk()
t.geometry("500x160")
screen_width = t.winfo_screenwidth()
screen_height = t.winfo_screenheight()
win_width = 500
win_height = 160
x = screen_width - win_width - 50
y = screen_height - win_height - 120
t.geometry(f"{win_width}x{win_height}+{x}+{y}")
t.title("메뉴 및 시간")
def on_enter(event):
    t.geometry("500x250")
    #bu.pack()
def on_leave(event):
    t.geometry("500x160")
    #bu.pack_forget()
t.bind("<Enter>", on_enter)
t.bind("<Leave>", on_leave)
t.resizable(0,0)
t.configure(bg="black")
t.attributes("-alpha",0.75)
t.wm_attributes("-topmost", 1)
def timeupdate():
    nowt=time.strftime("%H:%M:%S")
    la.config(text=nowt)
    t.after(500,timeupdate)
la=Label(t,font="맑은고딕 80",fg="white",bg="black")
la.pack()
mainfr=Frame(t,bg="black")
mainfr.pack()
exitbu=Button(mainfr,text="종료",command=t.destroy,font="맑은고딕 20",bg="black",fg="white")
exitbu.grid(row=0,column=0)
info=Label(mainfr,text="    마우스를 올려 메뉴 보기",font="맑은고딕 20",bg="black",fg="white")
info.grid(row=0,column=1)
def numpick():
    subprocess.Popen(["number.exe"])
def stopwatch():
    subprocess.Popen(["timer.exe"])
def timeropen():
    subprocess.Popen(["timer1.exe"])
def teampick():
    subprocess.Popen(["teams.exe"])
def timeopen():
    subprocess.Popen(["nowtime.exe"])
def alertopen():
    subprocess.Popen(["alerting.exe"])
frame=Frame(t,bg="black")
frame.pack()
numbu=Button(frame, text="랜덤 번호 뽑기", font="맑은고딕 20", command=numpick,fg="white",bg="black")
numbu.grid(row=0,column=0)
timbu=Button(frame, text="스톱워치", font="맑은고딕 20", command=stopwatch,fg="white",bg="black")
timbu.grid(row=0,column=1)
tim2bu=Button(frame, text="타이머", font="맑은고딕 20", command=timeropen,fg="white",bg="black")
tim2bu.grid(row=0,column=2)
teambu=Button(frame,text="팀 짜기",font="맑은고딕 20",command=teampick,fg="white",bg="black")
teambu.grid(row=1,column=0)
clockbu=Button(frame,text="시계",font="맑은고딕 20",command=timeopen,fg="white",bg="black")
clockbu.grid(row=1,column=1)
alertbu=Button(frame,text="공지 입력",font="맑은고딕 20",command=alertopen,fg="white",bg="black")
alertbu.grid(row=1,column=2)
timeupdate()
t.mainloop()