import socket, select, string, sys


def cl() :
    sys.stdout.write('<Me>: ')
    sys.stdout.flush()

if __name__ == "__main__":
    if len(sys.argv)!=2:
        print('***Usage: $python client.py <PORT>')
        sys.exit()
    host = "localhost"
    port = int(sys.argv[1])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # connect
    try :
        s.connect((host, port))
    except :
        print('Can\'t connect')
        sys.exit()

    print('Connected to chat.')
    cl()
    input = input()

    while 1:
        s_list = [sys.stdin, s]
        rsock, wsock, errsock = select.select(s_list , [], [])
        for sock in rsock:
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print('\nDisconnected from chat server')
                    sys.exit()
                else :
                    sys.stdout.write(data)
                    cl()
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                cl()