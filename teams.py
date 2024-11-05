from tkinter import *
from tkinter import messagebox as msg
import random
import os
t=Tk()
t.geometry("1080x1080")
t.title("팀 짜기 프로그램")
lastla=Label(t, text="학생 수 입력",font="맑은고딕 30")
lasten=Entry(t,font="맑은고딕 20")
lastla.pack()
lasten.pack()
memla=Label(t, text="모둠 학생 수",font="맑은고딕 30")
memen=Entry(t,font="맑은고딕 20")
memla.pack()
memen.pack()
numlist=[]
memlist=[]
def go():
	try:
		num=int(lasten.get())
		mem=int(memen.get())
		if num<mem:
			msg.showwarning("오류","모둠 학생 수가 학생 수보다 큽니다.")
			exit()
		for i in range(num):
			numlist.append(i)
		for i in range(num//mem):
			for i in range(mem):
				thing=random.choice(numlist)
				numlist.pop(thing)
				memlist.append(thing)
			file=open("team.txt","a")
			file.write(f"{i}모둠 : {memlist}\n")
		os.system("team.txt")
	except Exception as e:
		msg.showerror("오류",f"오류가 발생했습니다:\n{e}")
gobutton=Button(t,text="시작",font="맑은고딕 20",command=go)
gobutton.pack()
t.mainloop()
