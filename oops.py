#class and object
# class Factory:
#     a = 12  #attribute
#     def hello(): 
#         print("how are you")
# print(Factory.a)   
# 
# 
# 
# 
# 
# 
# 
# class
class Factory:
    a = "hello I am attribute"      
    def hello():
        print("hello I am a method")

        obj = Factory( ) # obj now becomes a object who can access anything inside the till now
        obj2 = Factory()
        print(obj.a)
        obj2.hello()
