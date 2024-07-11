import requests
import json

# Function to call the AbuseIPDB API and check if the provided IPs are malicious
def api_call_abuseIPDB(iplist, api_key):

    # Loop through each IP in the provided list
    for ip_to_check in iplist: 
        # URL for the AbuseIPDB API endpoint
        url = 'https://api.abuseipdb.com/api/v2/check'
        
        # Parameters for the API request
        params = {
            'ipAddress': ip_to_check,  # The IP address to check
            'maxAgeInDays': 90,        # The maximum age of the reports to consider
            'verbose': ''              # Verbose parameter for detailed response
        }
        
        # Headers for the API request, including the API key for authentication
        headers = {
            'Key': api_key,            # Your AbuseIPDB API key
            'Accept': 'application/json'  # Specify that the response should be in JSON format
        }

        # Send the GET request to the AbuseIPDB API
        response = requests.get(url, params=params, headers=headers)
        
        # Decode the JSON response from the API
        decoded_response = json.loads(response.text)
        
        # Extract the abuse confidence score from the response data
        ipdb_result = decoded_response['data']['abuseConfidenceScore']
        
        # If the abuse confidence score is greater than 50, consider the IP malicious
        # You can change this value to finetune it.
        if ipdb_result > 50:
            print(f'AbuseIPDB found this IOC {ip_to_check} to be of malicious character with score {ipdb_result}/100')
