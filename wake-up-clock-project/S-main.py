import socket as socket

cnct_IP = str(str(open('./h_data/config.txt').read()).split('\n')[2].split(':')[1])
cnct_PORT = int(str(open('./h_data/config.txt').read()).split('\n')[1].split(':')[1])

try:
    machine = socket.socket()
    machine.connect((cnct_IP, cnct_PORT))
except:
    input('Listener is down at the current time.')
    machine.close()
    exit()

try:
    while (1):
        sendData = input(str('{}:{} >>> '.format(cnct_IP, cnct_PORT))) + ';'
        machine.send(sendData.encode())
        recData = machine.recv(1024).decode()
        print ('Response from {}:{} - "{}"'.format(cnct_IP, cnct_PORT, recData))
        if (sendData == ':exit;'):
            print ('Listener on {}:{} has been killed. Press enter to exit the program or do Ctrl+C to exit.'.format(cnct_IP, cnct_PORT))
            break
except EOFError:
    print ('Exiting...')
    machine.close()
except KeyboardInterrupt:
    print ('Exiting...')
    machine.close()


machine.close()