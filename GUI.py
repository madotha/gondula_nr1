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
        xlabel.after(1000, count)

    count()


def start(startmethod, cordsmethod):
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
    xposLabel = Label(topframe, text="X-Position:", font="Helvetica 18 bold")
    xposLabel.pack(side=LEFT)
    xpos_cords = Label(topframe, font="Helvetica 18")
    xpos_cords.pack(side=RIGHT)

    # Middleframe Labels
    zposLabel = Label(middleframe, text="Z-Position:", font="Helvetica 18 bold")
    zposLabel.pack(side=LEFT)
    zpos_cords = Label(middleframe, font="Helvetica 18")
    zpos_cords.pack()

    # Bottomframe for Buttons
    start_button = Button(bottomframe, text="Start", command=startmethod(), font="Helvetica 18")
    start_button.pack(side=LEFT, padx=5, pady=5)
    quit_button = Button(bottomframe, text="Quit", command=root.quit, font="Helvetica 18")
    quit_button.pack(side=RIGHT, padx=5, pady=5)

    # Updatemethod for Cords
    cord_loop(xpos_cords, zpos_cords, cordsmethod)

    root.mainloop()


if __name__ == '__main__':
    start(testStart, testCords)
