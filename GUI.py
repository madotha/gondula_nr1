from tkinter import *
import Main

def testGetXCords():
    return (69)


def testGetZCords():
    return (77)

def testStart():
    print("Tadaaa!")

def counter_label(label, readFunction):
    def count():
        label.config(text=readFunction())
        label.after(1000, count)

    count()


def start(readFunction):
    root = Tk()

    root.title("Gondula #1 Lastposition")
    xposLabel = Label(root, text="X-Position:", font="Helvetica 18 bold")
    xposLabel.pack()
    xpos_cords = Label(root, font="Helvetica 18")
    xpos_cords.pack()
    counter_label(xpos_cords, readFunction)
    zposLabel = Label(root, text="Z-Position:", font="Helvetica 18 bold")
    zposLabel.pack()
    zpos_cords = Label(root, text=testGetZCords(), font="Helvetica 18")
    zpos_cords.pack()
    start_button = Button(root, text="Start", command=testStart, font="Helvetica 18")
    start_button.pack()
    quit_button = Button(root, text="Quit", command=root.quit, font="Helvetica 18")
    quit_button.pack()

    root.mainloop()




