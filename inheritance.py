class Animal:  #parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"your name is {self.name} and your age is {self.age}")
obj1 = Animal("Lion", 12)



class Human(Animal):   #child class
    def __init__(self, name, age, number, group)    
        super().__init__(name, age)
        self.number = number
        self.group = group
        def info()


obj = Animal("Lion",12)
obj2 = Human("Akarsh",24, 1234567890, "B+")
obj2.info()
            

       