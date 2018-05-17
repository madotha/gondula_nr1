from tkinter import *
import FreedomCommunication as fc

root = Tk()

def testGetXCords():
    return (69)


def testGetZCords():
    return (77)

def testStart():
    print("Tadaaa!")

root.title("Gondula #1 Lastposition")

xposLabel = Label(root, text="X-Position:", font="Helvetica 18 bold").pack()
xpos_cords = Label(root, text=fc.getXCords(), font="Helvetica 18").pack()

zposLabel = Label(root, text="Z-Position:", font="Helvetica 18 bold").pack()
zpos_cords = Label(root, text=fc.getZCords(), font="Helvetica 18").pack()

start_button = Button(root, text="Start", command=fc.start(), font="Helvetica 18").pack()

quit_button = Button(root, text="Quit", command=root.quit, font="Helvetica 18").pack()


root.mainloop()
