# imports
import socket 
import os 
import os.path as path
import crypto_server

# instantiating socket object
s = socket.socket()  
print ("socket created")

port = 4000 # host port 

s.bind(('localhost', port))  
print ("socket binded to %s" %(port))
 
s.listen(5) 
print ("socket is listening") 

c, addr = s.accept() # creating the connection object
print ('connection to:', addr )

cwd_server = os.getcwd() # to get the current working directory of the terminal


def cwd(c, cwd_server):
      c.send(cwd_server.encode())

def ls(c, cwd_server):
      toSend = ''
      list_dir = os.listdir(cwd_server)
      for dir in list_dir:
            toSend += dir + '$'
      toSend = toSend[:-1]
      c.send(toSend.encode())

def cd(c, cwd_server):
      final_dir = c.recv(1024).decode()
      try:
        os.chdir(final_dir)
        cwd_server = os.getcwd()
        c.send('OK'.encode())
      except:
        c.send('Invalid directory in the current folder'.encode())
      return cwd_server

def dwd(c, encoding_type, directory, err):
      c.send(err.encode())
      if encoding_type == '-sb': # substitute encoding
        crypto_server.substitute_encode(directory)
      elif encoding_type == '-tp': # transpose encoding
        crypto_server.transpose_encryption(directory)
      elif encoding_type == '-pt': # plaintext encoding
        crypto_server.plain_text(directory)
        
      with open(directory, 'rb') as rfile: 
        for data in rfile:
          c.sendall(data)
      rfile.close()

      if encoding_type == '-sb': # substitute encoding
        crypto_server.substitute_decode(directory)
      elif encoding_type == '-tp': # transpose encoding
        crypto_server.transpose_encryption(directory)
      elif encoding_type == '-pt': # plaintext encoding
        crypto_server.plain_text(directory)

def upd(c, cwd_server):
    encoding_type = c.recv(1024).decode()
    file_name = c.recv(1024).decode()
    directory = path.join(cwd_server, file_name)
    toBreak = False
    with open(directory, 'wb') as wfile:
      data = c.recv(1024)
      if not data:
          toBreak = True
          return toBreak
      wfile.write(data)
    wfile.close()
    
    if encoding_type == '-sb':
      crypto_server.substitute_encode(directory)
    elif encoding_type == '-tp':
      crypto_server.transpose_encryption(directory)
    elif encoding_type == '-pt':
      crypto_server.plain_text(directory)
    return toBreak

while True:
  cmd_given = c.recv(1024).decode()

  if cmd_given.lower() == 'cwd': # send current working directory 
    cwd(c, cwd_server)

  elif cmd_given.lower() == 'ls': # send list of directories on the current working directory
    ls(c, cwd_server)
    
  elif cmd_given.lower() == 'cd': # change the current working directory to the mentioned directory or return invalid directory
    cwd_server = cd(c, cwd_server)


  elif cmd_given.lower() == 'dwd': # sending file from server to client
    encoding_type = c.recv(1024).decode()
    file_name = c.recv(1024).decode()
    directory = path.join(cwd_server, file_name)
 
    if path.isfile(directory):
      err = 'OK'
      dwd(c, encoding_type, directory, err)
      
    else: err = 'ERR'; c.send(err.encode())

  elif cmd_given.lower() == 'upd': # receive filee from server
    toBreak = upd(c, cwd_server)
    if toBreak:
          break
    
  elif cmd_given.lower() == 'exit':
    c.close()
    
  else: 
    continue

s.close() # closing the socket connection
