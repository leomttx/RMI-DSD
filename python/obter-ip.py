import socket

nome_do_host_local = socket.gethostname()
ip_do_host_local = socket.gethostbyname(nome_do_host_local)
print(ip_do_host_local)