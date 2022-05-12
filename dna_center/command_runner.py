import requests, json, urllib3, pprint, time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

base_url = "https://sandboxdnac2.cisco.com"

def get_auth_token():
    auth_url = base_url + "/dna/system/api/v1/auth/token"

    headers = {"Content-Type": "application/json"}

    response = requests.post(auth_url, headers=headers, auth=("devnetuser", "Cisco123!"), verify=False)

    token = json.loads(response.text)['Token']

    return token

def get_valid_keywords(token):
    url = base_url + "/dna/intent/api/v1/network-device-poller/cli/legit-reads"
    headers = {"x-auth-token": token, "Content-Type": "application/json"}
    
    response = requests.get(url, headers=headers, verify=False)

    data = json.loads(response.text)['response']

    print("Keywords of CLIs accepted by command runner:\n")
    print(data, "\n")

def get_device_ids(token):
    url = base_url + "/dna/intent/api/v1/network-device"
    headers = {"x-auth-token": token, "Content-Type": "application/json"}

    response = requests.get(url, headers=headers, verify=False)

    data = json.loads(response.text)['response']
    device_ids = []
    for device in data:
        device_ids.append(device["id"])

    return device_ids

def send_command(token, deviceIds):
    print("Sending command 'show clock'...\n")

    url = base_url + "/dna/intent/api/v1/network-device-poller/cli/read-request"
    headers = {"x-auth-token": token, "Content-Type": "application/json"}

    payload = {"commands": ["show clock"], "deviceUuids": deviceIds}

    response = requests.post(url, headers=headers, data=json.dumps(payload), verify=False)

    data = json.loads(response.text)['response']['taskId']
    return data

def wait_for_task(token, taskId):
    url = base_url +"/dna/intent/api/v1/task/" + taskId
    headers = {"x-auth-token": token}

    attempts = 3
    waitTime = 5

    for i in range(attempts):
        time.sleep(waitTime)

        response = requests.get(url, headers=headers, verify=False)

        data = json.loads(response.text)['response']

        if "endTime" in data:
            fileId = json.loads(data['progress'])['fileId']
            return fileId

    print("Request timed out")

def get_file(token, fileId):
    url = base_url + "/dna/intent/api/v1/file/" + fileId

    # print(fileId)
    headers = {"x-auth-token": token, "Content-Type": "application/json"}

    response = requests.get(url, headers=headers, verify=False)

    data = response.json()

    for i in data:
        print(i)

def main():
    token = get_auth_token()
    get_valid_keywords(token)
    deviceIds = get_device_ids(token)
    taskId = send_command(token, deviceIds)
    fileId = wait_for_task(token, taskId)
    get_file(token, fileId)

if __name__ == "__main__":
    main()