#!/usr/bin/env python
from Carbonblack.FindCBComputer import FindCBComputer
from Carbonblack.FindCBComputerGroup import FindCBComputerGroup
from Carbonblack.RemoveCBComputer import RemoveCBComputer
from Launch.Launch import Launch
from datetime import datetime, timedelta


if __name__ == '__main__':
	#Pull in the Launch module and get cmdline args via argparse.
    launch=Launch()
    args=launch.get_args()
    cbserverurl,cbapitoken=launch.load_cb_config(args.configfile)
    now = datetime.now()

    #get computers from sensor group '6', aka 'cloud-ops'
    cblookup = FindCBComputerGroup.Run(str(args.groupid),cbserverurl,cbapitoken)
    for computer in cblookup:
    	if computer['uninstall']==False:
	    	lastcheckintime = datetime.strptime(str(computer['last_checkin_time'][:19]),"%Y-%m-%d %H:%M:%S")
	    	if (now-lastcheckintime) > timedelta(days = int(args.daysoffline)):
	    		print computer['computer_name']+str(" has not checked in in over "+str(args.daysoffline)+" days, removing.")
	    		RemoveCBComputer.Run(computer['computer_name'], cbserverurl, cbapitoken)