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
import csv
import re

csv_reader = csv.reader(open(r'D:\python\test\2.csv',encoding = 'utf-8'))
rows = 0

#方法一、此方法可用于输出所有数值，过滤非数值（反之亦然成立）
def is_a_num(string):
    try:
        float(string)#return float(string)
    except:
        return string#return ''     
for row in csv_reader:
    rows += 1
    columns = 0

    for Factor in row[0:]:
        columns += 1
        if is_a_num(Factor) or Factor == '':
#            if not Factor.isalnum() and Factor != '' :
            print(rows,columns,Factor)