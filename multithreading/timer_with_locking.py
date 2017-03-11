import threading
import time

tLock = threading.Lock()

def timer(name, delay, repeat):
    print "Timer: %s started." % name

    # acquire a lock on the thread that called this funciton first
    tLock.acquire()
    print "%s has acquired the lock" % name
    while repeat > 0:
        time.sleep(delay)
        print name + ": " + str(time.ctime(time.time()))
        repeat -= 1

    print "%s is releasing the lock" % name

    # release lock and allow another thread to acquire it
    tLock.release()

    print "Timer: %s completed." % name

def main():
    thread_one = threading.Thread(target=timer, args=("Timer 1", 1, 5))
    thread_two = threading.Thread(target=timer, args=("Timer 2", 2, 5))
    thread_one.start()
    thread_two.start()

    print "Main complete."

main()
