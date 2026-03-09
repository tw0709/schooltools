from tkinter import *
t=Tk()
t.geometry("500x500")
t.title("공지")
t.configure(bg="black")
t.attributes("-alpha", 0.75)
t.wm_attributes("-topmost", 1)
size=20
def select(event):
    value=int(scale.get())
    en.config(font=f"맑은고딕 {value}")
scale = Scale(t,label="글자 크기", variable=size, orient="horizontal", showvalue=True, tickinterval=10,from_=10, to=100, length=200, command=select,bg="black",fg="white")
scale.pack(fill=BOTH)
scale.set(20)
en=Text(t,wrap=WORD,font=f"맑은고딕 {size}",fg="white",bg="black")
en.pack(fill=BOTH,expand=True)
t.mainloop()