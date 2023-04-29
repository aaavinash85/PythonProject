class Dog(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def speak(self):
        print('Hi, I am ',self.name, 'and I am ', self.age, 'years old')

    def change(self, age):
        self.age=age


tim=Dog('Tim', 23)
tim.speak()
tim.change(30)
tim.speak()