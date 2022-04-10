from tkinter import *
root=Tk()
root.geometry("400x400")

var=IntVar()
def sel():
    selection ="you are selsct the option" +str(var.get())
    label.config(text=selection)
R1 =Radiobutton(root,text="option 1",variable=var,value=1,command=sel)

R1.pack()

R2 =Radiobutton(root,text="option 2",variable=var,value=2,command=sel)
R2.pack()

R3 =Radiobutton(root,text="option 3",variable=var,value=3,command=sel)
R3.pack()

label = Label(root)
label.pack()
root.mainloop()