# example of Employee Constructor
class Employee:
    def __init__(self,id,name,sal,desg):
        self.id=id
        self.name=name
        self.sal=sal
        self.desg=desg
    def emp(self):
        print("Employee ID:{}\n Employee name:{}\n Employee salary:{}"
              "\n Employee designation:{}\n".format(self.id,self.name,self.sal,self.desg))
e1=Employee(101,"bhushan",25500,"software engineer")
e1.emp()
print("--------------------------------------")
e1=Employee(102,"shubham",78500,"IT Engineer")
e1.emp()