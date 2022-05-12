import json, requests, urllib3, pprint

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
base_url = "https://sandbox-sdwan-2.cisco.com"

def auth():
    auth_url = base_url + "/j_security_check"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {"j_username": "devnetuser", "j_password": "RG!_Yw919_83"}
    response = requests.post(auth_url, headers=headers, data=payload, verify=False)
    return response.cookies

def get_all_users(cookie):
    print("Getting Users...")
    print("Users:")
    url = base_url + "/dataservice/admin/user"
    response = requests.get(url, cookies=cookie, verify=False)
    data = response.json()['data']

    for i in data:
        print(i)

def get_active_sessions(cookie):
    print("Getting active sessions...")
    print("Active Sessions:")
    url = base_url + "/dataservice/admin/user/activeSessions"
    response = requests.get(url, cookies=cookie, verify=False)

    data = response.json()['data']

    pprint.pprint(data)

def main():
    cookie = auth()
    get_all_users(cookie)
    get_active_sessions(cookie)


if __name__ == "__main__":
    main()