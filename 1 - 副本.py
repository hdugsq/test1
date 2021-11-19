import sys
from method import *
from PyQt5.QtWidgets import QDialog, QPushButton, QWidget, QApplication,QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag,QPainter,QPen,QColor,QIcon
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
import pandas as pd
from PyQt5 import QtCore
import numpy as np
import pywt
import sklearn
import scipy.fft as fft
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
a=0
b=0
c=0
d=0
sig=0
sig2=0
ch=[0,0,0,0,0,0,0,0,0]
r3=[]
p=[]
dat=[]
pub=[]
r=""
mydata=[]
def getdata():
    global r,r3,mydata
    for i in range(len(r3)):
        data1=pd.read_csv(r,usecols=[r3[i]])
        data1=np.array(data1).tolist()
        mydata.append(data1)
    data=[[]for j in range(len(r3))]
    for i in range(len(mydata[0])):
        for j in range(len(r3)):
            data[j].append(mydata[j][i][0])
    mydata=data
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.RightButton:
            print('')

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        dropAcion = drag.exec_(Qt.MoveAction)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.set_u()
        self.initUI()
        self.pushButton.setFixedSize(24,24)
        self.pushButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.play)
        self.pushButton_2.setDisabled(True)
    def play(self):
        global r,r3
        wi=win(r,r3)
        wi.show()
        self.pushButton_2.setDisabled(True)

    def set_u(self):
        loadUi(r"untitled_1.ui", self)
    def initUI(self):
        self.setAcceptDrops(True)

        self.button1 = Button("文件", self)
        self.button1.move(0, 70)
        self.button1.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.button2 = Button("通道选择", self)
        self.button2.move(0, 130)
        self.button2.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.lab=QLabel('预处理',self)
        self.lab.move(0, 190)
        self.lab.setStyleSheet("QLabel{color:white}"
                                "QLabel{background-color:rgb(54, 54, 54)}")

        self.button7 = Button("滤波", self)
        self.button7.move(0, 240)
        self.button7.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.button3 = Button("小波去噪", self)
        self.button3.move(0, 300)
        self.button3.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.lab2=QLabel('特征提取',self)
        self.lab2.move(0, 360)
        self.lab2.setStyleSheet("QLabel{color:white}"
                                "QLabel{background-color:rgb(54, 54, 54)}")

        self.button4 = Button("fft", self)
        self.button4.move(0, 410)
        self.button4.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.button6 = Button("功率谱", self)
        self.button6.move(0, 470)
        self.button6.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.button8 = Button("倒频谱", self)
        self.button8.move(0, 530)
        self.button8.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.lab3=QLabel('分类',self)
        self.lab3.move(0, 590)
        self.lab3.setStyleSheet("QLabel{color:white}"
                                "QLabel{background-color:rgb(54, 54, 54)}")


        self.button5 = Button("svm", self)
        self.button5.move(0, 640)
        self.button5.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.button9 = Button("knn", self)
        self.button9.move(0, 700)
        self.button9.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

    def dragEnterEvent(self, e):
        e.accept()


    def dropEvent(self, e):
        global a,b,c,d,r
        position = e.pos()
        if self.button1.isDown():
            self.pu = WJ('文件',self)
            ch[0]=ch[0]+1
            self.pu.ch=ch[0]
            self.pu.clicked.connect(self.upd)
            self.pu.move(position)
            self.pu.setVisible(True)
            self.button1.setDisabled(True)
            r, filetype = QFileDialog.getOpenFileName(self,"选取文件","./", "All Files (*);;Excel Files (*.xls)")
            self.pu.r=r
        elif self.button2.isDown():
            self.pu2 = TD('通道选择',self)
            ch[1]=ch[1]+1
            self.pu2.ch=ch[1]
            self.pu2.clicked.connect(self.upd)
            self.pu2.move(position)
            self.pu2.setVisible(True)
            self.button2.setDisabled(True)
        elif self.button3.isDown():
            self.pu3 = XB('小波去噪',self)
            ch[2]=ch[2]+1
            self.pu3.ch=ch[2]
            self.pu3.clicked.connect(self.upd)
            self.pu3.move(position)
            self.pu3.setVisible(True)
        elif self.button7.isDown():
            self.pu7 = LvB('滤波',self)
            ch[3]=ch[3]+1
            self.pu7.ch=ch[3]
            self.pu7.clicked.connect(self.upd)
            self.pu7.move(position)
            self.pu7.setVisible(True)
        elif self.button4.isDown():
            self.pu4 = FFT('fft',self)
            ch[4]=ch[4]+1
            self.pu4.ch=ch[4]
            self.pu4.clicked.connect(self.upd)
            self.pu4.move(position)
            self.pu4.setVisible(True)
            self.button4.setDisabled(True)
        elif self.button6.isDown():
            self.pu6 = GLP('功率谱',self)
            ch[5]=ch[5]+1
            self.pu6.ch=ch[5]
            self.pu6.clicked.connect(self.upd)
            self.pu6.move(position)
            self.pu6.setVisible(True)
        elif self.button8.isDown():
            self.pu8 = DPP('倒频谱',self)
            ch[6]=ch[6]+1
            self.pu8.ch=ch[6]
            self.pu8.clicked.connect(self.upd)
            self.pu8.move(position)
            self.pu8.setVisible(True)
        elif self.button5.isDown():
            self.pu5 = SVm('svm',self)
            self.pu5.r=r
            ch[7]=ch[7]+1
            self.pu5.ch=ch[7]
            self.pu5.clicked.connect(self.upd)
            self.pu5.move(position)
            self.pu5.setVisible(True)
            self.button5.setDisabled(True)
        elif self.button9.isDown():
            self.pu9 = KNN('knn',self)
            self.pu9.r=r
            ch[8]=ch[8]+1
            self.pu9.ch=ch[8]
            self.pu9.clicked.connect(self.upd)
            self.pu9.move(position)
            self.pu9.setVisible(True)
        e.setDropAction(Qt.MoveAction)
        e.accept()
    def print(self,sender):
        label=QLabel(sender.name+':')
        label.setStyleSheet('font-size:30px;')
        self.formLayout.addRow(label,QLabel('   '))
        label=QLabel('通道')
        label2=QLabel(str(r3))
        self.formLayout.addRow(label,label2)
    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drewLines(qp)   
        qp.end()
 
    def drewLines(self,qp):
        global a,b,c,d,p
        pen = QPen(QColor(85,170,255), 4, Qt.SolidLine)
        qp.setPen(pen)
        if(a!=0 and c!=0):
            for i in range(len(p)):
                qp.drawLine(p[i][0],p[i][1],p[i][2],p[i][3])
            self.update()  
    def upd(self):
        global a,b,c,d,sig,mydata,dat,pub
        sender = self.sender()
        if sig==0:
            sender.setStyleSheet("QPushButton{color:red}""QPushButton{background-color:rgb(203, 248, 235)}")
            sender.setDisabled(True)
            pub.append(sender)
        else:
            pub[0].setStyleSheet("QPushButton{color:black}""QPushButton{background-color:rgb(203, 248, 235)}")
            pub[0].setDisabled(False)
            pub.clear()
        if sender.text()=="文件":
            if sig==0:
                a=self.pu.x()
                b=self.pu.y()
                sig=sig+1
                with codecs.open('data.txt','w','utf-8') as f:
                    f.write('from mtry import *\nr=\''+r+'\'')
                label=QLabel(sender.name+':')
                label.setStyleSheet('font-size:30px;')
                self.formLayout.addRow(label,QLabel('   '))
                label=QLabel('文件路径')
                line=QLabel(r)
                self.formLayout.addRow(label,line)
                try:
                    ans=pd.read_csv(r,usecols=["others1"])
                    ans2=pd.read_csv(r,usecols=["others2"])
                except ValueError:
                    label=QLabel('无被试者信息')
                    line=QLabel()
                    self.formLayout.addRow(label,line)
                else:
                    ans=np.array(ans).tolist()
                    ans2=np.array(ans2).tolist()
                    for i in range(5):
                        label=QLabel(ans[i][0])
                        line=QLabel(ans2[i][0])
                        self.formLayout.addRow(label,line)
            else:
                c=self.pu.x()
                d=self.pu.y()
                p.append([a,b,c,d])
                sig=0
        elif sender.text()=="通道选择":
            if sig==0:
                a=self.pu2.x()
                b=self.pu2.y()
                self.pushButton_2.setDisabled(True)
                sig=sig+1
                if self.pu2.r=='':
                    getdata()
                    self.pu2.r='1'
                dat=mydata
                sender.mdata=mydata
                with codecs.open('data.txt','a','utf-8') as f:
                    f.write('\nr3=[')
                    for i in range(len(r3)-1):
                        f.write('\''+r3[i]+'\',')
                    f.write('\''+r3[len(r3)-1]+'\']\n')
                    f.write('''mydata=[]
for i in range(len(r3)):
    data1=pd.read_csv(r,usecols=[r3[i]])
    data1=np.array(data1).tolist()
    mydata.append(data1)
data=[[]for j in range(len(r3))]
for i in range(len(mydata[0])):
    for j in range(len(r3)):
        data[j].append(mydata[j][i][0])
mydata=data''')
            else:
                c=self.pu2.x()
                d=self.pu2.y()
                p.append([a,b,c,d])
                win2.show()
                sig=0
                self.pushButton_2.setDisabled(False)
                win2.pushButton_2.clicked.connect(lambda:self.print(sender))
        else:
            if sig==0:
                a=sender.x()
                b=sender.y()
                dat=sender.mdata
                sig=sig+1
                sender.totxt1()
            else:
                c=sender.x()
                d=sender.y()
                p.append([a,b,c,d])
                sig=0
                sender.mdata=dat
                sender.r=r
                sender.do()
                sender.totxt2()
                label=QLabel(sender.name+':')
                label.setStyleSheet('font-size:30px;')
                self.formLayout.addRow(label,QLabel('   '))
                for i in range(len(sender.sig)):
                    label=QLabel(sender.sig[i])
                    label2=QLabel(str(sender.set[i]))
                    self.formLayout.addRow(label,label2)
                if sender.text()=='svm' or sender.text()=='knn':
                    label=QLabel('分类结果')
                    label2=QLabel('')
                    label.setStyleSheet('font-size:30px;')
                    self.formLayout.addRow(label,label2)
                    label=QLabel('标签预测')
                    label2=QLabel(str(sender.b))
                    self.formLayout.addRow(label,label2)
