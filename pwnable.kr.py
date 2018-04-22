import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pwnable.kr", 9007))

# Continue receiving msg until you break loop
while True: 
    # Every time received 2048 byte data.
    data = s.recv(2048)
    
    # target msg
    # or you could break while loop with qC for new for loop 
    if data.startswith("N="):
        qus = data.strip().split(' ')
        qN = qus[0][2:] # N
        qC = qus[1][2:] # C

        # Do something you want to do.
        # algorithm, send msg ... etc.
        
    # may be you need add determine about answer msg
