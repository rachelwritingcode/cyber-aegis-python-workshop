import nmap3

nmap = nmap3.Nmap()
results = nmap.scan_top_ports("127.0.0.1")
print(results)

nmap_scan = nmap3.NmapScanTechniques()
ping_results = nmap_scan.nmap_ping_scan("https://www.github.com")
print(ping_results)