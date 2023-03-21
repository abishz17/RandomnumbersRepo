import time
class LinearCongurential:
    def __init__(self,seed,a,c,m) -> None:
        self.X_n = seed;
        self.a=a
        self.c=c
        self.m=m
    
    def generate(self):
        self.X_n=(self.a*self.X_n+self.c)%self.m
        return self.X_n
    def generateBetween0and1(self):
        return self.generate()/self.m # DIVIDING BY M TO GET VALUES BETWEEN O AND 1

seed = time.time()

a = 1664525 # The multiplier a should be chosen such that (a-1) is divisible by all prime factors of m. If m is a multiple of 4, (a-1) should also be divisible by 4.
c = 1013904223 # The increment c should be relatively prime to m, meaning they share no divisors other than 1.
m = 2**12 #The modulus m should be large (e.g., a prime number or a power of 2) to generate a long sequence of numbers.

randomobject= LinearCongurential(seed,a,c,m)

for i in range(10):
    print(randomobject.generateBetween0and1())
