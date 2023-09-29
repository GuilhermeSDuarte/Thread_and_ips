import ipaddress

ip = '192.168.0.0/24'

endereco = ipaddress.ip_network(ip)

for ips in endereco:
    print(ips)