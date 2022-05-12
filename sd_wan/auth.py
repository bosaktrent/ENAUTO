import requests, json, urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
base_url = "https://sandbox-sdwan-2.cisco.com"

def auth():
    auth_url = base_url + "/j_security_check"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {"j_username": "devnetuser", "j_password": "RG!_Yw919_83"}
    response = requests.post(auth_url, headers=headers, data=payload, verify=False)
    return response.cookies