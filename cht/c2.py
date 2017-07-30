import socket
import sys

HOST, PORT = "localhost", 9999
#print('Enter your name:')


# Create a socket (SOCK_STREAM means a TCP socket)
#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#try:
	# Connect to server and send data
	#sock.connect((HOST, PORT))
	#sock.sendall(bytes(data + "\n", "utf-8"))

	# Receive data from the server and shut down
	#received = str(sock.recv(1024), "utf-8")
#finally:
	#sock.close()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
name = None
def client():
	name = None
	if not name:
		name = input('Enter your name: ')
		sock.sendall(bytes(name+ "\n", "utf-8"))
		received = str(sock.recv(1024), "utf-8")
		print(received)
		name = input('Enter your name: ')
		sock.sendall(bytes(name+ "\n", "utf-8"))
		received = str(sock.recv(1024), "utf-8")
		print(received)
	data = input('Enter your message: ')
	sock.sendall(bytes(data + "\n", "utf-8"))
	#msg = str(sock.recv(1024), "utf-8")
	print(str(sock.recv(1024), "utf-8"))
	#client()
client()
	#if __name__ == "__main__":

#	sys.exit(client())	
#print("Sent:     {}".format(data))
#print(received)