class a:
    b=[11]
    def __init__(self) -> None:
        self.__a=[11]
    def aa(self):
        self.__a[0]=2
        self.b[0]=2
    def aaa(self):
        print(self.__a[0])
        print(self.b[0])
a1=a()
a2=a()
a1.aa()
a1.aaa()
a2.aaa()
import numpy as np
p=[[1,2,2,1,1],[10,10,10,10,100]]
print(np.log10(p[:][:]))