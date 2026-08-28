class Robot:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduction(self):
        print(f"Hello I am {self.name} and i am {self.age} years old")

tom = Robot("Tom", 15)
jerry = Robot("Jerry", 17)

tom.introduction()
jerry.introduction()