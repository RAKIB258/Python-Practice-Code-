this_list=["Rakib","CSE","ISTT","Dhaka"]
print(this_list)


li=['a','b','c','d','f',6,2,9,7]

print(this_list[3])

print(li[-1])

print(li[1:2:6])
print(li[:5])

print(li[4:])

print(li[-5:-1])

li[3]="Rakib"
print(li)

for i in li:
	print(i)

if "Rakib" in li:
	print("Yes")

print(len(this_list))
print(len(li))

li.append("hosen")
print(li)

li.insert(2,"sabudj")
print(li)

li.remove("f")
print(li)

li.remove('hosen')
print(li)

print(li)
print(li.pop())

print(li)



new_li=li+this_list
print(new_li)

for x in this_list:
	li.append(x)

print(li)

li.extend(li)
print(li)