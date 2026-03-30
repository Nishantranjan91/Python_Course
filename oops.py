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
# class Factory:
#     a = "hello I am attribute"      
#     def hello():
#         print("hello I am a method")

#         obj = Factory( ) # obj now becomes a object who can access anything inside the till now
#         obj2 = Factory()
#         print(obj.a)
        # obj2.hello()





# creating a constructor
# def Factory(material, zips, pockets):
#     def __init__() :
#         print("hello I will run no matter what")
# Factory()        






class Factory:
    def __init__(self, material, zips, pockets):
        
        self.material = material
        self.zips = zips
        self.pockets = pockets
obj = Factory("Leater",3,3)        
        

