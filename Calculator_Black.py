from tkinter import *
window=Tk()
window.geometry("354x460")
window.configure(bg="black")
label=Label(window,text="Calculator",width=35,bg="black",font=("Bernard MT Condensed",30,"bold"),fg="white")
window.title("calc")
label.pack(side=TOP)


textin=StringVar()
operator=""

def clckbtn(number):
    global operator
    operator=operator+str(number)
    textin.set(operator)

def eqlbtn():
    global operator
    add=str(eval(operator))
    textin.set(add)
    operator=""

def eqlbtn():
    global operator
    sub=str(eval(operator))
    textin.set(sub)
    operator=""

def eqlbtn():
    global operator
    mul=str(eval(operator))
    textin.set(mul)
    operator=""  

def eqlbtn():
    global operator
    div=str(eval(operator))
    textin.set(div)
    operator=""
  


def clrbtn():
    textin.set("")

#ALigNMent
wintext=Entry(window,font=("Bernard MT Condensed",12,"bold"),text=textin,width=40,bd=8,bg="light blue")
wintext.pack()

btn1=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn(1),text="1")
btn1.place(x=10,y=100)


btn2=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn(2),text="2")
btn2.place(x=75,y=100)

btn3=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn(3),text="3")
btn3.place(x=140,y=100)

btn4=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn(4),text="4")
btn4.place(x=10,y=175)

btn5=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn(5),text="5")
btn5.place(x=75,y=175)

btn6=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn(6),text="6")
btn6.place(x=140,y=175)

btn7=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn(7),text="7")
btn7.place(x=10,y=250)

btn8=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn(8),text="8")
btn8.place(x=75,y=250)


btn9=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn(9),text="9")
btn9.place(x=140,y=250)

btn0=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn(0),text="0")
btn0.place(x=75,y=325)

btndot=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn("."),text=".")
btndot.place(x=10,y=325)

btnadd=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn("+"),text="+")
btnadd.place(x=205,y=100)

btnsub=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn("-"),text="-",width=2)
btnsub.place(x=205,y=175)

btnmul=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn("*"),text="*")
btnmul.place(x=205,y=250)

btndiv=Button(window,padx=14,pady=14,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=lambda:clckbtn("/"),text="/")
btndiv.place(x=140,y=325)


btnclr=Button(window,padx=14,pady=126,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=clrbtn,text="CE")
btnclr.place(x=270,y=100)

btneql=Button(window,padx=147,pady=5,bg="grey",font=("Bernard MT Condensed",16,"bold"),fg="white",command=eqlbtn,text="=")
btneql.place(x=10,y=400)

window.mainloop()

