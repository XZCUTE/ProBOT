from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time
import os
import tkinter as tk

w=Tk()
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))

w.overrideredirect(1) 

Frame(w, width= 427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text='ProBOT', fg='white', bg='#272727')
label1.configure(font=("Game of Squids", 32, "bold"))
label1.place(x=110,y=70)

label2=Label(w, text='Loading...', fg='white', bg='#272727')
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

image_a=ImageTk.PhotoImage(Image.open('images/c2.png'))
image_b=ImageTk.PhotoImage(Image.open('images/c1.png'))

for i in range(8): 
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.15)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.15)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.15)


    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.15)

w.destroy()

w=Tk()
w.geometry('800x600')
w.configure(bg='#262626')
w.resizable(0,0)
w.title('ProBOT')

def default_home():
    f2=Frame(w,width=800,height=600,bg='#262626')
    f2.place(x=0,y=0)
    l2=Label(f2,text='ProBOT',fg='white',bg='#262626')
    l2.config(font=('Game of squids',60))
    l2.place(x=250,y=220)
    
def Instruction():
    f1.destroy()
    instruction_img = Image.open("images/INSTRUCTION.png")
    img_width, img_height = instruction_img.size
    instruction_photo = ImageTk.PhotoImage(instruction_img)
    w.geometry(f"{img_width}x{img_height}")
    label = Label(w, image=instruction_photo)
    label.image = instruction_photo
    label.place(x=-2, y=0)
    toggle_win()

def RupertInfo():
    f1.destroy()
    instruction_img = Image.open("images/RUPERTINFO.png")
    img_width, img_height = instruction_img.size
    instruction_photo = ImageTk.PhotoImage(instruction_img)
    w.geometry(f"{img_width}x{img_height}")
    label = Label(w, image=instruction_photo)
    label.image = instruction_photo
    label.place(x=-2, y=0)
    toggle_win()

def MelodyInfo():
    f1.destroy()
    instruction_img = Image.open("images/MELODYINFO.png")
    img_width, img_height = instruction_img.size
    instruction_photo = ImageTk.PhotoImage(instruction_img)
    w.geometry(f"{img_width}x{img_height}")
    label = Label(w, image=instruction_photo)
    label.image = instruction_photo
    label.place(x=-2, y=0)
    toggle_win()
    
def RupertVA():
    f1.destroy()
    instruction_img = Image.open("images/RUPERTBUTTON.png")
    img_width, img_height = instruction_img.size
    instruction_photo = ImageTk.PhotoImage(instruction_img)
    w.geometry(f"{img_width}x{img_height}")
    label = Label(w, image=instruction_photo)
    label.image = instruction_photo
    label.place(x=-2, y=0)

    button_width, button_height = 120, 320
    button = Button(w, text="START", font=('Game of squids', 20), bg='#140605', fg='white', 
                    width=button_width//7, height=button_height//110, 
                    command=lambda: os.system("python ProBOT_Rupert.py"))
    button.place(relx=0.49, rely=.78, anchor=CENTER)
    toggle_win()

def MelodyVA():
    f1.destroy()
    instruction_img = Image.open("images/MELODYBUTTON.png")
    img_width, img_height = instruction_img.size
    instruction_photo = ImageTk.PhotoImage(instruction_img)
    w.geometry(f"{img_width}x{img_height}")
    label = Label(w, image=instruction_photo)
    label.image = instruction_photo
    label.place(x=-2, y=0)

    button_width, button_height = 120, 320
    button = Button(w, text="START", font=('Game of squids', 20), bg='#0E0325', fg='white', 
                    width=button_width//7, height=button_height//110, 
                    command=lambda: os.system("python ProBOT_Melody.py"))
    button.place(relx=0.49, rely=.75, anchor=CENTER)
    toggle_win()

def About():
    f1.destroy()
    instruction_img = Image.open("images/ABOUT PROBOT.png")
    img_width, img_height = instruction_img.size
    instruction_photo = ImageTk.PhotoImage(instruction_img)
    w.geometry(f"{img_width}x{img_height}")
    label = Label(w, image=instruction_photo)
    label.image = instruction_photo
    label.place(x=-2, y=0)
    toggle_win()

def toggle_win():
    global f1
    f1 = Frame(w, width=146, height=600, bg='#eba4e2')
    f1.place(x=0, y=0)

    def bttn(x, y, text, bcolor, fcolor, cmd):
        def on_enter(e):
            myButton1['background'] = bcolor 
            myButton1['foreground']= '#262626'  

        def on_leave(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#FFFFFF'

        myButton1 = Button(f1, text=text,
                        width=21,
                        height=2,
                        fg='#FFFFFF',
                        border=0,
                        bg=fcolor,
                        activeforeground='#FFFFFF',
                        activebackground=bcolor,            
                            command=cmd,
                            font=('Bebas neue', 14))
                      
        myButton1.bind("<Enter>", on_enter)
        myButton1.bind("<Leave>", on_leave)

        myButton1.place(x=x, y=y)


    bttn(-25, 50, 'INSTRUCTION', '#6a48a0', '#ea80fc', Instruction)
    bttn(-25, 123, 'RUPERT INFO', '#6a48a0', '#ea80fc', RupertInfo)
    bttn(-25, 196, 'MELODY INFO', '#6a48a0', '#ea80fc', MelodyInfo)
    bttn(-25, 269, 'RUPERT', '#6a48a0', '#ea80fc', RupertVA)
    bttn(-25, 342, 'MELODY', '#6a48a0', '#ea80fc', MelodyVA)
    bttn(-25, 415, 'ABOUT', '#6a48a0', '#ea80fc', About)
 

    def dele():
        f1.destroy()
        b2=Button(w,image=img1,
               command=toggle_win,
               border=0,
               bg='#262626',
               activebackground='#262626')
        b2.place(x=5,y=8)

    global img2
    img2 = ImageTk.PhotoImage(Image.open("images/close.png"))

    Button(f1,
           image=img2,
           border=1,
           command=dele,
           bg='#F650E1',
           activebackground='#F650E1').place(x=5,y=10)


default_home()

img1 = ImageTk.PhotoImage(Image.open("images/open.png"))

global b2
b2=Button(w,image=img1,
       command=toggle_win,
       border=1,
       bg='#262626',
       activebackground='#262626')
b2.place(x=5,y=8)

w.mainloop()

