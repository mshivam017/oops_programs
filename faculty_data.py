class Faculty:
    def __init__(self,a,b,c):
        self.id = a
        self.name = b
        self.salary = c

    def display(self):
        print("\nFaculty Id: ", self.id)
        print("Name: ", self.name)
        print("Salary: ", self.salary)


a = Faculty(int(input("\nFaculty ID: ")), input("Faculty Name: "), float(input("Faculty Salary: ")))
a.display()

b = Faculty(18, "Surya", 1222)
b.display()
