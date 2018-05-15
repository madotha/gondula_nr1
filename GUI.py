from tkinter import *
import FreedomCommunication

class GondulaGUI:

    def __init__(self, master):
        freecom = FreedomCommunication

        self.master = master
        master.title("Gondula #1 Lastposition")

        self.xpos = Label(master, text="X-Position:").pack()

        self.ypos = Label(master, text="Y-Position:").pack()

        self.connect_button = Button(master, text="Connect", command=freecom.FreedomCommunications.__init__(freecom)).pack()

        self.start_button = Button(master, text="Start", command=freecom.FreedomCommunications.start(freecom)).pack()

        self.quit_button = Button(master, text="Quit", command=master.quit).pack()

root = Tk()
my_gui = GondulaGUI(root)
root.mainloop()