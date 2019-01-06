This is a very concise version of all the help that is actually available. If you dont find what you are looking for here, then raise an issue on the github page.

Instructions for configuring the .config file:
	This file is located in <./h_data/.config>. You can open this file with any regular text editor.
	1.] Set the value of "Operate-using-port". This is the port that the script you are running will run off of.
	2.] Set the value of "Reach-to-port". This is the secondary port that you are going to try to connect to.
	3.] Set the value of "Reach-to-addr". This is the secondary IP address of the machine you are going to try to connect to.
	4.] Set the value of "Python3-executable-name" to the name of your python. This could be but is not limited to, "py", "py3", "python", "python3"...

Instructions for starting up a one time connection:
	1.] Start <S-listener.py> on the machine where the clock is located.
	2.] Start <S-main.py> on the controlling machine.
	Thats all.

Instructions for starting up a auto restarting connection:
	1.] Start <S-uptime-checker-auto-restarter> on the machine where the clock is located.
	2.] Start <S-main.py> on the controlling machine.
	If you cant connect to the listener, wait 10 seconds, for that is the restart cycle of the script.
	This script will check if the program is running every 10 seconds, and if it isnt, then it will restart the script.

Instructions for using the command line:
	In this command line, all commands start with ":", so "help" is not a command, but ":help" is a command.
	For a list of valid commands, type ":help".

Defaults:
	Bed time: 19:30:00
	Wake up time: 07:00:00
	Wake up length: 00:30:00