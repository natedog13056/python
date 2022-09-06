class father:
    def write(self):
        print("father is good at writing")

class mother:
    def speak(self):
        print("mother is good at speaking")

class son(father, mother):
    def eat(self):
        print("son is good at eating")


obj = son()
obj.write()
obj.speak()
obj.eat()