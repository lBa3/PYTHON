import time

from threading import Thread

def myfunc(i):
    print ("sleeping 5 sec from thread", i)
    time.sleep(5)
    print ("finished sleeping from thread", i)

for i in range(10):
    t = Thread(target=myfunc, args=(i,))
    t.start()

   