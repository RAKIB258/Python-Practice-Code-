name=["Rakib", "Hanif","Sakil","Mejbah","Riaz"]

for na in name:
	print(na)

#print the item	
for i in "Rakib":
	print(i)

#Break the stetement

for item in name:
	if item=="Mejbah":
		break
	print(item)
print("Doneeeeeeeeeee")
#The continue statemnt in for loop

for it in name:
	if it=="Sakil":
		continue
	print(it)
print("Doneeeeeeeeeee")

# range() funtion

for i in range(12):
	print(i)
print("Doneeeeeeeeeee")

for new in range(2,32,2):
	print(new)

#Nested for loop
name2=["Bhola","23","CSE"]
rs=[2.98,3.2,2]

for i in name:
	for j in name2:
		for k in rs:
			print(i,j,k)

#Pass statement
for x in [2,4,5,8]:
	pass # No value return