import socket, argparse

#connect addr
host = "localhost"

#args and help
p = argparse.ArgumentParser(description='Simple client programm to send/receive messages')
p.add_argument('-P', '--PORT', type=int, help='enter port bla bla')
p.add_argument('-p', '--post', help='enter message to store it on server, all symbols/digits allowed (EXCEPT '|||'),type [-q, --queue] and digit after message to blablabla')
p.add_argument('-g', '--get', action='store_true', help='receive message, type [-q, --queue] and digit to recieve blablalba')
p.add_argument('-q', '--queue', help='queue number, number should be in range 1-10000')



#main func	
def client(port, g=False, po=None, q=None):
	
	#post/get conv. funcs
	post = lambda x,y: bytes(x+'|||'+y, 'utf-8')
	get = lambda x: bytes(x, 'utf-8')

	if not q:
			q = '0'	
	#main func body		
	try:
		con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#get request
		if g and (int(q) in range(10001)):
			con.connect((host, port))
			data = get(q)
			con.send(data)
			recv = str(con.recv(1024), "utf-8")
			print(recv)
			con.close()
			return recv
		
		#post requst
		if po and (int(q) in range(10001)) and not '|||' in po:
			con.connect((host, port))
			data = post(po,q)
			con.send(data)
			recv = str(con.recv(1024), "utf-8")
			print(recv)
			con.close()
			return recv
			#p.print_help()
		#if port only or not any of post/get
		return p.print_help()
	except:
		p.print_help()
		
if __name__ == '__main__':
	#if not p.parse_args().PORT:
	#	exit(p.print_help())
	client(p.parse_args().PORT, p.parse_args().get, p.parse_args().post, p.parse_args().queue)
	
		
		