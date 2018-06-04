'''
109. Write a program to Accept Three Digits and Print all Possible Combinations from the Digits
'''
li=list()
i=0
while i < 3:
	li.append(int(input("enter digit: ")))
	i=i+1
for i in li:
	for j in li:
		if li.index(i)!=li.index(j):
			for k in li:
				if li.index(k)!=li.index(i) and li.index(k) != li.index(j):
					print(i*100+j*10+k)
					