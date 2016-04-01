import Tkinter as tk
from handControl.hand import hand

def onKeyPress(event):
    if event.char == 'w':
        hand.move_axis(0,hand._axis[0].angle+5)
    if event.char == 's':
        hand.move_axis(0,hand._axis[0].angle-5)
    if event.char == 'a':
        hand.move_axis(1,hand._axis[1].angle+5)
    if event.char == 'd':
        hand.move_axis(1,hand._axis[1].angle-5)
    if event.char == '1':
        hand.move_axis(2,hand._axis[2].angle+5)
    if event.char == '2':
        hand.move_axis(2,hand._axis[2].angle-5)
    if event.char == 'q':
        hand.move_axis(3,hand._axis[3].angle+5)
    if event.char == 'e':
        hand.move_axis(3,hand._axis[3].angle-5)

def motion(event):
    hand.move([event.x/5,event.x/5,event.y/8,event.y/8])
    text.insert(0,"{},{}".format(event.x,event.y))

root = tk.Tk()
root.geometry('1440x900')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.bind('<Motion>', motion)
root.mainloop()