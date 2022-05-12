import requests, json, urllib3, pprint, time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://sandboxdnac2.cisco.com"

def get_auth_token():
    auth_url = base_url + "/dna/system/api/v1/auth/token"

    headers = {"Content-Type": "application/json"}

    response = requests.post(auth_url, headers=headers, auth=("devnetuser", "Cisco123!"), verify=False)

    token = json.loads(response.text)['Token']

    return token

def get_sites(token):
    print("Getting sites...\n")
    url = base_url + "/dna/intent/api/v1/site"

    headers = {"x-auth-token": token}

    response = requests.get(url, headers=headers, verify=False)

    data = response.json()['response']

    for i in data:
        print(i['siteNameHierarchy'])

def main():
    token = get_auth_token()
    get_sites(token)

if __name__ == "__main__":
    main()