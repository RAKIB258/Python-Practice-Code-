try:
	print(x)

except:
	print("An exception occured")


#Many exception
try:
	print(val)

except NameError:
	print("Variable val is not defined")
except:
	print("Something else went wrong")


#Else

try:
	print("hello")
except:
	print("Something went wrong")
else:
	print("Nothing went wrong")

