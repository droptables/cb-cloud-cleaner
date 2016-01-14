import argparse
from clint.textui import colored


class Launch(object):
    
  def get_args(self):
      parser = argparse.ArgumentParser(description='Terminal application for remediating Bit9 alerts in a Jiffy.')
      parser.add_argument('-c','--config-file', action='store', dest="configfile", help="Config file for Carbon Black Server URL and API Token.", required=True)
      parser.add_argument('-do','--days-offline', action='store', dest="daysoffline", help="Number of days offline to remove sensors.", required=True)
      parser.add_argument('-gid','--group-id', action='store', dest="groupid", help="ID of the group to clean.", required=True)

      args = parser.parse_args()
      return args

  def load_cb_config(self,configile):
          #print colored.yellow("[*] Loading config file.")
          cfile= open(configile, "r").readlines()
          cbserverurl=str(cfile[0].rstrip())
          cbapitoken=str(cfile[1].rstrip())

          #print colored.green("[+] Completed.\n")
          return (cbserverurl,cbapitoken)
