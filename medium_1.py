print("Revision")

str1= "This is a Revision of Python programming."
print(str1)

str2="THis_a_sa_book"

print(str1[1:22])

print(str2[1:-7])

print(len(str1))
print(len(str2))

sp="  Shemul  seikh"
print(sp.strip())

print(sp)

vari="MY NAME IS RAKIB. SHEMUL IS A GOOD BOY. This is A Biri."
print(vari.lower())

print(vari.upper())

name="Kala Mia"
print(name.replace("Kala","Sada"))

nam="Shemul, Seikh"
print(nam.split(","))

txt="Tthis ius sbdf ndsfdsfblsdaf shemul fdssnflkjds shemul jbflbsdfbfs  jdhfdihfi dhdsfd shemul"
x= "shemul" in txt
print(x)

y="shemul" not in txt
print(y)

z=nam+"    "+txt
print(z)

age=23
print("My age is 10 years {}".format(age))

quantity=2
per=20
total=40
msg="I purchase {} book which is {} Tk. and total {}"
print(msg.format(quantity,per,total))

tabb="We arae \"boy\" is "
print(tabb)

#Boolean Value

print(10>9)
print(8>83)

r=10
e=33

if r<e:
	print("r is less than e")
else:
	print("r is greater than e")

print(bool("helo"))
print(bool(13))

xo="hsdsk"
io=2424
print(bool(xo))
print(bool(io))


print(bool("ABsjs"))
print(bool(227))
print(bool([2782, "hkshd"]))

print(bool(False))
print(bool(True))


class myClass():
	def _len_(self):
		return 0

myobj=myClass()
print(bool(myobj))

x=200
print(isinstance(x,int))

