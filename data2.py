from tkinter import *
root=Tk()
def get_x(event):
    global lasx ,lasy
    lasx=event.x
    lasy=event.y

def draw_s(event):
    global  lasx ,lasy
    canvas.create_line((lasx,lasy,event.x,event.y),fill="red",width=2)
    lasx =event.x
    lasy =event.y
canvas=Canvas(root,bg="black")
root.geometry("400x400")
canvas.pack(anchor='nw', fill='both',expand=1)
canvas.bind('<Button-1>',get_x)
canvas.bind('B1-Motion',draw_s)


root.mainloop()


