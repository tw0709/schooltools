from tkinter import *
import random
from tkinter import messagebox as msg
nl1=None
t=Tk()
t.geometry("720x480")
t.title("랜덤 번호 뽑기! - 설정")
la1=Label(t, text="시작 버튼을 눌러주세요!\n",font="맑은고딕 30")
la1.pack()
fnl=Label(t, text="첫번째 숫자 입력", font="맑은고딕 30")
fnl.pack()
fn=Entry(t,width=10, font="맑은고딕 20")
fn.pack()
enl=Label(t, text="마지막 숫자 입력",font="맑은고딕 30")
enl.pack()
en=Entry(t, font="맑은고딕 20",width=10)
en.pack()
def checkandgo():
    try:
        global intfn
        global inten
        global la1
        intfn = int(fn.get())
        inten = int(en.get())
        result=random.randint(intfn,inten)
        la1.configure(text=f"결과 : {result}\n")
    except Exception as e:
        msg.showerror("오류",f"오류가 발생하였습니다.\n{e}")
cb=Button(t, text="시작", font="맑은고딕 20",command=checkandgo)
cb.pack()
t.mainloop()