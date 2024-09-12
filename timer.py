from tkinter import *
import time
startt=0
nowt=0
resultt=0
timestarted = False
t=Tk()
t.geometry("720x480")
t.title("스톱워치")
la1=Label(t,text="시작 버튼을 눌러주세요!",font="맑은고딕 30")
la1.pack()
def update_timer():
    global nowt, resultt
    if timestarted:
        nowt = time.time()
        resultt = nowt - startt
        la1.configure(text=f"{resultt:.3f}초")
        t.after(1, update_timer)

def timerstart():
    global timestarted, startt
    startt = time.time()
    timestarted = True
    update_timer()

def timerstop():
    global timestarted
    timestarted = False
bu1=Button(t, text="시작", font="맑은고딕 20",command=timerstart)
bu1.pack()
bu2=Button(t, text="정지", font="맑은고딕 20", command=timerstop)
bu2.pack()
t.mainloop()