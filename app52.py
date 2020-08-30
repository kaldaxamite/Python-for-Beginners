class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talk")


debayan = Person("Debayan Nanda")
print(debayan.name)
debayan.talk()