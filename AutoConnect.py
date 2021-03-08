from pywinauto import application
import time
import os
import json

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
time.sleep(5)

with open('config.json', 'r') as f:
    config = json.load(f)

CREON_PWD = config['CREON']['pwd']
CREON_PWDCERT = config['CREON']['pwdcert']

app = application.Application()
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:dreament /pwd:{0} /pwdcert:{1} /autostart'.format(CREON_PWD, CREON_PWDCERT))
time.sleep(60)
