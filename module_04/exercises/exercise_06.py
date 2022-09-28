import nmap3
import json 

# Find the all the open ports
nmap = nmap3.Nmap()
port_results = nmap.scan_top_ports("127.0.0.1")
# create a json file for the results
results_file = open("ports_results.json", "w")
# store the json data into the json file
json.dump(port_results, results_file, indent = 3)
results_file.close()

