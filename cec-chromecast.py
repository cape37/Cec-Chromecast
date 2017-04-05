#!/usr/bin/python

from __future__ import print_function
import time
import re
import pychromecast # https://github.com/balloob/pychromecast
import os

#Get info from chromecast
chromecasts = pychromecast.get_chromecasts()
cast = next(cc for cc in chromecasts if cc.device.friendly_name == "ChromecastName") #Change ChromcastName
status = str(cast.status)

#Regex the info from chromecast
prog = re.compile(r'app_id=u.(\S{0,8})')
applist = prog.search(status)
app = str(applist.group(1))

#Dashboard app_id on chromecast
dash = str("E8C28D3C")

#Do something if chromecast is at dash.
if app == dash:

        #Send hexcode to TV via CEC-client (Switches hdmi port)
        os.system('echo "tx 4f:82:40:00" | cec-client -s') #Adjust hex code to your tv

#Print app_id for current app
print(app)
