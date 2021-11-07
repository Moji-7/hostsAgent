
import schedule
import time
import logging
import os
import runHost
#import runnerOnly
logging.basicConfig(level= logging.INFO, filename="runLog.log")
#bashPath=""
os.system("echo 'infoType-fn' > /home/m_pourmirzaei/checklist/mustApiOnly.txt")
os.system("echo 'infoCdcStatus-fn' >> /home/m_pourmirzaei/checklist/mustApiOnly.txt")
print("ali")
def func():
        print("run")
        runHost.main()

        #jq '.result[][].cdcstatus | select(.count==0)'  only-cdcstatus-*.json | jq -s '.' |jq '[.[].server] |group_by(.)[]|{samaneh:(.[0]),count:[.[]]|length}' |jq  -s ' .' > oldold
        
        #runnerOnly.main("infoCdcStatus" "cdcstatus")
        os.system("python runnerOnly.py 'infoCdcStatus' 'cdcstatus'")
        
        #jq '.result[][].cdcstatus | select(.count==0)'  only-cdcstatus-*.json | jq -s '.' |jq '[.[].server] |group_by(.)[]|{samaneh:(.[0]),count:[.[]]|length}' |jq  -s ' .' 
        #runner.main()
  
schedule.every(2).seconds.do(func)
  
while True:
    schedule.run_pending()
    time.sleep(1)
