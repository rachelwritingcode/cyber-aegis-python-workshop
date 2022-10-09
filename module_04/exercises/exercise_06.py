import nmap3
import json

nmap  = nmap3.Nmap()
port_results = nmap.scan_top_ports("127.0.0.1")

with open('port_results.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(port_results, indent=3))
