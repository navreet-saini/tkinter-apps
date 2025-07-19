import tkinter as tk
app=tk.Tk()

app.geometry("900x300")
app.title("My first tkinter app")
app.config(background="pink")



lbl =tk.Label(app,text="Hello world",font=("robort",43,"bold"),foreground="blue" ,background="red")  #fg=foreground we use
lbl.pack(fill="x",pady=20,padx=20,ipady=5,side="top")

inpx=tk.Entry(app,font=("robort",43,"italic"),fg="blue")
inpx.pack()

btn=tk.Button(app,text="ClickMe",font=("robort",20,"bold"),foreground="blue" ,background="red")
btn.pack(pady=30,ipadx=40)




app.mainloop()