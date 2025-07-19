import tkinter as tk

def add():
    a=name.get()
    zx=int(a)
    b=name1.get()
    zy=int(b)
    sum=zy+zx
    print(sum)
    showinfo.config(text=f"the total of {a} and {b} is:{sum}")

def sub():
    a=name.get()
    zx=int(a)
    b=name1.get()
    zy=int(b)
    sub=zx-zy
    print(sub)
    showinfo.config(text=f"the subtraction of {a} and {b} is:{sub}")

def mul():
    a=name.get()
    zx=int(a)
    b=name1.get()
    zy=int(b)
    mul=zx*zy
    print(mul)
    showinfo.config(text=f"the multipliction of {a} and {b} is:{mul}")

app=tk.Tk()
app.geometry("900x400")
app.title("practice")
app.config(background="pink")

lbl=tk.Label(app,text="calculator",font=("Times new roman",30,"underline"),bg="pink",fg="blue")
lbl.grid(row=0,column=2)

lbl1=tk.Label(app,text="enter first no:",font=("Times new roman",20,"bold"),bg="pink",fg="blue")
lbl1.grid(row=1,column=1)

name=tk.Entry(app,font=("robort",20,"italic"),fg="blue")
name.grid()
lbl2=tk.Label(app,text="enter your 2nd no:",font=("Times new roman",20,"bold"),bg="pink",fg="blue")
lbl2.grid()
name1=tk.Entry(app,font=("robort",20,"italic"),fg="blue")
name1.grid(ipadx=20)


btn=tk.Button(app,text="addition",font=("robort",20,"bold"),foreground="blue" ,background="red",command=add)
btn.grid(pady=10,ipadx=10)
btn1=tk.Button(app,text="subtraction",font=("robort",20,"bold"),foreground="blue" ,background="red",command=sub)
btn1.grid(pady=30,ipadx=10)
btn2=tk.Button(app,text="multiplication",font=("robort",20,"bold"),foreground="blue" ,background="red",command=mul)
btn2.grid(pady=10,ipadx=10)

showinfo=tk.Label(app,text="",background="pink",fg="blue",font=("robort",20,"bold")) 
showinfo.grid(pady=30)





app.mainloop()