#CLASS

class Hometown:
	def __init__(self,village,dist):
		self.village_name=village
		self.dist_name=dist


	def Edu(hosen):
		print("I went to "+hosen.village_name +" and "+ hosen.dist_name)

#INHERITANCE
class Student(Hometown):
	def __init__(self,village,dist,year):
		super().__init__(village,dist)
		self.grad_year =year

#OBJECT

obj1= Student("Dhania", "Bhola",2019)
obj1.Edu()
print(obj1.grad_year)


