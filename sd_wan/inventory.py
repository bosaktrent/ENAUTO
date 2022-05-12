import requests, urllib3, json, pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
base_url = "https://sandbox-sdwan-2.cisco.com"

def auth():
    auth_url = base_url + "/j_security_check"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {"j_username": "devnetuser", "j_password": "RG!_Yw919_83"}
    response = requests.post(auth_url, headers=headers, data=payload, verify=False)
    return response.cookies

def get_controllers(cookie):
    print("Getting vSmart Controllers...")
    print("vSmart Controller IP Addresses:")
    url = base_url + "/dataservice/system/device/controllers"
    response = requests.get(url, cookies=cookie, verify=False)
    
    data = response.json()['data']

    for i in data:
        print(i['deviceIP'])
    
    print('\n')

def get_vedges(cookie):
    print("Getting vEges...")
    print("vEdge Chasis Numbers:")
    url = base_url + "/dataservice/system/device/edges"
    response = requests.get(url, cookies=cookie, verify=False)

    data = response.json()['data']

    for i in data:
        print(i['chasisNumber'])
    
    print('\n')

def get_sync_status(cookie):
    print("Getting vEdge sync status...")

    url = base_url + "/dataservice/system/device/controllers/vedge/status"
    response = requests.get(url, cookies=cookie, verify=False)

    data = response.json()['data']
    print(data)

def main():
    cookie = auth()
    get_controllers(cookie)
    get_vedges(cookie)
    get_sync_status(cookie)

if __name__ == "__main__":
    main()