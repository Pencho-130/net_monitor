import requests

def api_call_threatFox(iplist):

    url = 'https://threatfox-api.abuse.ch/api/v1/'

    for ip_to_check in iplist:
        data = {
            "query": "search_ioc",
            "search_term": ip_to_check
        }

        response = requests.post(url, json=data)

        if response.status_code == 200:
            response_data = response.json()
            if response_data['query_status'] == 'ok' and response_data['data']:
                for entry in response_data['data']:
                    ip_port = entry['ioc']
                    threat_type_desc = entry['threat_type_desc']
                    print(f"ThreatFox found this entry to be malicious -> IP:PORT: {ip_port}")
                    print(f"Reason ->  {threat_type_desc}")
        else:
            print(f"Request to ThreatFox failed with status code: {response.status_code}")
