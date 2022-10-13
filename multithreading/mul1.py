#multithreading -> is used to execute parallel
import threading
import time
def calc_square(num):           #2,3,4,5
    print("calculate square")
    for i in num:
        time.sleep(.3)
        print("square=",i*i)
def calc_cube(num):             #2,3,4,5
    print("claculate cube")
    for i in num:
        time.sleep(.3)
        print("cube=",i*i*i)
ar=[2,3,4,5]
t1=threading.Thread(target=calc_square,args=(ar,))
t2=threading.Thread(target=calc_cube,args=(ar,))
t1.start()
t2.start()
t1.join()
t2.join()
print("Finished execution of threads")