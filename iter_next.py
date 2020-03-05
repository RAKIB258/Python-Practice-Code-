#iter()

mytuple =("Dhaka", "Bhola", "Barisal")
myit =iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

li="Rakib"
it = iter(li)

print(next(it))
print(next(it))
print(next(it))

for x in mytuple:
	print(x)


class myNumbers:
	def __iter__(self):
		self.val=1
		return self

	def __next__(self):
		x = self.val
		self.val+=1
		return x

myclass = myNumbers()
myi = iter(myclass)

print(next(myi))
print(next(myi))
print(next(myi))