num="9378"
a="Rakib"

def myFun():
	print("The numvber is :"+num)
	global x
	x="Rakib"

myFun()
print("The name is a "+x)

print(type(num))

print(type(x))
g=memoryview(bytes(5))
print(g)

x=63.83
y=737
z="Rakib"

print(type(x))
print(type(y))
print(type(z))

def test():
	a,b,c,d=2+5j,4.7,'a',80
	print(type(a))
	print(type(b))
	print(type(c))

	print(int(b))
	print(float(d))


test()

import random
print(random.randrange(0,100))

k=int(num)
print(k)

value= input("Enter your name: ")
print(value)

val=input("Enter raw input value")
print(val)
