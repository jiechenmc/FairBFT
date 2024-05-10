from xml.dom.minidom import parse
document = parse("nodes.xml")

hosts = list(map(lambda x: x.getAttribute("ipv4"),document.getElementsByTagName("host")))

with open("replicas.txt", "w") as f:
    for host in hosts:
        f.write(f"{host} {host}\n")

with open("servers", "w") as f:
    for host in hosts:
        f.write(f"chenj@{host}\n")