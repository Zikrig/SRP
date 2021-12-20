from random import randint
import sympy

class client:
    def __init__(self,i,p):
        self.i = i
        self.s = randint(1000,2000)
        self.p=p
        self.x=hash(self.s+self.p)
        self.N=prime()

        self.g=11
        print(self.g,self.x,self.N)
        self.v=stost(self.g,self.x,self.N)


    def autent(self):

        self.a=randint(100,1000)
        self.A=stost(self.g,self.a, self.N)


    def autent2(self, B,s,k):
        if (B == 0):
            print("Ошибка")
        self.B=B
        print(self.A, self.B)
        self.s=s
        self.u=hash(self.A+B)
        if (self.u) == 0:
            print("Ошибка")
        self.S=stost(B-k*stost(self.g,self.x,self.N),self.a+self.u*self.x,self.N)
        self.K = hash(self.S)

        self.m=hash((hash(self.N) ^ hash(self.g) )+hash(self.i)+self.S+self.A+self.B+k)
        self.r_cl = hash(self.A + self.m + k)

    def getr(self,r):

        self.r=r





class server:
    def __init__(self):
        pass
    def registr(self,i,s,v,g):
        self.i=i
        self.s=s
        self.v=v
        self.k = 3
        self.g=g
        pass
    def autent(self,A,N):
        if(A==0):
            print("Ошибка")
        b=randint(100,1000)
        self.B=(self.k*self.v + stost(self.g,b,N))%N

        self.A=A
        print(self.A,self.B)
        self.u=hash(A+self.B)
        if(self.u)==0:
            print("Ошибка")
        self.S=stost(A*stost(self.v,self.u, N),b,N)
        self.K=hash(self.S)
        self.m = hash((hash(N) ^ hash(self.g)) + hash(self.i) + self.S + self.A + self.B + self.k)
        self.r =  hash(self.A+self.m+self.k)

    def chekM(self,mcl):
        if(mcl==self.m):
            return self.r
        return 0

def stost(a,b,delit):#Возведение в степень с остатком
    res=1
    for i in range(b):
        res*=a
        res = res % delit
    return (res)


def prime():
    while True:
        q=sympy.randprime(500,700)
        N=2*q+1
        if(sympy.isprime(N)):
            return(N)


def hash(a):
    m=a+21
    for i in range(10,300):
        #print(m)
        m+=(a+2)%(i+1)
        m%=999
    return m
