#!/usr/bin/python

import socket
import os, hashlib, sys

def md5(fname):
    hash = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash.update(chunk)
    return hash.hexdigest()

def getSize(filename):
    st = os.stat(filename)
    return st.st_size

def padGen(num):
    pad=''
    for i in range (num):
	pad +='+'
    return pad

def padding(name):
    new_name=''
    if len(name) < 16:
	new_name=padGen(15-len(name))+name
	return new_name


sock=socket.socket()
try:
    sock.connect(('194.58.88.242',8080))
except:
    print "Cannot connect to server";
    exit()

print "Connected"

path='/home/alex/Desktop/python/'
filename=sys.argv[1]
fullpath=path+filename
filesize=getSize(fullpath)
print "File: " +path +filename + " Size: " + str(filesize)


msg=padding(filename)+":"+padding(str(filesize))
print len(msg)
sock.sendall(msg)

md5data=md5(fullpath)
file = open(fullpath,"rb")
while 1:
    buff=file.read(1024)
    sock.sendall(buff)
    if len(buff) == 0:
	print "I'm waiting MD5 hash from server..."
	data=sock.recv(128)
	print data;
        break

print md5data;
if md5data == data:
    print "File was sent succesfull";
else:
    print "File was sent failed"
file.close()
sock.close();
