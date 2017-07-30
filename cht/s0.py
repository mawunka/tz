import socketserver

c_addr = []
c_names = {}
class MyTCPHandler(socketserver.BaseRequestHandler):
	"""
	The RequestHandler class for our server.

	It is instantiated once per connection to the server, and must
	override the handle() method to implement communication to the
	client.
	"""
	#c_ddr = []
	#c_names = {}
	def handle(self):
        # self.request is the TCP socket connected to the client
		self.data = self.request.recv(1024).strip()
		if not self.client_address[1] in c_addr:
			c_addr.append(self.client_address[1])
			c_name = str(self.data, 'utf-8')
			c_names[self.client_address[1]] = c_name
			self.data = bytes('Hello '+c_names[self.client_address[1]]+' !', 'utf-8')
		
		print("{} wrote:".format(self.client_address[1]))
		print(self.data)
        # just send back the same data, but upper-cased
		self.data = str(self.data, 'utf-8')
		self.data = bytes(c_names[self.client_address[1]]+': '+self.data, 'utf-8')
		self.request.sendall(self.data)

if __name__ == "__main__":
	HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
	server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
	server.serve_forever()