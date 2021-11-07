
from multiprocessing import Pool
import sys
import subprocess
from termcolor import colored

def shell(samanehid,whichApi):
    print colored("the api is:%s and the samaneh is:%s"%(whichApi,samanehid),"yellow")
    #whichApi=sys.argv[1]#infoCdcStatus
    #whichApi_child=sys.argv[2]#cdcstatus
    stdout = subprocess.call( ['/home/m_pourmirzaei/checklist/only.sh %s all %s' %(samanehid,whichApi)],shell = True)

def main(samaneh,whichApi):
    pool = Pool()
    print colored("samaneh list: %s"%(samaneh),"red")
    result1 = [pool.apply_async(shell,args=(x,whichApi,)) for x in samaneh]    # evaluate "solve1(A)" asynchronously
    pool.close();
    pool.join()
    return str("finish")

#main()
