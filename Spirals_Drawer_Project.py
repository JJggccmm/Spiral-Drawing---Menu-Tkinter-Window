from tkinter import*
import tkinter.filedialog
from tkinter import font
from turtle import TurtleScreen, RawTurtle
import turtle
import random
import time

janela = Tk() 

janela.title("Spirals :")

Mistral24 = font.Font(family='Mistral', size=10)

# Some tests
#Arial24 = font.Font(family='Arial Black', size=10)#(｡◕‿◕｡)
#Cambria24 = font.Font(family='Cambria Math', size=10)
#espiral(60,10,2,20)
#espiral(60,10,2,10)
#espiral(60,10,2,5)
#espiral(60,10,2,45)
#espiral(60,10,2,60)
##espiral(100,100,100,15)
#espiral(60,30,10,90)
#espiral(100,30,10,360)
#espiral(100,30,2,180)
#espiral(400,30,10,270)
#espiral(60,30,10,120)

cv1 = Canvas(janela, width=590, height=660)
cv1.pack()
                
s1 = TurtleScreen(cv1)             

pri = RawTurtle(s1)

tat = RawTurtle(s1)
tat.shapesize(2)

val_01 = 0
val_02 = 0
val_03 = 0
val_04 = 0

flag = 0

s1.tracer(0,0)

pri.ht()

pri.penup()
pri.goto(-290,265)
pri.pendown()
pri.write("Spiral :",font=("Courier New", 48))

cores = ['lime','red','fuchsia','darkslategrey','turquoise','gray','black','mediumslateblue','navy','lightcyan','aqua','blue','orange','indigo','yellow','lawngreen','lavender','crimson','rosybrown','darkred']

def espiral(ns, ti, inc, ang):
    for i in range(ns):
        tat.forward(ti)
        tat.left(ang)
        ti = ti + inc

def drag_spiral(x,y):

    global val_01
    global val_02
    global val_03
    global val_04

    global flag

    global bt6
    
    if flag == 0:
    
        espiral(val_01,val_02,val_03,val_04)
        
        tat.penup()
        tat.goto(x,y)
        tat.pendown()
        s1.update()
        tat.speed(6)

    if flag == 1:

        val_01 = random.randint(-999,999)
        val_02 = random.randint(-999,999)
        val_03 = random.randint(-999,999)
        val_04 = random.randint(-360,360)

        espiral(val_01,val_02,val_03,val_04)

        bt6.destroy()

        bt6 = Button(janela,bg = cores[random.randint(0,19)],height = 1,width = 7, text= "∞", command=bt_click_6)
        bt6.place(x= 4, y = 537)

        tat.penup()
        tat.goto(x,y)
        tat.pendown()
        s1.update()
        tat.speed(6)

def take_spiral(x,y):
    
    tat.penup()
    tat.goto(x,y)
    tat.pendown()
    s1.update()
    tat.speed(6)

def bt_click():

    global val_01
    global val_02
    global val_03
    global val_04

    val_01 = int(ed1.get())
    val_02 = int(ed2.get())
    val_03 = int(ed3.get())
    val_04 = int(ed4.get())
    
def bt_click_3():

    global flag
    flag = 0

    tat.clear()

    global bt7

    bt7.destroy()

    bt7 = Button(janela,bg = cores[random.randint(0,19)],fg = cores[random.randint(0,19)],height = 1,width = 7, text= "RAmDoM", command=bt_click_5)
    bt7.place(x= 4, y = 563)

    global bt6

    bt6.destroy()

    bt6 = Button(janela,bg = 'white',height = 1,width = 7, text= "∞", command=bt_click_6)
    bt6.place(x= 4, y = 537)    
    
def bt_click_4():

    lis_cores = ['lime','red','fuchsia','darkslategrey','turquoise','gray','black','mediumslateblue','navy','lightcyan','aqua','blue','orange','indigo','yellow','lawngreen','lavender','crimson','rosybrown','darkred']
    tat.pencolor(lis_cores[random.randint(0,19)])
       
def bt_click_5():

    global val_01
    global val_02
    global val_03
    global val_04

    val_01 = random.randint(-999,999)
    val_02 = random.randint(-999,999)
    val_03 = random.randint(-999,999)
    val_04 = random.randint(-360,360)    

def bt_click_6():

    global flag
    flag = 1    
    
lb2 = Label(janela, text="                                         :                                           :                                           :                                          ", background='white')
lb2.place(x=66, y=620)

ed1= Entry(janela)
ed1.place(x= 66, y= 620)

ed2= Entry(janela)
ed2.place(x= 197, y= 620)

ed3= Entry(janela)
ed3.place(x= 329, y= 620)

ed4= Entry(janela)
ed4.place(x= 461, y= 620)

bt2 = Button(janela,bg = 'white',height = 1,width = 7, text= " ✍Apply ", command=bt_click)
bt2.place(x= 4, y = 616)

bt4 = Button(janela,bg = 'red',height = 1,width = 2, text= ">:(", command=bt_click_3)
bt4.place(x= 4, y = 511)

bt5 = Button(janela,bg = 'white',fg = 'magenta',height = 1,width = 10, text= "★Color~",font=Mistral24, command=bt_click_4)
bt5.place(x= 4, y = 588)

bt6 = Button(janela,bg = 'white',height = 1,width = 7, text= "∞", command=bt_click_6)
bt6.place(x= 4, y = 537)

bt7 = Button(janela,bg = cores[random.randint(0,19)],fg = cores[random.randint(0,19)],height = 1,width = 7, text= "RAmDoM", command=bt_click_5)
bt7.place(x= 4, y = 563)

s1.update()

tat.ondrag(drag_spiral,1)
tat.ondrag(take_spiral,3)

janela.geometry("590x660")
janela['bg'] = '#FFFFFF'
janela.mainloop()
