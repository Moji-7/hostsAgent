

from multiprocessing import Pool
import subprocess
from termcolor import colored


def shell(samanehid):
    #time.sleep(2)
    #return samanehid*samanehid
    print colored("the samaneh ID is going to run on server:%s"%(samanehid),"red")
    stdout = subprocess.call( ['/home/m_pourmirzaei/checklist/r2New.sh %s' %(samanehid)],shell = True)

def main(samaneh):
	print colored("the samaneh ID list are: %s"%(samaneh),"yellow")
	pool2 = Pool()
	#result1 = [pool2.apply_async(shell,args=(x,)) for x in samaneh]
	for thisList in ((samaneh)):
		 print colored("the samaneh ID is: %s"%(thisList),"blue")
		 pool2.apply_async(shell,args=(thisList,))
	pool2.close();
	pool2.join()   
	return str("finish")

#main([10,11])
