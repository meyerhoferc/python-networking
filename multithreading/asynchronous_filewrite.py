import threading
import time

class AsynchronousWrite(threading.Thread):
    def __init__(self, text, output_file):
        threading.Thread.__init__(self)
        self.text = text
        self.output_file = output_file

    def run(self):
        file = open(self.output_file, "a")
        file.write(self.text + "\n")
        file.close()
        time.sleep(2)
        print "Finished background file write to %s" % self.output_file

def main():
    message = raw_input("Enter text to store: ")
    background_worker = AsynchronousWrite(message, "out.txt")
    background_worker.start()
    print "The program can continue to run while it writes in another file."
    print 100 + 400

    background_worker.join()
    print "Waited until thread was complete."

main()
