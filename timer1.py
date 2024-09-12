from tkinter import *
from tkinter import messagebox as msg
import time
import pygame
t=Tk()
t.geometry("720x480")
t.title("타이머")
pygame.mixer.init()
alarm_sound = pygame.mixer.Sound("알람소리.mp3")
mla=Label(t, text="시간을 입력하고\n시작 버튼을 눌러주세요!",font="맑은고딕 30")
mla.pack()
minentry=Entry(t,font="맑은고딕 20",width=10)
minentry.pack()
minla=Label(t,text="분",font="맑은고딕 20")
minla.pack()
secentry=Entry(t,font="맑은고딕 20",width=10)
secentry.pack()
secla=Label(t,text="초",font="맑은고딕 20")
secla.pack()
def update_timer(realsec):
    if realsec > 0:
        leftmin = realsec // 60
        leftsec = realsec % 60
        mla.configure(text=f"{leftmin}분 {leftsec}초 남음")
        t.after(1000, update_timer, realsec - 1)  # 1초 후에 다시 호출
    else:
        mla.configure(text="타이머 종료됨.\n시간을 입력하고\n시작 버튼을 눌러주세요!")
        pygame.mixer.Sound.play(alarm_sound)
def checkandgo():
    try:
        min = minentry.get()
        if min == "":
            min = 0
        else:
            min = int(min)

        sec = secentry.get()
        if sec == "":
            sec = 0
        else:
            sec = int(sec)

        realsec = min * 60 + sec

        if realsec > 0:
            update_timer(realsec)
        else:
            msg.showwarning("오류", "타이머 시간이 0초 이하입니다.")
    except Exception as e:
        msg.showerror("오류", f"오류가 발생하였습니다.\n{e}")
startbu=Button(t, text="시작",font="맑은고딕 20",command=checkandgo)
startbu.pack()
t.mainloop()