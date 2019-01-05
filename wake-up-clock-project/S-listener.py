import socket as socket
import _thread as thread
import h_clocklib as clocklib
import time as time

def updateLastUptime():
    while (1):
        time.sleep(0.5)
        file = open('./h_data/lastuptime-listener.txt', 'w')
        file.write(str(clocklib.timeget.localtime()))
        file.close()

thread.start_new_thread(updateLastUptime, ())

machine = socket.socket()
port = int(str(open('./h_data/config.txt').read()).split('\n')[0].split(':')[1])
machine.bind(('', port))
machine.listen(5)
c, addr = machine.accept()

print ('Socket is connected to {}.'.format(addr))

commands = [':exit;', ':help;', ':man;', ':echo;', ':dataquery;']

class data:
    data = {}

while (1):
    rcvData = c.recv(1024).decode()
    sendData = 'Data was recived'
    if (rcvData in commands):
        sendData = 'Command was found but it has no script.'
    elif (rcvData.startswith(':')):
        sendData = 'Unknown command.'
    if (rcvData == ':exit;'):
        sendData = 'Aborting listener...'
        break
    elif (rcvData == ':help;'):
        sendData = '''
LIST OF COMMANDS (* indicates a work in progress command):

:exit - Exits the shell and kills the active connection between the connected script and the listener.
:help - Returns a list of valid commands that can be used with the listener.
*:man <command> - Returns the manual page for the specified command.
:echo <string> - Prints a string to the listener's command line.
:dataquery <key> - Returns the value assigned to the key, in the file <./h_data/.data>
:setdata <key> <value> - Sets the value of the designated key for the dict located in <./h_data/.data>
:laudti - (Last update time); Returns the contents of the file <./h_data/.lastuptime-listener>
:datavardump - Returns all the values of the items in <./h_data/.data>
'''
    elif (rcvData.split(' ')[0] in [':man', ':man;']):
        sendData = '''
This command is a work in progress and does not work yet.
'''
    elif (rcvData.split(' ')[0] == ':echo'):
        print (rcvData[len(':echo') + 1:])
        sendData = 'Echoed.'
    elif (rcvData.split(' ')[0] == ':dataquery'):
        query = rcvData.split(' ')[1].split(';')[0]
        sendData = 'Invalid key.'
        exec('data.data = {}'.format(str(open('./h_data/data.txt').read())))
        try:
            sendData = str(data.data[query])
        except KeyError:
            pass
    elif (rcvData == ':dataquery;'):
        sendData = 'Missing argument for <:dataquery>'
    elif (rcvData == ':laudti;'):
        sendData = str(open('./h_data/lastuptime-listener.txt').read())
    elif (rcvData == ':setdata;' or (rcvData.split(' ')[0] == ':setdata' and rcvData.count(' ') < 2)):
        sendData = 'Missing arguments for <:setdata>'
    elif (rcvData.split(' ')[0] == ':setdata'):
        exec('data.data = {}'.format(str(open('./h_data/data.txt').read())))
        data.data[str(rcvData.split(' ')[1])] = rcvData.split(' ')[2].split(';')[0]
        sendData = 'Set <data.data[{}]> to <{}>'.format(rcvData.split(' ')[1], rcvData.split(' ')[2].split(';')[0])
        file = open('./h_data/data.txt', 'w')
        file.write(str(data.data))
        file.close()
    elif (rcvData == ':datavardump;'):
        exec('data.data = {}'.format(str(open('./h_data/data.txt').read())))
        sendData = '\n\n'
        for key in data.data:
            sendData += 'data.data["{}"] = {}\n'.format(key, data.data[key])
        sendData += '\n'
    c.send(sendData.encode())

machine.close()