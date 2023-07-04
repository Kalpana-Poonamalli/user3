#Program to demonstrate Threads
import threading.*
class thread1(threading.thread):
 def run(self):
  for  i in range(10):
   print(i);
t1=thread()
t1.start() 
