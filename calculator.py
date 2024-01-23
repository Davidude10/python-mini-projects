from tkinter import *
a=Tk()
a.title("Simple Calculator")

clicking=Label(text="CLICKED     :")
clicking.place(x=20,y=80)
label2=Label(text="RESULT       :")
label2.place(x=20,y=120)
label3 = Label(a, text="",background="white")
label3.place(x=100,y=120)
label4=Label(text="SIMPLE CALCULATOR",background="Red",foreground="blue")
label4.place(x=180,y=10)
global b
b=""
def button1():
    global b
    b= b + '1'
    label.config(text=b)
def button2():
    global b
    b= b + '2'
    label.config(text=b)
def button3():
    global b
    b= b + '3'
    label.config(text=b)
def button4():
    global b
    b= b + '4'
    label.config(text=b)
def button5():
    global b
    b= b + '5'
    label.config(text=b)
def button6():
    global b
    b= b + '6'
    label.config(text=b)
def button7():
    global b
    b= b + '7'
    label.config(text=b)
def button8():
    global b
    b= b + '8'
    label.config(text=b)
def button9():
    global b
    b= b + '9'
    label.config(text=b)
def button0():
    global b
    b= b + '0'
    label.config(text=b)
def buttonplus():
    global b
    b= b + '+'
    label.config(text=b)
def buttonminus():
    global b
    b= b + '-'
    label.config(text=b)
def buttonmulti():
    global b
    b= b + '*'
    label.config(text=b)
def buttondivide():
    global b
    b= b + '/'
    label.config(text=b)
def buttonrem():
    global b
    b= b + '%'
    label.config(text=b)
def buttonbrac1():
    global b
    b= b + '('
    label.config(text=b)
def buttonbrac2():
    global b
    b= b + ')'
    label.config(text=b)
def buttonclr():
    global b
    b= " "
    label.config(text=b)
def buttonequal():
    global b
    try:
        result=eval(b)
        label3.config(text="" + str(result))
    except Exception as e:
        label3.config(text="Error: " + str(e))

seven=Button(a,text="7" ,pady=10,width=10,command=button7,background="green")
seven.place(x=30,y=200)
eight=Button(a,text="8" ,pady=10,width=10,command=button8,background="green")
eight.place(x=120,y=200)
nine=Button(a,text="9" ,pady=10,width=10,command=button9,background="green")
nine.place(x=210,y=200)

plus=Button(a,text="+" ,pady=10,width=6,command=buttonplus,background="light blue")
plus.place(x=320,y=200)
minus=Button(a,text="-" ,pady=10,width=6,command=buttonminus,background="light blue")
minus.place(x=390,y=200)

four=Button(a,text="4" ,pady=10,width=10,command=button4,background="green")
four.place(x=30,y=250)
five=Button(a,text="5" ,pady=10,width=10,command=button5,background="green")
five.place(x=120,y=250)
six=Button(a,text="6" ,pady=10,width=10,command=button6,background="green")
six.place(x=210,y=250)

multi=Button(a,text="x" ,pady=10,width=6,command=buttonmulti,background="light blue")
multi.place(x=320,y=250)
divide=Button(a,text="÷" ,pady=10,width=6,command=buttondivide,background="light blue")
divide.place(x=390,y=250)

one=Button(a,text="1" ,pady=10,width=10,command=button1,background="green")
one.place(x=30,y=300)
two=Button(a,text="2" ,pady=10,width=10,command=button2,background="green")
two.place(x=120,y=300)
three=Button(a,text="3" ,pady=10,width=10,command=button3,background="green")
three.place(x=210,y=300)

brac1=Button(a,text="(" ,pady=10,width=10,command=buttonbrac1,background="light green")
brac1.place(x=30,y=350)
zero=Button(a,text="0" ,pady=10,width=10,command=button0,background="green")
zero.place(x=120,y=350)
brac2=Button(a,text=")" ,pady=10,width=10,command=buttonbrac2,background="light green")
brac2.place(x=210,y=350)

rem=Button(a,text="%" ,pady=10,width=6,command=buttonrem,background="light blue")
rem.place(x=320,y=300)
clr=Button(a,text="C" ,pady=10,width=6,command=buttonclr,background="brown")
clr.place(x=320,y=350)
equal=Button(a,text="=" ,pady=20,width=6,height=3,command=buttonequal,background="yellow")
equal.place(x=390,y=300)

label = Label(a, text="")
label.place(x=100,y=80)
label.config(text=b)

a.geometry("500x480")
a.mainloop()