class window2(QDialog):
    def __init__(self):
        super().__init__()
        self.set_u()
        self.setWindowOpacity(0.90)
        self.pushButton_2.clicked.connect(self.sd)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton.clicked.connect(self.__initUI__)
        self.pushButton.setStyleSheet("QPushButton{color:black}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:rgb(78,255,255)}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:10px}"
                                  "QPushButton{padding:2px 4px}")
        self.pushButton_2.setStyleSheet("QPushButton{color:black}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:rgb(78,255,255)}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:10px}"
                                  "QPushButton{padding:2px 4px}")
    def set_u(self):
        loadUi(r'untitled10.ui', self)
    def __initUI__(self):
        global r
        self.df=pd.read_csv(r)
        self.check=[]
        self.r4=self.df.columns
        for i in range(0,len(self.r4)-2):
            self.line = QCheckBox(self.r4[i])
            self.line.setChecked(True)
            self.check.append(self.line)
            self.verticalLayout.addWidget(self.line)
    def sd(self):
        global r3
        r3.clear()
        for i in range(0,len(self.r4)-2):
            if self.check[i].isChecked():
                r3.append(self.check[i].text())
class window3(QDialog):
    def __init__(self):
        super().__init__()
        self.set_u()
        self.setWindowIcon(QIcon(r"C:\Users\qq\Pictures\src=http___pic.51yuansu.com_pic3_cover_03_06_80_5b35d9015cba3_610.jpg&refer=http___pic.51yuansu.jfif"))
        self.setWindowOpacity(0.90)
        self.pushButton_2.setStyleSheet("QPushButton{color:black}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:rgb(78,255,255)}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:10px}"
                                  "QPushButton{padding:2px 4px}")
    def set_u(self):
        loadUi(r'untitled.ui', self)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    win2=window2()
    win2.resize(393,900)
    app.exec_()