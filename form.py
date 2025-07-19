import tkinter as tk
import mysql.connector

conn=mysql.connector.connect(
    host="localhost",
    username="root",
    password="123456",
    database="internship"
)
cur=conn.cursor()

def abc():
    a=ent1.get()
    b=ent2.get()
    c=ent3.get()
    d=ent4.get()
    e=ent5.get("1.0",tk.END)
    
    cur.execute(f"insert into contact_us(full_name,age,phone_no,email,message) values ('{a}','{b}','{c}','{d}','{e}');")
    conn.commit()

    ent1.delete(0,tk.END)
    ent2.delete(0,tk.END)
    ent3.delete(0,tk.END)
    ent4.delete(0,tk.END)
    ent5.delete("1.0",tk.END)
app=tk.Tk()
app.geometry("700x600")
app.title("form page")
app.config(background="#16c4c4")

x=tk.Label(app,text="",background="#16c4c4")
x.grid(row=0,column=0,padx=55,pady=20)


lbl1=tk.Label(app,text="Full Name",font=("roburst",23,"bold"),background="#16c4c4")
lbl2=tk.Label(app,text="Age",font=("roburst",23,"bold"),background="#16c4c4")
lbl3=tk.Label(app,text="Phone No",font=("roburst",23,"bold"),background="#16c4c4")
lbl4=tk.Label(app,text="Email",font=("roburst",23,"bold"),background="#16c4c4")
lbl5=tk.Label(app,text="Message",font=("roburst",23,"bold"),background="#16c4c4")

lbl6=tk.Label(app,text=":",font=("roburst",23,"bold"),background="#16c4c4")
lbl7=tk.Label(app,text=":",font=("roburst",23,"bold"),background="#16c4c4")
lbl8=tk.Label(app,text=":",font=("roburst",23,"bold"),background="#16c4c4")
lbl9=tk.Label(app,text=":",font=("roburst",23,"bold"),background="#16c4c4")
lbl10=tk.Label(app,text=":",font=("roburst",23,"bold"),background="#16c4c4")


ent1=tk.Entry(app,font=("roburst",23),background="#dceff2")
ent2=tk.Entry(app,font=("roburst",23),background="#dceff2")
ent3=tk.Entry(app,font=("roburst",23),background="#dceff2")
ent4=tk.Entry(app,font=("roburst",23),background="#dceff2")
ent5=tk.Text(app,font=("roburst",23),height=4,width=20,background="#dceff2")


lbl1.grid(row=1,column=1)
lbl2.grid(row=2,column=1,pady=15)
lbl3.grid(row=3,column=1)
lbl4.grid(row=4,column=1,pady=15)
lbl5.grid(row=5,column=1)

lbl6.grid(row=1,column=2)
lbl7.grid(row=2,column=2)
lbl8.grid(row=3,column=2)
lbl9.grid(row=4,column=2)
lbl10.grid(row=5,column=2)


ent1.grid(row=1,column=3)
ent2.grid(row=2,column=3)
ent3.grid(row=3,column=3)
ent4.grid(row=4,column=3)
ent5.grid(row=5,column=3)


btn=tk.Button(app,text="submit",font=("roburst",23,"bold"),background="blue",fg="white",command=abc)
btn.grid(row=6,column=3,pady=20)

app.mainloop()