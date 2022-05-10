import numpy as np
def distance(a,b): #距离计算函数
    print(len(a))
    dis=[]
    for j,c in enumerate(b):
        sum=0
        for i in range(4):
            sum= sum+abs(a[i]-c[i])**4
        dis.append([sum**(1/4),j])
    return dis
def label(s):#划分数据和标签
    it={b'Iris-setosa':0, b'Iris-versicolor':1, b'Iris-virginica':2 }#map
    return it[s]
data=np.loadtxt('19051910高士奇第二次爬虫作业\iris.data', dtype=float, delimiter=',', converters={4:label})
x=data[:,0:4]
y=data[:,4]
shuffed_indexes=np.random.permutation(150)
train_indexes=shuffed_indexes[:130]  #划分测试集和样本集（样本集140，测试集10）
test_indexes=shuffed_indexes[130:]
x_test=x[test_indexes]
y_test=y[test_indexes]
x_train=x[train_indexes]
y_train=y[train_indexes]
answer=[]
for i in range(len(x_test)):
    nei=sorted(distance(x_test[i],x_train),key=lambda x:x[0])[0:5]
    p=[[0,0],[0,1],[0,2]]
    for j in range(5):
        if y_train[nei[j][1]]==0:
            p[0][0]=p[0][0]+(5-j)*20
        if y_train[nei[j][1]]==1:
            p[1][0]=p[1][0]+(5-j)*20
        if y_train[nei[j][1]]==2:
            p[2][0]=p[2][0]+(5-j)*20
    answer.append(max(p)[1])
pricision=0
score=100/len(y_test)
for i in range(len(y_test)):
    if answer[i]==y_test[i]:
        pricision=pricision+score
print(answer)
print(pricision)