import requests
import json
import os

home_dir = os.path.expanduser("~")

# Get configuration
config_file = open("{}/.ddns4s/config.json".format(home_dir), 'r')
config = json.load(config_file)

DNS_API_URL = "https://api.godaddy.com"
DNS_API_Key = config['godaddy']['api_key']
DNS_API_SECRET = config['godaddy']['api_secret']

ROOT_DOMAIN = "antuzi.com"
SERVER_SUBDOMAIN = config['server_subdomain']


# Get current external IP
my_ip_response = requests.get('http://ipinfo.io')

my_ip_info = json.loads(my_ip_response.text)
my_ip = my_ip_info['ip']


# Update DNS
godaddy_req = "{}/v1/domains/{}/records/A/{}".format(DNS_API_URL, ROOT_DOMAIN, SERVER_SUBDOMAIN)
req_payload = [{"data": my_ip, "ttl": 900}]
auth = "sso-key {}:{}".format(DNS_API_Key, DNS_API_SECRET)
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": auth
}

godaddy_response = requests.put(godaddy_req, data=json.dumps(req_payload), headers=headers)

print(godaddy_response.text)
