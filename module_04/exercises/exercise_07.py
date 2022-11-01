import nmap3
import json 

# Find out the OS of an IP or url
nmap = nmap3.Nmap()
os_results = nmap.nmap_os_detection("127.0.0.1") # Run this as root user
with open('os_results.json', 'w') as f:
    f.write(json.dumps(os_results, indent=3))
