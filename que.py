import Queue
import runHost
import runnerOnly
from termcolor import colored
from multiprocessing import Pool






def shell2(samanehid):
        print colored("testing runHost %s"%(samanehid),"red")
        runHost.main(samanehid);



def task (name,work_queue):
    print("Task %s runningiiiiiiiiiiiiiiiiiiiiiiii"%(name))
    if work_queue.empty():
        print("Task %s nothing to do"%(name))
    else:
        while not work_queue.empty():
	    count = work_queue.get()
	    #pool = Pool()
	    print("Task %s runningiiiiiiiiiiiiiiiiiiiiiiii"%(count))
	    runHost.main(count)
            print("Task %s running"%(name))

def main():
    # Create the queue of work
    work_queue = Queue.Queue()

    # Put some work in the queue
    #for work in [[1,2,3,4,5,6],[7,8,9,10,11],[12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]:
    #for work in [[1010,1111]]:
    for work in [['log','cdc']]:
        work_queue.put(work)

    pool=Pool()
    samanehList=[[1,2,3,4,5,6],[7,8,9,10,11],[12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]] 
    samanehList=["log","uptime"] 

    #for thisList in ((samanehList)):
	       #print("this:%s"%thisList)
               #pool.map_async(task,thisList)
    #pool.close()
    #pool.join()



    # Create some synchronous tasks
    tasks = [(pool, [8,22,23], work_queue)
	#,(pool, [13,14,15,16,17], work_queue)
	]
    #for work in [[1010,1111]]:
    #for work in [[1010,1111]]:
    # Run the tasks
    for t, n, q in tasks:
	print ("tt%s ss%s ff%s"%(t,n,q))
	#pool.map_async(task,thisList)
        t.apply_async(runHost.main(n),args=(n,))
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()

