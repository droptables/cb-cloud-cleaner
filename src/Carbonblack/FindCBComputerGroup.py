import requests

class FindCBComputerGroup(object):

    @staticmethod
    def Run(groupid, cbserverurl, cbapitoken):

        headers = {"X-Auth-Token": cbapitoken}  
        resp = requests.get(cbserverurl+str("/api/v1/sensor?groupid="+str(groupid)), headers=headers, verify=False)  
        return resp.json()