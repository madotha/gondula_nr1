from threading import Thread
import FreedomCommunication as fc
# import fc_fake_test as fc
import cap
import time
import GUI

BLOCK_STARTPOS = 65
block_x_pos = BLOCK_STARTPOS
block_z_pos = 0
target_reached = False
running = False


def main():
    # Open Serialinterface
    time.sleep(1)
    fc.open()
    GUI.start(startmethod=start_gondula, stopmethod=stop_gondula, cordsmethod=get_cords)


def start_gondula():
    global running
    running = True
    fc.start()
    t = Thread(target=readCordsFromSerial, args=())
    t.start()


def stop_gondula():
    global running
    running = False
    fc.stop()
    cap.stop()


def readCordsFromSerial():
    print("Start readingloop x and z from mc")
    global block_x_pos
    global block_z_pos
    first_run = True
    x_compare = 0
    while not target_reached and running:
        # X Values are checked from the Controller. Controller sends 0 until he picked up the Block
        # The first Value starts the capturing
        x, z = fc.getCords()
        print("X-Wert" + str(x))
        if x > 0:
            # Start PictureDetection by first
            if first_run:
                x_compare = x
                print("Erster x Wert" + str(x_compare))
                Thread(target=cap.start, args=(drop_block,)).start()
                first_run = False
            # Old Programm: So the first Value after 0 gets read and safe to compare the progress, after this position.
            # else:
                # block_x_pos = x_compare - x + BLOCK_STARTPOS
                # block_z_pos = z
            x_compare = 325 - x
            if x_compare > 65:
                block_x_pos = x_compare

        time.sleep(0.25)


def drop_block():
    global block_z_pos
    global target_reached

    fc.object_detected()
    time.sleep(5)
    block_z_pos = 1
    # target_reached stops the cord readloop, timesleep so the reading continues a few seconds
    target_reached = True


def get_cords():
    return block_x_pos, block_z_pos


if __name__ == "__main__":
    main()

