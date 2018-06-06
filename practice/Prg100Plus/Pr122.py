'''
122. Write a program to Compute Simple Interest Given all the Required Values
'''
pri=int(input("enter principle amount: "))
roi=int(input("enter ROI: "))
dur=int(input("enter Duration in years: "))
int=pri*roi*dur/100
print(int)