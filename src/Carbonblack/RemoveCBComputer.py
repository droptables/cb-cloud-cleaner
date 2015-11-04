import cbapi,requests,json
from Carbonblack.FindCBComputer import FindCBComputer

class RemoveCBComputer(object):

    @staticmethod
    def Run(hostname, cbserverurl, cbapitoken):
		authJson={
		'X-Auth-Token': cbapitoken, 
		'content-type': 'application/json'
		}
		data = FindCBComputer.Run(hostname.rstrip())
		data[0]["uninstall"] = True
		r = requests.put("%s/api/v1/sensor/%s" % (cbserverurl, data[0]['id']), headers=authJson,
	                       data=json.dumps(data[0]), timeout=120, verify=False)
		r.raise_for_status()
		return r.status_code == 200