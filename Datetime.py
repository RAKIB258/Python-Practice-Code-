import datetime

recent = datetime.datetime.now()
print(recent)

print(recent.year)
print(recent.month)
print(recent.day)
print(recent.strftime("%A"))

x= datetime.datetime(2020,2,25)
print(x)