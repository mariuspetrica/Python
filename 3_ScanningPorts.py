import nmap


nm = nmap.PortScanner()

host = "scanme.nmap.org"
option = " -p 22,53 -sVC -A -o "##scan_results.txt"

nm.scan(host, arguments=option)

for host in nm.all_hosts():
    print(f"The host is {host}, scan {nm[host].hostname}")
    print(f"The state is {nm[host].state()}")
    for protocol in nm[host].all_protocols():
        print(f"Protocol is {protocol}")
        port_info = nm[host][protocol]
        for port,state in port_info.items():
            print(f"Port: {port} and state {state}")
            