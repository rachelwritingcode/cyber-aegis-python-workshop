import nmap3
import json 

# Find out the OS of an IP or url
nmap = nmap3.Nmap()
os_results = nmap.nmap_os_detection("127.0.0.1") # Run this as root user
results_file = open("network_results.json", "w")
json.dump(os_results, results_file, indent = 6)
results_file.close()
