import requests

# Function to call the ThreatFox API and check if the provided IPs are malicious
def api_call_threatFox(iplist):
    # URL for the ThreatFox API endpoint
    url = 'https://threatfox-api.abuse.ch/api/v1/'

    # Loop through each IP in the provided list
    for ip_to_check in iplist:
        # Data for the API request
        data = {
            "query": "search_ioc",  # Type of query to perform
            "search_term": ip_to_check  # The IP address to search for
        }

        # Send the POST request to the ThreatFox API
        response = requests.post(url, json=data)

        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            response_data = response.json()  # Decode the JSON response

            # Check if the query status is 'ok' and there is data in the response
            if response_data['query_status'] == 'ok' and response_data['data']:
                # Iterate through the data entries in the response
                for entry in response_data['data']:
                    ip_port = entry['ioc']  # Extract the IP:PORT
                    threat_type_desc = entry['threat_type_desc']  # Extract the threat type description
                    print(f"ThreatFox found this entry to be malicious -> IP:PORT: {ip_port}")
                    print(f"Reason ->  {threat_type_desc}")
        else:
            # Print an error message if the request failed
            print(f"Request to ThreatFox failed with status code: {response.status_code}")
