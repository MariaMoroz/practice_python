# OOP
class Cat:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        print(f"Cat {self.name} is being initialized and says Meow!")

    def say_meow(self):
        print(f"{self.name} says Meow!")

    def print_name(self):
        print("This is", self.name)

    def print_age(self):
        print(self.name, "is", self.age, "years old")


    def print_weight(self):
        print(f"{self.name}'s weight is {self.weight} lbs")

    def eat(self, food="food"):
        print(f"{self.name} ate {food}")

    def eat_a_lot(self, food="food"):
        self.weight += 0.25
        print(f"{self.name} ate a lot of {food} and gained quoter pound")



black_cat = Cat("Tom", 2, 8)
print(black_cat)
black_cat.print_name()
black_cat.print_age()
black_cat.print_weight()
black_cat.eat()

black_cat.eat_a_lot()
black_cat.print_weight()