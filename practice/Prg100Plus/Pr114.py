'''
114. Write a program to Check if a Number is a Palindrome
'''
#num=input("enter number to check if it is palindrome: ")
num=input("enter number")
i=0
start=0
end=len(num)-1
palindrome=1
while i < int(len(num)/2):
	if num[start+i]!=num[end-i]:
		print("not a palindrome")
		palindrome=0
		break
	i=i+1
if(palindrome==1):
	print("Palindrome")
	
