import socket, argparse, sys

#connect addr
HOST = "localhost"

#args and help
p = argparse.ArgumentParser(description='Simple client programm to send/receive messages')
p.add_argument('-P', '--PORT', type=int, help='enter port bla bla')
p.add_argument('-p', '--post', help='enter message to store/update on server,type [--queue] and digit after message to blablabla')
p.add_argument('-g', '--get', action='store_true', help='receive message, type [--queue] and digit to recieve blablalba')
p.add_argument('-q', '--queue', help='queue number, number should be in range 1-10000')



#main func to connect/post/get
def client(port, ge=False, po=None, qu=None):
	
	#doctest for main functions
	'''
	>>> client(False, 'test0', None)
	[done]
	>>> client(False, 'test1', '1')
	[done]
	>>> client(False, 'test2', '1')
	[done]
	>>> client(True, None, '1')
	test2
	[done]
	>>> client(True, None, None)
	test0
	[done]
	>>> for i in range(100):
	... 	client(False, '0', None)
	>>> client(False, '0', None)
	<BLANKLINE>
	'''
	#sock connect and data formatting 
	con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	get = 'get' if ge else False
	post = 'post:'+po if po else False
	if qu and int(qu) not in range(10001):
		p.print_help()
		exit()
	queue = ':'+qu if qu else False
	data = ''.join([i for i in (get,post,queue) if type(i) == str])
	#print('DATA HERE : ', data)
	if data:
		con.connect((HOST, port))
		con.send(bytes(data, "utf-8"))
		r = str(con.recv(1024), "utf-8")
		print(r)
		con.close()
	


if __name__ == '__main__':
    if len(sys.argv[:])<2:
        p.print_help()
        exit()
	#exec
    client(p.parse_args().PORT, p.parse_args().get, p.parse_args().post, p.parse_args().queue)