import requests, json, urllib3, pprint, time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://sandboxdnac2.cisco.com"

def get_auth_token():
    auth_url = base_url + "/dna/system/api/v1/auth/token"

    headers = {"Content-Type": "application/json"}

    response = requests.post(auth_url, headers=headers, auth=("devnetuser", "Cisco123!"), verify=False)

    token = json.loads(response.text)['Token']

    return token

def get_discovery_count(token):
    print("Getting count of all discovery jobs...\n")
    url = base_url + "/dna/intent/api/v1/discovery/count"

    headers = {"x-auth-token": token}

    response = requests.get(url, headers=headers, verify=False)
    print(response.json(), "\n")

def get_discoveries_by_range(token):
    print("Getting discovery jobs...\n")
    url = base_url + "/dna/intent/api/v1/discovery/1/1"
    
    headers = {"x-auth-token": token}

    response = requests.get(url, headers=headers, verify=False)

    data = response.json()['response']

    print(data)

def main():
    token = get_auth_token()
    get_discovery_count(token)
    get_discoveries_by_range(token)

if __name__ == "__main__":
    main()