
print("Loading your data.........................")

class student:
    uni= "ISTT"

    def __init__(self,Name,ID,year):
        self.Name=Name
        self.ID= ID
        self.year=year

    def Display(self):
        print("Student Name: ",self.Name)
        print("University Name: ",self.uni)
        print("Student's ID is: ",self.ID)
        print("Year of Admitted: ", self.year)

student1= student(Name=input("Name:"),
                  ID=input("ID:"),
                  year=input("Year:"))

student2= student(Name=input("Name:"),
                  ID=input("ID:"),
                  year=input("Year:"))

student3= student(Name=input("Name:"),
                  ID=input("ID:"),
                  year=input("Year:"))

A=str(input())
B=int(input())
C=int(input())

student4=student(A,B,C)
student4.Display()

student1.Display()
student1.Display()
student1.Display()