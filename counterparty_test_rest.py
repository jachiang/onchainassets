import requests

url = "ec2-54-93-227-47.eu-central-1.compute.amazonaws.com:4000/rest/"
headers = {'content-type': 'application/json'}

query = 'sends/get?source=mn6q3dS2EnDUx3bmyWc6D4szJNVGtaR7zc&destination=mtQheFaSfWELRB2MyMBaiWjdDm6ux9Ezns&op=AND'

response = requests.get(url + query, headers=headers)
print("Response: ", response.text)