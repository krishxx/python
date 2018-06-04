'''Question: 82

Please write a program to compress and decompress the string 
"hello world!hello world!hello world!hello world!".



Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.


Solution:
'''
import zlib
s = b"hello world!hello world!hello world!hello world!"
#s=123
t = zlib.compress(s,3)
print( t)
print("****************************")
print(zlib.decompress(t))

