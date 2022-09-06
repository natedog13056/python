class grandClass:
    def __int__(self):
        print('in grandClass')
        super().__init__()

class parentClass(grandClass):
    def __int__(self):
        print('in parentClass')
        super().__init__()

class childClass(parentClass):
    def __int__(self):
        print('in childClass')
        super().__init__()

child = childClass()

