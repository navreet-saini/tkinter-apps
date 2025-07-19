import tkinter as tk
from PIL import Image,ImageTk

app=tk.Tk()
app.geometry("600x500")

img=Image.open("download.jpeg")
new_image=ImageTk.PhotoImage(img)

lbl=tk.Label(app,image=new_image,width=600)  #(width,height)  it can only crop tge image
lbl.pack()
app.mainloop()