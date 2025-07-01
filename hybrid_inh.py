class A:
    def m1():
        print("class A")


class B(A):
    def m2():
        print("class B")
        
    
class C(A):
    def m3():
        print("class C")

class D:
    def m4():
        print("class D")
    
class E(B):
    def m5():
        print("class E")

class F(C,D):
    def m6 ():
        print("class F")
    
jay=E
viru=F


jay.m1()
jay.m2()
jay.m5()
jay.m6()


viru.m3()
viru.m4()
viru.m6()

