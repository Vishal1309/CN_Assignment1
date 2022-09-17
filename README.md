## Computer Networks Assignment 1
The pdfs 19110207_CN_A1_P1.pdf, 19110207_CN_A1_P2.pdf, and 19110207_CN_A1_P3.pdf contain answers to the respective parts.

### Steps to run
Install all required packages (socket, os)
Clone this repository.

There are two separate folders client and server. Open these folders in separate terminals, and run connect_server.py and connect_client.py, in this order. The connection will be established. You can now run the commands on the running client. As a sample, the data folder contains a text file dummy.txt, which can be downloaded to the client, and then uploaded to the server in a different folder. we do not delete files from their original location upon download or upload.

To use the different encoding modes, use -pt (for plain text), -tp (for transpose) or -sb (for subtstitution encoding) after the file name. 

Example: dwd dummy.txt -tp or upd dummy.txt -pt. Plaintext is the default encoding if no encoding type is provided
