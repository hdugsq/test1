from mtry import *
r='D:/python/test/train2.csv'
r3=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62']
mydata=[]
for i in range(len(r3)):
    data1=pd.read_csv(r,usecols=[r3[i]])
    data1=np.array(data1).tolist()
    mydata.append(data1)
data=[[]for j in range(len(r3))]
for i in range(len(mydata[0])):
    for j in range(len(r3)):
        data[j].append(mydata[j][i][0])
mydata=data
xb1=XB()
xb1.mdata=mydata
xb1.mset(['db8'])
xb1.do()
mydata=xb1.mdata
fFt1=FFT()
fFt1.mdata=mydata
fFt1.mset(['振幅'])
fFt1.do()
mydata=fFt1.mdata
mlp1=MLP()
mlp1.r=r
mlp1.mdata=mydata
mlp1.mset([0,452,411,424])
mlp1.do()