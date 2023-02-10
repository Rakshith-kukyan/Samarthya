class cars:
    def __init__(self,brand,hp,model,color):
        self.brand=brand
        self.hp=hp
        self.model=model
        self.color=color
    def myfun(self):
        print("Car brand is "+ self.brand+",Horse power is: "+str(self.hp)+",Model is: "+self.model+" & color is: "+self.color)
    def __str__(self):
       return f"Brand: {self.brand} , Horsepower: {str(self.hp)}, Model: {self.model}, Color: {self.color}\n"
p1=cars("TATA",742,"harrier","red")
p2=cars("Mercedes",800,"620DI","black")
p3=cars("RollsRoyce",900,"Phantom","blue")
p1.myfun()
p2.myfun()
p3.myfun()
print(p1,p2,p3)