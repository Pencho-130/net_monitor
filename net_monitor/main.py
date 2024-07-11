import time
from connections import get_active_connections
from abuseipdb import api_call_abuseIPDB
from threatfox import api_call_threatFox
from dotenv import load_dotenv
import os

# Main function to monitor network connections and check for malicious IPs
def main():
    # Load environment variables from the .env file
    load_dotenv()
    
    # Get the AbuseIPDB API key from the environment variables
    abuseipdb_api_key = os.getenv('ABUSEIPDB_API_KEY')
    
    # Initialize a set to keep track of seen IPs
    seen_ips = set()

    try:
        # Infinite loop to continuously monitor network connections
        while True:
            # Get the current active network connections
            current_connections = get_active_connections()
            
            # Find new IPs by checking which current connections are not in the seen IPs set
            new_ips = [ip for ip in current_connections if ip not in seen_ips]
            
            # If there are new IPs detected
            if new_ips:
                print("\nNew IPs detected:")
                print(new_ips)
                
                # Check the new IPs with AbuseIPDB
                api_call_abuseIPDB(new_ips, abuseipdb_api_key)
                
                # Check the new IPs with ThreatFox
                api_call_threatFox(new_ips)
            
            # Update the set of seen IPs with the current connections
            seen_ips.update(current_connections)
            
            # Wait for 2 seconds before checking again
            time.sleep(2)
    
    except KeyboardInterrupt:
        # Handle the user interrupt (Ctrl+C) to stop the monitoring
        print("\nMonitoring stopped.")

# Entry point for the script
if __name__ == "__main__":
    main()
