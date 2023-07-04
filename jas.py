#Program to demonstrate Threads
import threading
import time
class thread1(threading.Thread) :
 def run(self) :
  for i in range(10):
   print("thread1 :"+str(i));
   time.sleep(4)
class thread2(threading.Thread) :
 def run(self) :
  for i in range(10):
   print("thread2 :"+str(i));
   time.sleep(6)
t1=thread1()
t1.start()
t2=thread2()
t2.start()


