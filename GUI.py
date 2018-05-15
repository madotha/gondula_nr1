from tkinter import *
import FreedomCommunication

class GondulaGUI:

    def __init__(self, master):
        freecom = FreedomCommunication
        #conn = freecom.FreedomCommunications.__init__(freecom)

        self.master = master
        master.title("Gondula #1 Lastposition")

        self.xposLabel = Label(master, text="X-Position:", font="Helvetica 18 bold").pack()
        self.xpos = Label(master, text=self.testGetXCords(), font="Helvetica 18").pack()
        #self.xpos = Label(master, text=freecom.FreedomCommunications.getXCords(freecom), font="Helvetica 18").pack()

        self.zposLabel = Label(master, text="Z-Position:", font="Helvetica 18 bold").pack()
        self.zos = Label(master, text=self.testGetZCords(), font="Helvetica 18").pack()
        #self.ypos = Label(master, text=freecom.FreedomCommunications.getZCords(freecom), font="Helvetica 18").pack()

        self.start_button = Button(master, text="Start", command=self.testStart(), font="Helvetica 18").pack()
        #self.start_button = Button(master, text="Start", command=freecom.FreedomCommunications.start(freecom), font="Helvetica 18").pack()

        self.quit_button = Button(master, text="Quit", command=master.quit, font="Helvetica 18").pack()

    def testGetXCords(self):
        return(88)

    def testGetZCords(self):
        return(77)

    def testStart(self):
        return("Starte die Gondula!")

root = Tk()
my_gui = GondulaGUI(root)
root.mainloop()