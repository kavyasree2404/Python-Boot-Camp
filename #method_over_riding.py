#method_over_riding
class Animal:
    def Speak():
        return"Animal is speaking......" 
     #single inh   
class Dog(Animal):
        def Speak():
            return "dog is speaking..."
class puppy(Dog):
     def Speak():
          return "puppy is speaking...."
     
obj3=puppy
print(obj3.Speak())     

