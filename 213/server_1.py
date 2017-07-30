import socketserver, argparse

p = argparse.ArgumentParser(description='Simple server programm to send/receive messages, only 100 messages cant be in QUEUE blablabla')
p.add_argument('-p', '--port', type=int, help='PORT number')

#message container
messages = []

#custom socket handler to receive/store data from client
class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = str(self.request.recv(1024), 'utf-8')
        l = [i for i in self.data.split(':' if ':' in self.data else None)]
        if l[0] == 'get':
            if len(l)>1:
                self.data = messages.pop(int(l[1]))
                self.data = bytes(self.data+'\n[done]', 'utf-8')				
            else:
                
                self.data = messages.pop(0)
                self.data = bytes(self.data+'\n[done]', 'utf-8')
                
        if l[0] == 'post':
            if len(messages)<=100:
                if len(l) == 2:
                    messages.append(l[1])
                    self.data = bytes('[done]', 'utf-8')
                if len(l) == 3:
                    messages.insert(int(l[2]), l[1])
                    self.data = bytes('[done]', 'utf-8')
        self.request.sendall(self.data)
            

#exec			
if __name__ == '__main__':
    
    if not p.parse_args().port:
        p.print_help()
        exit()
    HOST, PORT = 'localhost', p.parse_args().port		
    s = socketserver.TCPServer((HOST, PORT), MyHandler)
    print("server is up", PORT)
    s.serve_forever()