dic={
	"Rakib": "ISTT",
	"Shahidul": "AIUB",
	"Navid": "CSE",
	"Asif": "BUET",
	"Year": "2020"
}

print(dic)
print(type(dic))

#Access items
print(dic["Navid"])
print(dic["Rakib"])

#Access items using get() method
print(dic.get("Shahidul"))

#The the items's value 
print(dic["Year"])
dic["Year"]=2016
print(dic["Year"])

#Loop through a Dictionary to print key names

for keys in dic:
	print(keys)

#print values through for loop

for val in dic:
	print(dic[val])

#We can use values() function to print values
for va in dic.values():
	print(va)

#Print keys and Values throug items() function
for k, i in dic.items():
	print(k, i)

#Check if key exit
if "Rakib" in dic:
	print("yes")
else:
	print("no")

#Dictionary lenth
print(len(dic))

#Removing items
dic.pop("Rakib")
print(dic)

print(len(dic))

#Pop last items from the dictionary
dic.popitem()
print(dic)
print(len(dic))

#copy a dictionary
new_dic= dic.copy()
print(new_dic)

#clear dictionary
dic.clear()
print(dic)

#Nested Dictionary
student_data={
	"name1":{
	"Rakib":"Dhaka",
	"Dept": "CSE",
	"Birth":"1996",
	},
	"name2":{
	"Nazmul":"Bagerhat",
	"Dept": "Political Science",
	"Birth": "1993",
	},
	"name3":{
	"Shemul":"Dhaka",
	"Dept": "Economics",
	"Birth": "1998",
	}
}

print(student_data)
print()

#Create Dictionaryn that contain other dictionary

A= {
	"name":"Fahim",
	"e-mail":"fahim@gmail.com"
}
B={
	"name":"Mamun",
	"e-mail":"mamun@gmail.com"
}
C={
	"name":"Kaniz",
	"e-mail":"Kaniz@gmail.com"
}
my_dic={
	"Fahim":A,
	"Mamun":B,
	"Kaniz":C,
}

print(my_dic)
print(my_dic["Fahim"])

#Dictionary using dict() constractor
this_Dic=dict(Bangladesh="Dhaka",USA="Wasington DC",Canda="Toronto")
print(this_Dic)


