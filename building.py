class Building:
    def __init__(self):
        self.no=int(input("Building Number :"))
        self.name=input("Building Name :")
        self.floor=int(input("Building Total Floor :"))
    def show(self):
        print("number :\t",self.no)
        print("name :\t",self.name)
        print("Total Floor :\t",self.floor)
c=Building()
print("-------------")
c.show()