import tkinter as tk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

con=mysql.connector.connect(
    host="localhost",
    port=3306,
    username="root",
    password="123456",
    database="internship"
)

cur=con.cursor()
def abc():
    full_name=ent1.get()
    email=ent2.get()
    qual=ent3.get()
    phone=ent4.get()
    course=ent5.get()
    msg=ent6.get("1.0",tk.END)
    
    cur.execute(f"insert into users(full_name,email_add,qualification,phone_no,course_name,message) values ('{full_name}','{email}','{qual}','{phone}','{course}','{msg}');")

    con.commit()

    messagebox.showinfo("Data Saved", "Your Message saved sucessfuly in Database..")

    ent1.delete(0, tk.END)
    ent2.delete(0, tk.END)
    ent3.delete(0, tk.END)
    ent4.delete(0, tk.END)
    ent5.delete(0, tk.END)
    ent6.delete("1.0", tk.END)

    showinfo.config(text=f"Dear {full_name},You succesfully enrolled in {course}")


app=tk.Tk()
app.geometry("1100x680")
app.title("my_contact form")
app.config(background="#f2eb5a")


frame1=tk.Frame(app,relief="raised",borderwidth=15,background="#f2eb5a")
frame1.pack(fill="x")

cont_lbl=tk.Label(frame1,text="--Course Registration Form--",font=("robort",38,"bold"),bg="#f2eb5a")
cont_lbl.pack(fill="x",pady=15)

frame2=tk.Frame(app)
frame2.pack(fill="x")

show=Image.open("a.jpg")
new_img=ImageTk.PhotoImage(show)

img=tk.Label(frame2, image=new_img,height=120,width=1500)
img.pack()

frame3=tk.Frame(app,relief="sunken",borderwidth=10,bg="#95edf0")
frame3.pack(fill="x",pady=10)

frame4=tk.Frame(frame3,bg="#95edf0")
frame4.grid(row=0,column=0)

frame5=tk.Frame(frame3,bg="#95edf0")
frame5.grid(row=0,column=1)

lbl0=tk.Label(frame4,text="",font=("roburst",18,"bold"),bg="#95edf0")
lbl1=tk.Label(frame4,text="Full Name",font=("roburst",18,"bold"),bg="#95edf0")
lbl2=tk.Label(frame4,text="Email",font=("roburst",18,"bold"),bg="#95edf0")
qual=tk.Label(frame4,text="Qualification",font=("roburst",18,"bold"),bg="#95edf0")

lbl3=tk.Label(frame5,text="",font=("roburst",18,"bold"),bg="#95edf0")
lbl4=tk.Label(frame5,text="Phone_no",font=("roburst",18,"bold"),bg="#95edf0")
course=tk.Label(frame5,text="Course_Name",font=("roburst",18,"bold"),bg="#95edf0")
lbl5=tk.Label(frame5,text="Message",font=("roburst",18,"bold"),bg="#95edf0")




semi1=tk.Label(frame4,text=":",font=("roburst",18,"bold"),bg="#95edf0")
semi2=tk.Label(frame4,text=":",font=("roburst",18,"bold"),bg="#95edf0")
semi3=tk.Label(frame4,text=":",font=("roburst",18,"bold"),bg="#95edf0")
semi4=tk.Label(frame5,text=":",font=("roburst",18,"bold"),bg="#95edf0")
semi5=tk.Label(frame5,text=":",font=("roburst",18,"bold"),bg="#95edf0")
semi6=tk.Label(frame5,text=":",font=("roburst",18,"bold"),bg="#95edf0")

lbl0.grid(row=0,column=0,padx=20)
lbl1.grid(row=1,column=1)
lbl2.grid(row=2,column=1,pady=20)
qual.grid(row=3,column=1)

lbl3.grid(row=0,column=0,padx=45)
lbl4.grid(row=1,column=1)
course.grid(row=2,column=1,pady=20)
lbl5.grid(row=3,column=1)

semi1.grid(row=1,column=2)
semi2.grid(row=2,column=2)
semi3.grid(row=3,column=2)
semi4.grid(row=1,column=2)
semi5.grid(row=2,column=2)
semi6.grid(row=3,column=2)


ent1=tk.Entry(frame4,font=("roburst",20))
ent2=tk.Entry(frame4,font=("roburst",20))
ent3=tk.Entry(frame4,font=("roburst",20))
ent4=tk.Entry(frame5,font=("roburst",20))
ent5=tk.Entry(frame5,font=("roburst",20))
ent6=tk.Text(frame5,font=("roburst",20),width=20,height=2)

ent1.grid(row=1,column=3)
ent2.grid(row=2,column=3)
ent3.grid(row=3,column=3)
ent4.grid(row=1,column=3)
ent5.grid(row=2,column=3)
ent6.grid(row=3,column=3)


frame6=tk.Frame(app,bg="#f2eb5a")
frame6.pack(fill="x")

btn=tk.Button(frame6,text="Submit",font=("roburst",20,"bold"),bg="red",fg="white",command=abc)
btn.pack(pady=15)

showinfo=tk.Label(frame6,text="",font=("roburst",20,"bold"),fg="blue",bg="#f2eb5a")
showinfo.pack(fill="x")

app.mainloop()