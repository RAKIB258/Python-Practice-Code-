#creating Function

def my_func():
	print("Function Practice")

my_func()

#Arguments

def func(value):
	print(value+" is good")

func("Rakib")  #Function call
func("Hanif")
func("Nazmul")

#parameter
def func_para(f_name, l_name):
	print(f_name+ " "+ l_name)

func_para("Rakib", "Ahmed")  #functiona call
func_para("Nazmul", "Hossain")

#func_para("Shemul")  ..If I use two parameter but pass the value one it didn't generate any value and show error

#Multiple argument pass
def staric_para(*age):
	print("Your name is :"+ age[0])
	print("Your age is :" +age[1])

staric_para("Rakib","23","Bhola")  #generate the index number 1st
staric_para("Sakil","23","Dhaka")

#Keyword aguments
def my_fu(ch1, ch2, ch3):
	print("the youngest child is: "+ch2)

my_fu(ch1="Rakib",ch2="Nazmul",ch3="Shemul")

#Arbitary Keywords
def funct(**name):
	print("It's name is: "+name["l_name"])
funct(f_name="Tulatuli", l_name="Dhonia")

#Default paraeter value
def test(country="Bangladesh"):
	print("I am from "+country)

test("Norway")
test("USA")
test("Canada")

#Passing a list as an arguments
def my_f(food):
	for x in food:
		print(x)

fruits=["Guava","orange","Banana"]
my_f(fruits)

def ret_val(x):
	return 7*x

print(ret_val(2))
print(ret_val(4))
print(ret_val(3))

#recursion
def recur(k):
	if (k>0):
		result=k+recur(k-2)
		print(result)
	else:
		result =0
	return result
print("\n\nrecursion example result is: ")
recur(4)

#LAMBDA

x= lambda a: a+20
print(x(5))
print("\nDone!!!!!!!!!!")

x= lambda a, b: a*b
print(x(5,6))
print("\nDone!!!!!!!!!!")

y= lambda a, b,c, d: (a+b)*c+d
print(y(1,2,3,4))
print("\nDone!!!!!!!!!")


def myfunc(n):
	return lambda a: a*n
mydouble= myfunc(2)
print(mydouble(22))
print("\nDone!!!!!!!!!!")

def tripler(c):
	return lambda a: a*c

mydoubler= tripler(2)
mytripler= tripler(3)

print(mydoubler(12))
print(mytripler(10))



