from threading import Thread
import time

def timer(name, delay, repeat):
    print "Timer: %s started." % name

    while repeat > 0:
        time.sleep(delay)
        print name + ": " + str(time.ctime(time.time()))
        repeat -= 1

    print "Timer: %s completed." % name

def main():
    thread_one = Thread(target=timer, args=("Timer 1", 1, 5))
    thread_two = Thread(target=timer, args=("Timer 2", 2, 5))
    thread_one.start()
    thread_two.start()

    print "Main complete."

main()
