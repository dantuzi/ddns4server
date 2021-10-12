# Dynamic Dns for server

Script to periodically update a DNS authoritative record with the public IP of the server where it is installed on.  
Currently only GoDaddy is supported

## Installation
1. Create a folder ***.ddns4s*** on your HOME_PATH: `/home/<user>/.ddns4s`
2. Create a configuration file ***config.json***  

        {
            "server_subdomain": "dns-upd-test",
            "godaddy": {
                "api_key": "<DNS_API_KEY>",
                "api_secret": "<DNS_API_SECRET>",
                "root_domain": "ddns4s.com"
            }
        }

3. Replace the credentials for your DNS provider
4. Run the script

        python src/sripts/godaddy.ph

5. Verify that everything is set correctly by querying the DNS

        ➜  ~ dig A +short dns-upd-test.ddns4s.com
        151.143.24.35

6.Install the script as a cronjob task

---

## Testing
Tested only on linux servers

