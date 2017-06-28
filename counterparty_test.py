import json
import requests
from requests.auth import HTTPBasicAuth
import sys

#DO YOU WANT TO CREATE OR READ?
#test ="create"
test ="create"

#TESTNET PORT 14000 / DONT FORGET TO CHANGE USER NAME FOR MAINNET
url = 'http://ec2-54-93-227-47.eu-central-1.compute.amazonaws.com:4000/api/'
headers = {'content-type': 'application/json'}
auth = HTTPBasicAuth('4321rpc1234','4321coop1234')


#CREATE TOKEN
if test is 'create':
	payload = {
	           "method": "create_issuance",
	           "params": {
	                      "source": "19Ri5T5Mujh2TQcvR1NpuuuDTA8T7vSgdA", #MAINNET Wallet number
	                      "asset": "A11945611906419650012",
	                      "quantity": 10,
	                      "divisible": False,
	                      "description": "ascii code here",
	                      "transfer_destination": None
	                     },
	           "jsonrpc": "2.0",
	           "id": 0
	          }

	resp = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
	data = resp.json()
	#u before the keys are handled automatically (unicode)
	print data

#READ TOKEN
if test is 'read':
	payload = {
	           "method": "get_asset_info",
	           "params": {
	                      "assets":['A11945611906419650000'] #must be list of assets
	                     },
	           "jsonrpc": "2.0",
	           "id": 0
	          }

	resp = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
	data = resp.json()
	#u before the keys are handled automatically (unicode)
	string_out = data['result'][0]['description']
	print data


#TestNet To 


