#Scope

def mFunc():
	x=30
	print(x)

mFunc()


def inside_S():
	x=3400
	def innerFunc():
		print(x)
	innerFunc()

inside_S()


val=893
def Global():
	val=30
	print(val)

#Define global
g=13
def global_define():
	global g
	g=10

Global()
print(val)
global_define()
print(g)
