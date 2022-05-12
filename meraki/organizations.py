import requests, json, urllib3, pprint
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://api.meraki.com/api/v1"

apiKey = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"

def get_organizations():
    url = base_url + "/organizations"

    headers = {
        "Content-Type": "application/json",
        "X-Cisco-Meraki-API-Key": apiKey
    }

    response = requests.get(url, headers=headers)

    data = response.json()

    return data[0]['id']

def get_networks(id):
    url = base_url + "/organizations/{}/networks/".format(id)

    headers = {
        "X-Cisco-Meraki-API-Key": apiKey
    }

    response = requests.get(url, headers=headers, verify=False)

    print(response.text)

id = get_organizations()
get_networks(id)
