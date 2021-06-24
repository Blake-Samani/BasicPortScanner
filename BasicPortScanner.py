
import socket
import termcolor
#termcolor is for printing in different colors



def scan(target, ports):
	print(termcolor.colored(('\n' + 'Starting scan for ' +str(target)), 'green'))
	for port in range (1,ports):
		scan_port(target,port)

def scan_port(ipaddress, port):
	try:
		sock = socket.socket() #creating and initializing a socket object
		sock.connect((ipaddress,port)) #connect to a port, requires ip address and port
		print("Port Opened " + str(port))
		sock.close()
	except:
		pass



targets  = input("Enter targets to scan(split by a comma):  ") #user inputs string, IP addresses
ports = int(input("Enter how many ports you want to scan: ")) #num of ports to scan, convert to int to remove type errors when iterating through ports in scan function
if ',' in targets:
	print(termcolor.colored(("Scanning multiple targets"), 'green'))
	for ip_addr in targets.split(','): #iterate through ip addresses given by user and splitting by commas
		scan(ip_addr.strip(' '),ports) #remove whitespace before entering into function
else:
	scan(targets,ports) #if they only input one ip address