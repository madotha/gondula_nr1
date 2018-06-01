from tkinter import *


def testCords():
    return 42, 88


def testStart():
    print("Tadaaa!")


def cord_loop(xlabel, zlabel, readFunction):
    def count():
        x, z = readFunction()
        xlabel.config(text=str(x))
        zlabel.config(text=str(z))
        xlabel.after(200, count)

    count()


def start(startmethod, stopmethod, cordsmethod):
    fonttext ="Helvetica 80"
    fontbutton = "Helvetica 36"
    buttonsize = {'heigh': 2, 'width': 10}

    # Create Windows
    root = Tk()
    root.attributes("-fullscreen", True)
    root.title("Gondula #1 Lastposition")

    # Prepare Frames for Labels
    topframe = Frame(root)
    topframe.pack(side=TOP)
    middleframe = Frame(root)
    middleframe.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=BOTTOM)

    # Topframe Labels
    xposLabel = Label(topframe, text="X-Pos:", font=fonttext)
    xposLabel.pack(side=LEFT)
    xpos_cords = Label(topframe, font=fonttext)
    xpos_cords.pack(side=RIGHT)

    # Middleframe Labels
    zposLabel = Label(middleframe, text="Z-Pos:", font=fonttext)
    zposLabel.pack(side=LEFT)
    zpos_cords = Label(middleframe, font=fonttext)
    zpos_cords.pack()

    # Commands for Buttons
    def bstart():
        startmethod()
        start_button.config(text="Stop", command=bstop)

    def bstop():
        stopmethod()
        start_button.config(text="Start", command=bstart)

    def bquit():
        stopmethod()
        root.destroy()

    # Bottomframe for Buttons
    start_button = Button(bottomframe, text="Start", command=bstart, font=fontbutton, **buttonsize)
    start_button.pack(side=LEFT, padx=5, pady=5)
    quit_button = Button(bottomframe, text="Exit", command=bquit, font=fontbutton, **buttonsize)
    quit_button.pack(side=RIGHT, padx=5, pady=5)

    # Updatemethod for Cords
    cord_loop(xpos_cords, zpos_cords, cordsmethod)

    root.mainloop()


if __name__ == '__main__':
    start(testStart, testStart, testCords)
