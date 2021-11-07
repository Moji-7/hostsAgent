
import runHost
import runnerOnly
from termcolor import colored
from multiprocessing import Pool
#import asyncio
samanehList = [['10'],[13,14]]

#for i in range(len(samanehList)):
#	print colored("testing runHost","red")
#	runHost.main(samanehList[i]);

result_list=[]
def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)

def shell2(samanehid):
	print colored("testing runHost %s"%(samanehid),"red")
	runHost.main(samanehid);


def me():
	pool = Pool()
	for thisList in range(len(samanehList)):
		 pool.apply_async(shell2,args=(samanehList[thisList],),callback=log_result)
	#result1 = [pool.apply_async(shell2,args=(samanehList[thisList],)) for thisList in range(len(samanehList))]
	#result1.get()
	pool.close();
	pool.join()
	print("ali")
	print(result_list)
	#return str("by")

me()

#runHost.main([10,11]);
#runHost.main([13,14]);

#return str("finish")

#print colored("testing runnerOnly","red")
#runnerOnly.main(samanehList,"infoCdcStatus");
