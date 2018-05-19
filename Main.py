from threading import Thread
import _thread
# import FreedomCommunication as fc
import fc_fake_test as fc
import cap
import time
import GUI

BLOCK_STARTPOS = 45
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
        # X Values are only send from the Controller, after it pick up the Block. Until this, he sends 0
        # So the first Value after 0 gets read and safe to compare the progress, after this position.
        x, z = fc.getCords()
        if x > 0:
            # Start PictureDetection by first
            if first_run:
                x_compare = x
                Thread(target=cap.start, args=(drop_block,)).start()
                # _thread.start_new_thread(cap.start, (drop_block,))
                first_run = False
            else:
                block_x_pos = x_compare - x + BLOCK_STARTPOS
                block_z_pos = z
        time.sleep(1)


def drop_block():
    fc.object_detected()
    global target_reached
    target_reached = True


def get_cords():
    return block_x_pos, block_z_pos


if __name__ == "__main__":
    main()

