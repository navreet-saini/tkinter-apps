import tkinter as tk
import datetime as date
def ca():
    
    xy=agee.get()
    age=int(xy)
    new_age=-age

    showinfo.config(text=f"you are {new_age} years old")
app=tk.Tk()
app.geometry("900x400")
app.title("Age Calculator")
app.config(background="#2ff7c9")
xyz=tk.Label(app,text="AgeCalculator",fg="green",bg="pink",font=("robort",40,"bold"))
xyz.pack(fill="x",ipadx=10)
agee=tk.Entry(app,font=("robort",40,"bold"),bg="#b1f0e1")
agee.pack(pady=30,ipadx=20)

btn=tk.Button(app,text="Check age",fg="#2ff7c9",bg="#12a106",font=("robort",25,"bold"),command=ca)
btn.pack(pady=10)

showinfo=tk.Label(app,text="",background="#2ff7c9",fg="blue",font=("robort",20,"bold")) 
showinfo.pack(pady=30)
app.mainloop()