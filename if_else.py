#general concept
A=30
B=32
if A<B:
	print("num2 is greater")

#if,elif,else
num1=int(input("Enter your first value: "))
num2=int(input("enter your second value: "))

if num1<num2:
	print("Second value is greater")
elif num1==num2:
	print("Two value are equal")
else:
	print("First value is greater")

#Short hand if
if B>A : print("B is greater")
 
#short hand if,else
print("Yes") if 5>3 else print("No")

a=44
b=33
print("a is greater") if a>b else print("equal") if a==b else("b is greater")

#While loop

i=1
while i<10:
	print(i)
	i+=1

#The break statement

it= 2
while it<22:
	print(it)
	if it==12:
		break
	it+=1
print("done")
#The continue statement

t=2
while t<20:
	t+=1
	if t==5:
		continue
	print(t)
else:
	print(" t is no longer")

	