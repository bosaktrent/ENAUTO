import requests, urllib3, json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://sandboxdnac2.cisco.com"

auth_url = base_url + "/dna/system/api/v1/auth/token"

headers = {"Content-Type": "application/json"}

response = requests.post(auth_url, headers=headers, auth=("devnetuser", "Cisco123!"), verify=False)

token = json.loads(response.text)['Token']

print(token)