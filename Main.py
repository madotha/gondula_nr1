import threading
import FreedomCommunication
import cap

class Main:

    freedom_communication = FreedomCommunication
    cap = cap

    def __init__(self):
        print("Main init")

    def start(self):
        print("Main_start")
        self.freedom_communication.FreedomCommunications.__init__(FreedomCommunication)
        self.cap.ImageProcessor.start_detecting(self, target_found)

if __name__ == "__main__":
    Main()
