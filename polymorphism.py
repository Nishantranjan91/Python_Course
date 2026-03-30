# def hello():
#     print("hello I am a func")

#     def hello():
#         print("hello I am also a func")


class Animal:
    def speak(self):
        print("hello I roar")

class Bird:
    name = "sparrow"
    def speak(self):
        print("hello I tweet")

obj = Animal()
obj2 = Bird() 

obj.speak
obj2.speak              