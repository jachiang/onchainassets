#test1
import json
import requests
from requests.auth import HTTPBasicAuth
import time


#Get Balance?
get_balance = 'no'
set_issuance = 'yes'

#url = "http://localhost:4000/api/" for MAINNET
url = 'http://ec2-52-59-226-244.eu-central-1.compute.amazonaws.com:4000/api/'
headers = {'content-type': 'application/json'}
#PASSWORD = '4321coop1234'
auth = HTTPBasicAuth('rpc','rpc')


#GET BALANCE IN ADDRESS
if get_balance is 'yes':
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


if set_issuance is 'yes':
  #TEST different ascii codes from 0-127
  char = ""
  for i in range(127):
    char = char + chr(i)

  #ISSUANCE
  for i in range(1):
    payload = {
               "method": "create_issuance",
               "params": {
                          "source": "19Ri5T5Mujh2TQcvR1NpuuuDTA8T7vSgdA", #Mainnet Wallet Address is 19Ri5T5Mujh2TQcvR1NpuuuDTA8T7vSgdA
                          "asset": "A11945611906419650001",
                          "quantity": 10,
                          "divisible": False,
                          "description": char+i*chr(1), #add an arbitrary character to make one longer
                          "transfer_destination": None,
                          "disable_utxo_locks": True
                         },
               "jsonrpc": "2.0",
               "id": 0
              }
    resp = requests.post(url, data=json.dumps(payload), headers=headers, auth=auth)
    data = resp.json()
    print data
    time.sleep(.5)
    print len(char+i*chr(1))

#MAINNET TO DOS
#things to do: 1) Verify max char on mainnet 2) Read asset back
#Test different issuance commands (length iterating 100+)
#Submit 2-4, check how fee varies










