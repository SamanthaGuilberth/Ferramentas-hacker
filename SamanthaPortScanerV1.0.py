
from socket import socket

import socket

from colorama import Fore, Back, Style

print(Fore.RED+ "########################################################\n")
print(Fore.YELLOW +"************** Samantha  port scan v_1.0 ***************\n")
print("ferramenta em desenvolvimento\n")
print("https://github.com/SamanthaGuilberth\n")
print(Fore.RED +"########################################################\n")

sair = 0

site = input(Fore.WHITE + f"Digite o site:\n")

while sair == 0:
	porta =input(Fore.WHITE + f"Digite a porta:\n")

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.2)
	code = client.connect_ex((site, int(porta)))

	if code == 0:
    		print(Fore.GREEN + f"porta {porta} Aberta")
	else:
	    	print(Fore.RED + f"porta {porta} Fechada")
	print(Fore.YELLOW + f"tecle ctrl+c para sair")
	continue
