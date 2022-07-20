import pyautogui,time
from tkinter import *
from tkinter import messagebox
import sys
from pynput.keyboard import Listener
def lu_click():
    def anonymous(key):
        if key=="Key.f12":
            sys.exit()
        print(key)
        with Listener(on_press=anonymous) as hacker:
            hacker.join()
        click=int(tbUser.get())
        delay=int(tbPass.get())
        print("start in...")
        for i in range(3,0,-1):
            print(i)
            time.sleep(1)
        x,y=pyautogui.position()
        for _ in range(click):
            time.sleep(delay)
            pyautogui.click(x,y)  
def ex_click():
    sys.exit()
nice=Tk()
nice.title("Nguyễn Hoàng Phúc")
nice.geometry("380x200")
menu = Menu(nice)
new_item = Menu(menu)
new_item.add_command(label='Exit',command=ex_click)
menu.add_cascade(label='File', menu=new_item)
nice.config(menu=menu)
lb2= Label(nice, text="Nhập số lần click:",font=("Arial",12),fg="red",)
lb2.place(x=5,y=19)
tbUser=Entry(nice,width=10,font=("consolas",12))
tbUser.place(x=150,y=22)
lb3= Label(nice, text="nhập delay sau mỗi lần click:" , font=("Arial",12),fg="red")
lb3.place(x=5,y=50)
tbPass=Entry(nice,width=10,font=("consolas",12))
tbPass.place(x=220,y=52)
lu=Button(nice , text="Bắt đầu",font=("consolas",14,"bold"),width=10,height=1,command=lu_click)
lu.place(x=100,y=90)
lbname2=Label(nice,text="2022-©-Nguyễn Hoàng Phúc",font=("Time New Roman",14),fg="blue")
lbname2.place(x=70,y=130)
nice.mainloop()