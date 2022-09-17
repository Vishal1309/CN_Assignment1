# imports
import socket 
import os
import os.path as path
import crypto_client

# instantiating socket object
c = socket.socket()
port = 4000 # host port 
c.connect(('localhost', port))  # instantiating the connection

client_dir = os.getcwd()  # the directory location of the client

def cwd(c):
	print(c.recv(1024).decode())

def ls(c):
	file_list = c.recv(1024).decode().split("$")
	print(file_list)

def cd(c, cmd_line):
	new_dir = cmd_line[1]
	c.send(new_dir.encode())
	print(c.recv(1024).decode())

def dwd(c, cmd_line, client_dir):
	file_name = cmd_line[1]
	encoding_type = '-pt'
	try:
		encoding_type = cmd_line[2]
	except:
		if encoding_type != '-pt' or encoding_type != '-sb' or encoding_type != 'tp':
			encoding_type = '-pt'

	c.send(encoding_type.encode())
	c.send(file_name.encode())

	err = c.recv(1024).decode() # receives ERR from server if there is a problem while downloading the file
	toBreak = False
	if err == 'OK':
		directory = path.join(client_dir, file_name)
		with open(directory, 'wb') as wfile:
			data = c.recv(1024)
			if not data:
				err = 'ERR'
				toBreak = True
				return toBreak
			wfile.write(data)
		wfile.close()
		if encoding_type == '-sb':
			crypto_client.substitute_decode(directory)
		elif encoding_type == '-tp':
			crypto_client.transpose_encryption(directory)
		elif encoding_type == '-pt':
			crypto_client.plain_text(directory)
		print(err)
	elif err == 'ERR': print(err)
	return toBreak

def upd(c, cmd_line, client_dir):
	file_name = cmd_line[1]
	encoding_type = '-pt'
	try:
		encoding_type = cmd_line[2]
	except:
		if encoding_type != '-pt' or encoding_type != '-sb' or encoding_type != 'tp':
			encoding_type = '-pt'

	c.send(encoding_type.encode())
	c.send(file_name.encode())

	directory = path.join(client_dir, file_name)
	if (path.isfile(directory) == False):
		print('ERR')
	else:
		if encoding_type == '-sb':
			crypto_client.substitute_encode(directory)
		elif encoding_type == '-tp':
			crypto_client.transpose_encryption(directory)
		elif encoding_type == '-pt':
			crypto_client.plain_text(directory)
		
		with open(directory, 'rb') as rfile:
			for data in rfile:
				c.sendall(data)
		rfile.close()
		print('OK')

		if encoding_type == '-sb':
			crypto_client.substitute_decode(directory)
		elif encoding_type == '-tp':
			crypto_client.transpose_encryption(directory)
		elif encoding_type == '-pt':
			crypto_client.plain_text(directory)

while True:
	cmd_line = input().split(' ')
	cmd_given = cmd_line[0].casefold()
	c.send(cmd_given.encode())

	if cmd_given.lower() == 'cwd': # get the server's working directory
		cwd(c)

	elif cmd_given.lower() == 'ls': # get the list of directories in the folder of cwd in server
		ls(c)

	elif cmd_given.lower() == 'cd': # change server's working directory to one mentioned by user, rseturns 'Invalid directory in the current folder' if error, OK if changed
		cd(c, cmd_line)
			
	elif cmd_given.lower() == 'dwd': # download file on server to client
		toBreak = dwd(c, cmd_line, client_dir)
		if toBreak:
			break
		
	elif cmd_given.lower() == 'upd': # upload file on client to server
		upd(c, cmd_line, client_dir)

	elif cmd_given.lower() == 'exit':
		break
		
	else:
		print('invalid command, type exit to quit')
	

c.close() # closing the socket connection
