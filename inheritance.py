class Dog(object):
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def speak(self):
        print('Hi, I am ',self.name, 'and I am ', self.age, 'years old')

    def talk(self):
        print("bark")

class Cat(Dog):

    def __init__(self, name, age, color):
        super().__init__(name,age)
        self.color=color

    def talk(self):
        print('something')


tim=Cat('tim', 55, 'black')
tim.speak()
tim.talk()

jim=Dog('jim', 50)
jim.talk()