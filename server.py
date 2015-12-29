#!/usr/bin/python

import socket, sys
import string,re
import base64
import hashlib

def md5(fname):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()

def delPad(name):
    end = name.rfind('+')
    return name[end+1:]

buffer_size = 1024;
sock = socket.socket()

try:
    sock.bind(('', 8080))
except socket.error:
    print "Cannot bind socket";
    sys.exit()

while True:
 print "Listening port 8080";
 sock.listen(2)
 conn, addr = sock.accept()
# conn.settimeout(60)
 print 'Connected:', addr
 msg=conn.recv(31)
 filename,filesize=msg.split(":")
 filename = delPad(filename)
 filesize = delPad(filesize)

 print "File: "+filename+ " Size: "+ str(filesize)

 k=0;
 file = open(filename,'wb')
 #while True:
 while (int(k) < int(filesize)):
    buff = conn.recv(buffer_size)
    if buff:
	if (len(buff)==buffer_size):
    	    file.write(buff)
	    k += buffer_size
	elif (len(buff) < buffer_size) and (len(buff) >0):
    	    file.write(buff)
	    k += len(buff)
    else:
	print "NULL"
	break

 file.close()
 print "File received. Size: " + str(k)
 print "Calculating md5..."
 md5data=md5(filename)
 conn.send(md5data)
 print md5data





"""
    else:
	print "File have received. Size:" +str(k)
	md5data=md5(filename)
	conn.send(md5data)
	print md5data

#	print "Data is not found. Exit"
	file.close()
	break
"""
conn.close()

"""
# print "receiving.." + str(k);
 buff = conn.recv(64)
 k +=len(buff)
# if len(buff) == 0:


conn.close()
# print buff
"""
"""
	if len(buff)==64:
	    file.write(buff)
	    k +=len(buff)
	elif (len(buff)<64) and (len(buff)>0):
	    file.write(buff)
	    k +=len(buff)
	elif len(buff)==0:
	    print "File have received. Size:" +str(k)
	    md5data=md5(filename)
	    conn.send(md5data)
	    print md5data
	    break
"""


