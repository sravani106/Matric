#number checking program
number=int(input('enter a number: '))
if number>0:
    print('number is positive')
elif number==0:
    print('number is zero')
else:
    print('number is negative')

#Fibbonaci Program
a=0
b=1
c=0
n=int(input("enter number of terms: "))
for i in range(n):
    print(a)
    c=a
    a=b
    b=c+b
print()

#Armstrong Number program
number=input('enter a number: ')
sum=0
if len(number)==3:
    for i in number:
        sum=sum+int(i)**3
    if sum==int(number):
            print(number,'is armstrong number')
    else:
        print(number,"is not a armstrong number")
else:
    print("enter a three digit number")
