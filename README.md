Carbon Black has a configuration in /etc/cb/cb.conf that allows you to choose remove sensors that have been offline for X days.  

One thing that's missing is to control this by Sensor Group.  

CB-Cloud-Cleaner takes a sensor group ID and X days amount to remove those sensors.
I found this particularly useful for cleaning up my AWS sensors.

Hope this helps :)

usage:

./cloud-cleaner.py -c cb-server.config -do 10 -gid 5

-c = CB server config file
-do = days offline
-gid = groupID 