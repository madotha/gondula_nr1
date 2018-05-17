from tkinter import *

root = Tk()

def testGetXCords(self):
    return (69)


def testGetZCords(self):
    return (77)

def testStart(self):
    print("Tadaaa!")
    return ("Starte die Gondula!")

root.title("Gondula #1 Lastposition")

xposLabel = Label(root, text="X-Position:", font="Helvetica 18 bold").pack()
xpos_cords = Label(root, text=testGetXCords(self=root), font="Helvetica 18").pack()

zposLabel = Label(root, text="Z-Position:", font="Helvetica 18 bold").pack()
zpos_cords = Label(root, text=testGetZCords(self=root), font="Helvetica 18").pack()

start_button = Button(root, text="Start", command=testStart(self=root), font="Helvetica 18").pack()

quit_button = Button(root, text="Quit", command=root.quit, font="Helvetica 18").pack()


root.mainloop()
