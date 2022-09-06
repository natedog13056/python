# multiple parent class
class grandfather:
    def say(self):
        print("greeting from grandfather")

class father(grandfather):
    def say(self):
        super().say()
        print('greeting from father')

class child(father):
    def say(self):
        super().say()
        print('greeting from child')

alan = child()
alan.say()