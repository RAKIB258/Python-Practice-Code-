cars=["ford","volvo","BMW"]

car1="anvdjjd"
car2="bdckddddkd"
car3="cdfnddfdfddfddk"

for i in car1:
	print(car1)

x=cars[0]
cars[0]="Toyota"
print(x)
print(cars)

for i in cars:
	print(i)

#Adding array element

cars.append("Marcidiz Benz")
print(cars)

#removing cars

cars.pop(2)
print(cars)

cars.remove("volvo")
print(cars)

arr=[
["Bhola","Barisal","Dhaka"],
[122,444,555],
["CSE","EEE","Civ"]]

print(arr)
print(len(arr))
print(type(arr))

print(arr[0])
print(arr[2][1])
print(arr[0][2][2])