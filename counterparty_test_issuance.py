
import json
import requests
from requests.auth import HTTPBasicAuth
import time

#url = "http://localhost:4000/api/"
url = 'http://ec2-54-93-227-47.eu-central-1.compute.amazonaws.com:14000/api/'
headers = {'content-type': 'application/json'}
#PASSWORD = '4321coop1234'
auth = HTTPBasicAuth('rpc','rpc')

#GET BALANCE IN ADDRESS
payload = {
           "method": "get_unspent_txouts",
           "params": {
                      "address": "n4a9WAw1scE8WVTtyjckcKx5sL8o5upxvW", #need to create address at bitcoind?
                      "unconfirmed": False,
                     },
           "jsonrpc": "2.0",
           "id": 0
          }
resp = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
data = resp.json()

#TEST different ascii codes from 0-127
char = ""
for i in range(128):
  char = char + chr(i)

#ISSUANCE
payload = {
           "method": "create_issuance",
           "params": {
                      "source": "n4a9WAw1scE8WVTtyjckcKx5sL8o5upxvW", #need to create address at bitcoind?
                      "asset": "A11945611906419650010",
                      "quantity": 10,
                      "divisible": False,
                      "description": char,
                      "transfer_destination": None,
                      "disable_utxo_locks": True
                     },
           "jsonrpc": "2.0",
           "id": 0
          }
resp = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
data = resp.json()
print data['result']
#u before the keys are handled automatically (unicode)

#READING ISSUED ASSET
payload = {
           "method": "get_holder_count",
           "params": {
                      "source": "n4a9WAw1scE8WVTtyjckcKx5sL8o5upxvW", #need to create address at bitcoind?
                      "asset": "A11945611906419650000",
                      "quantity": 10,
                      "divisible": False,
                      "description": char,
                      "transfer_destination": None,
                      "disable_utxo_locks": True
                     },
           "jsonrpc": "2.0",
           "id": 0
          }
resp = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
data = resp.json()







