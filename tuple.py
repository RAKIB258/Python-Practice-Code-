tu=('Rakib','Dhaka','Bhola',"Tulatuli",23)
print(tu)

print(tu[2])
print(tu[-1])

print(tu[1:3])
print(tu[-3:-1])

for x in tu:
	print(x)

if "Dhaka" in tu:
	print("Yes")


print(len(tu))

ad=("thuijs")
print(type(ad))

ass=("thsis")
print(type(ass))

new_tuple=ad+ass
print(new_tuple)

th=tuple(("server","domain","sir"))
print(th)


#SET

st={"New","ols","djdk",90}
print(st)

for i  in st:
	print(st)
print("New" in st)

st.add("Rakib")
print(st)

st.update(["Rakib","Ahmed","Bhola"])
print(st)
print(len(st))


st.remove("Bhola")
print(st)

st.discard("abi")
print(st)

st2=st.pop()
print(st)

num1={1,2,3,8,4}
set1=st.union(num1)
print(set1)

st.update(num1)
print(st)

cons=set(("Apple","banana","Orange","jackf"))
print(cons)
print(type(cons))