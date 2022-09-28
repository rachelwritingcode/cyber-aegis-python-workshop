import nmap3
import json 

# Find the all the open ports
nmap = nmap3.Nmap()
port_results = nmap.scan_top_ports("127.0.0.1")
results_file = open("ports_results.json", "w")
json.dump(port_results, results_file, indent = 6)
results_file.close()

