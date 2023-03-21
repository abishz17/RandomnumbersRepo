#The additive constant is removed to reduce the complexity of the  lc method. However, its used relatively less.

import time
class MultiplicativeCongurential:
    def __init__(self,seed,a,m) -> None:
        self.X_n = seed;
        self.a=a
        self.m=m
    
    def generate(self):
        self.X_n=(self.a*self.X_n)%self.m
        return self.X_n
    def generateBetween0and1(self):
        return self.generate()/self.m # DIVIDING BY M TO GET VALUES BETWEEN O AND 1

seed = time.time()
a = 16807
m = 2147483647

randomobject= MultiplicativeCongurential(seed,a,m)

for i in range(10):
    print(randomobject.generateBetween0and1())
