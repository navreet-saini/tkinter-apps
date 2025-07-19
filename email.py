import tkinter as tk
import regex as re
def abc():
    zx=name.get()
    ptr=r"[a-z]+[0-9]*[a-z]*@[a-z]{5}[.][a-z]{3}"
    xyz=re.match(ptr,zx)
    if xyz:
       showinfo.config(text=f"you registered as {zx}")
    else:
        showinfo.config(text="invalid")

    
app=tk.Tk()
app.geometry("900x400")
app.title("practice")
app.config(background="pink")

lbl=tk.Label(app,text="Hello World",font=("Times new roman",20,"bold"),bg="pink",fg="blue")
lbl.pack(pady=20,ipady=10)

lbl1=tk.Label(app,text="enter your email:",font=("Times new roman",20,"bold"),bg="pink",fg="blue")
lbl1.pack()

name=tk.Entry(app,font=("robort",20,"italic"),fg="blue")
name.pack(ipadx=20)



btn=tk.Button(app,text="ClickMe",font=("robort",20,"bold"),foreground="blue" ,background="red",command=abc)
btn.pack(pady=30,ipadx=40)

showinfo=tk.Label(app,text="",background="pink",fg="blue",font=("robort",20,"bold")) 
showinfo.pack(pady=30)





app.mainloop()