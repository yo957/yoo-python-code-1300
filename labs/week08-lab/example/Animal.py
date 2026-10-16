<<<<<<< HEAD
# Parent class (Base class)ตัวอย่างของคลาสพ่อแม่
=======
# Parent class (Base class)
>>>>>>> upstream/main
class Animal:
    
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
    def make_sound(self):
        print(f"{self.name} makes a sound")

# Child class (Derived class)
<<<<<<< HEAD
class Dog(Animal):#การถ่ายถอดมาจากแม่มี3อย่างของแม่
    def __init__(self, name, breed): #มีข้อมูล3ตัวในการทําการ
=======
class Dog(Animal):
    def __init__(self, name, breed):
>>>>>>> upstream/main
        super().__init__(name, "Canine")  # Call parent constructor
        self.breed = breed
    
    # Method overriding
    def make_sound(self):
        print(f"{self.name} barks: Woof!")
    
    # New method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball")

<<<<<<< HEAD
class Cat(Animal): #ก็อป7อย่างมาที่ตัวเอง
=======
class Cat(Animal):
>>>>>>> upstream/main
    
    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} meows: Meow!")
    
    def climb_tree(self):
        print(f"{self.name} is climbing a tree")

# Usage
dog = Dog("Max", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

dog.eat()        # Inherited method
dog.make_sound() # Overridden method
dog.fetch()      # Dog-specific method

cat.make_sound() # Overridden method
cat.climb_tree() # Cat-specific method