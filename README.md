Simple transfer any files between client and server.
Wrote on the Python under the Ubuntu.


sample executing:
# ./server.py
Listening port 8080
Connected: ('aaa.zzz.yyy.xxx', 63491)
File: udp.pcap Size: 6946816
File received. Size: 6946816
Calculating md5...
abd85e9fdf0d504f10a97f53d6f54544
Listening port 8080

# ./client.py <filename>
Filename: udp.pcap Size:6946816
31
I'm waiting MD5 hash from server
abd85e9fdf0d504f10a97f53d6f54544
abd85e9fdf0d504f10a97f53d6f54544
File was sent is successful
#

If you have some question, please ask me.
