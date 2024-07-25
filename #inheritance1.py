#inheritance
class Animal:
    def Speak():
        return"Animal is speaking" 
     #single inh   
class Dog(Animal):
        def Bark():
            return "Bow..."
class puppy(Dog):
     def Speak():
          return "Aww"
obj1=Animal
obj2=Dog
obj3=puppy
print(obj1.Speak())
print(obj2.Bark())
print(obj3.Speak())