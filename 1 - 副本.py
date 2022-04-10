import sys
from method import *
from PyQt5.QtWidgets import QDialog, QPushButton, QWidget, QApplication
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDrag,QPainter,QPen,QColor,QIcon
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
import pandas as pd
import numpy as np
a=0
b=0
c=0
d=0
sig=0
sig2=0
ch=[0,0,0,0,0,0,0,0,0,0,0,0]
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
    print(mydata)
    data=[[]for j in range(len(r3))]
    for i in range(len(mydata[0])):
        for j in range(len(r3)):
            data[j].append(mydata[j][i][0])
    mydata=data
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)

    def mouseMoveEvent(self, e):
        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        dropAcion = drag.exec_(Qt.MoveAction)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.set_u()
        self.initUI()
        self.setStyleSheet("QWidget{border-radius: 50px}")
        self.pushButton.setFixedSize(24,24)
        self.pushButton.setStyleSheet('''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.pushButton.clicked.connect(self.close)
        self.pushButton_2.clicked.connect(self.play)
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.clicked.connect(self.undo)
        self.front=''
    def play(self):
        global r,r3
        wi=win(r,r3)
        wi.show()
        self.pushButton_2.setDisabled(True)

    def set_u(self):
        loadUi(r"untitled1.ui", self)
    def initUI(self):
        self.setAcceptDrops(True)

        self.button1 = Button("文件", self)
        self.button1.setFixedSize(230,60)
        self.button1.move(0, 90)
        self.button1.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.button2 = Button("通道选择", self)
        self.button2.move(0, 150)
        self.button2.setFixedSize(230,60)
        self.button2.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.lab=QLabel('预处理',self)
        self.lab.move(0, 220)
        self.lab.setStyleSheet("QLabel{color:white}"
                                "QLabel{background-color:rgb(54, 54, 54)}")

        self.button7 = Button("滤波", self)
        self.button7.move(0, 260)
        self.button7.setFixedSize(230,60)
        self.button7.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.button3 = Button("小波去噪", self)
        self.button3.move(0, 320)
        self.button3.setFixedSize(230,60)
        self.button3.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.lab2=QLabel('特征提取',self)
        self.lab2.move(0, 390)
        self.lab2.setStyleSheet("QLabel{color:white}"
                                "QLabel{background-color:rgb(54, 54, 54)}")

        self.button4 = Button("fft", self)
        self.button4.move(0, 430)
        self.button4.setFixedSize(230,60)
        self.button4.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.button6 = Button("功率谱", self)
        self.button6.move(0, 490)
        self.button6.setFixedSize(230,60)
        self.button6.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.button8 = Button("倒频谱", self)
        self.button8.move(0, 550)
        self.button8.setFixedSize(230,60)
        self.button8.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")
                                
        self.button11 = Button("HB", self)
        self.button11.move(0, 610)
        self.button11.setFixedSize(230,60)
        self.button11.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.lab3=QLabel('分类',self)
        self.lab3.move(0, 680)
        self.lab3.setStyleSheet("QLabel{color:white}"
                                "QLabel{background-color:rgb(54, 54, 54)}")


        self.button5 = Button("svm", self)
        self.button5.move(0, 720)
        self.button5.setFixedSize(230,60)
        self.button5.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.button9 = Button("knn", self)
        self.button9.move(0, 780)
        self.button9.setFixedSize(230,60)
        self.button9.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")
                                
        self.button10 = Button("mlp", self)
        self.button10.move(0, 840)
        self.button10.setFixedSize(230,60)
        self.button10.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")

        self.lab4=QLabel('聚类',self)
        self.lab4.move(0, 910)
        self.lab4.setStyleSheet("QLabel{color:white}"
                                "QLabel{background-color:rgb(54, 54, 54)}")
                            
        self.button12 = Button("kmeans", self)
        self.button12.move(0, 950)
        self.button12.setFixedSize(230,60)
        self.button12.setStyleSheet("QPushButton{color:white}"
                                  "QPushButton{background-color:rgb(54, 54, 54)}")


    def dragEnterEvent(self, e):
        e.accept()


    def dropEvent(self, e):
        global a,b,c,d,r
        position = e.pos()
        if(230<position.x()<1200 and 80<position.y()):
            if self.button1.isDown():
                self.pu = WJ('文件',self)
                ch[0]=ch[0]+1
                self.pu.ch=ch[0]
                self.pu.clicked.connect(self.upd)
                self.pu.move(position)
                self.pu.setVisible(True)
                self.button1.setDisabled(True)
                r, filetype = QFileDialog.getOpenFileName(self,"选取文件","./", "Csv Files (*.csv)")
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
            elif self.button10.isDown():
                self.pu10 = MLP('mlp',self)
                self.pu10.r=r
                ch[9]=ch[9]+1
                self.pu10.ch=ch[9]
                self.pu10.clicked.connect(self.upd)
                self.pu10.move(position)
                self.pu10.setVisible(True)
            elif self.button11.isDown():
                self.pu11 = HB('hb',self)
                self.pu11.r=r
                ch[10]=ch[10]+1
                self.pu11.ch=ch[10]
                self.pu11.clicked.connect(self.upd)
                self.pu11.move(position)
                self.pu11.setVisible(True)
            elif self.button12.isDown():
                self.pu12 = Kmeans('kmeans',self)
                self.pu12.r=r
                ch[11]=ch[11]+1
                self.pu12.ch=ch[11]
                self.pu12.clicked.connect(self.upd)
                self.pu12.move(position)
                self.pu12.setVisible(True)
            e.setDropAction(Qt.MoveAction)
            e.accept()
        else:
            # self.formLayout.addRow(QLabel("warnning:"),QLabel("不在显示区域内"))
            self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
            self.tableWidget.setSpan(self.tableWidget.rowCount()-1,0,1,2)
            newItem = QTableWidgetItem("不在按钮放置范围内") 
            self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem) 
    def print(self,sender):
        # label=QLabel(sender.name+':')
        # label.setStyleSheet('font-size:30px;')
        self.tableWidget.setRowCount(self.tableWidget.rowCount()+2)
        self.tableWidget.setSpan(self.tableWidget.rowCount()-1,0,1,2)
        newItem = QTableWidgetItem(sender.name+':') 
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
        # self.formLayout.addRow(label,QLabel('   '))
        # label=QLabel('通道')
        # label2=QLabel(str(r3))
        self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
        newItem = QTableWidgetItem('通道')
        newItem2 = QTableWidgetItem(str(r3))
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 1, newItem2)
        # self.formLayout.addRow(label,label2)
        sender.r3=r3
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
    def undo(self):
        global sig
        self.tableWidget.setRowCount(self.tableWidget.rowCount()+2)
        self.tableWidget.setSpan(self.tableWidget.rowCount()-1,0,1,2)
        newItem = QTableWidgetItem("取消成功！")
        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
        if sig==0:
            p.pop()
        else:
            sig=0
            pub[0].setStyleSheet("QPushButton{color:black}""QPushButton{background-color:rgb(203, 248, 235)}")
            pub[0].setDisabled(False)
            pub.clear()

    def upd(self):
        global a,b,c,d,sig,mydata,dat,pub
        sender = self.sender()
        if sig==0:
            sender.setStyleSheet("QPushButton{background-image:url(1.png);background-color:rgba(255, 255, 255,0);color:black}")
            sender.setDisabled(True)
            pub.append(sender)
        if sender.text()=="文件":
            if sig==0:
                a=self.pu.x()
                b=self.pu.y()
                sig=sig+1
                sender.r=r
                self.front='文件'
                with codecs.open('data.txt','w','utf-8') as f:
                    f.write('from mtry import *\nr=\''+r+'\'')
                # label=QLabel(sender.name+':')
                # label.setStyleSheet('font-size:30px;')
                # self.formLayout.addRow(label,QLabel('   '))
                self.tableWidget.setRowCount(self.tableWidget.rowCount()+2)
                newItem = QTableWidgetItem(sender.name+':')
                self.tableWidget.setSpan(self.tableWidget.rowCount()-1,0,1,2)
                self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
                # label=QLabel('文件路径')
                # line=QLabel(r)
                # self.formLayout.addRow(label,line)
                self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
                newItem = QTableWidgetItem('文件路径')
                newItem2 = QTableWidgetItem(r)
                self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
                self.tableWidget.setItem(self.tableWidget.rowCount()-1, 1, newItem2)
                try:
                    ans=pd.read_csv(r,usecols=["bq"])
                except ValueError:
                    # label=QLabel('无标签')
                    # line=QLabel()
                    self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
                    newItem = QTableWidgetItem('无标签')
                    self.tableWidget.setSpan(self.tableWidget.rowCount()-1,0,1,2)
                    self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
                    # self.formLayout.addRow(label,line)
                    self.button5.setEnabled(False)
                    self.button9.setEnabled(False)
                    self.button10.setEnabled(False)
                try:
                    ans=pd.read_csv(r,usecols=["others1"])
                    ans2=pd.read_csv(r,usecols=["others2"])
                except ValueError:
                    # label=QLabel('无被试者信息')
                    # line=QLabel()
                    self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
                    newItem = QTableWidgetItem('无被试者信息')
                    self.tableWidget.setSpan(self.tableWidget.rowCount()-1,0,1,2)
                    self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
                    # self.formLayout.addRow(label,line)
                else:
                    ans=np.array(ans).tolist()
                    ans2=np.array(ans2).tolist()
                    for i in range(5):
                        # label=QLabel(ans[i][0])
                        # line=QLabel(ans2[i][0])
                        self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
                        newItem = QTableWidgetItem(ans[i][0])
                        newItem2 = QTableWidgetItem(ans2[i][0])
                        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
                        self.tableWidget.setItem(self.tableWidget.rowCount()-1, 1, newItem2)
                        #self.formLayout.addRow(label,line)
                sender.do()
            else:
                self.tableWidget.setRowCount(self.tableWidget.rowCount()+2)
                self.tableWidget.setSpan(self.tableWidget.rowCount()-1,0,1,2)
                newItem = QTableWidgetItem("此连线是非法的") 
                self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
        elif sender.text()=="通道选择":
            if sig==0:
                a=self.pu2.x()
                b=self.pu2.y()
                self.front='通道选择'
                self.pushButton_2.setDisabled(True)
                sig=sig+1
                if self.pu2.r=='':
                    getdata()
                    self.pu2.r='1'
                dat=mydata
                sender.mdata=mydata
                sender.do()
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
                if self.front=='文件':
                    c=self.pu2.x()
                    pub[0].setStyleSheet("QPushButton{color:black}""QPushButton{background-color:rgb(203, 248, 235)}")
                    pub[0].setDisabled(False)
                    pub.clear()
                    d=self.pu2.y()
                    p.append([a,b,c,d])
                    win2.show()
                    sig=0
                    self.pushButton_2.setDisabled(False)
                    win2.pushButton_2.clicked.connect(lambda:self.print(sender))
                else:
                    self.tableWidget.setRowCount(self.tableWidget.rowCount()+2)
                    self.tableWidget.setSpan(self.tableWidget.rowCount()-1,0,1,2)
                    newItem = QTableWidgetItem("此连线是非法的") 
                    self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
        elif sender.text()=="hb":
            if sig==0:
                self.front="hb"
                a=sender.x()
                b=sender.y()
                sender.do()
                dat=sender.mdata
                sig=sig+1
                sender.totxt1()
            else:
                pub[0].setStyleSheet("QPushButton{color:black}""QPushButton{background-color:rgb(203, 248, 235)}")
                pub[0].setDisabled(False)
                pub.clear()
                c=sender.x()
                d=sender.y()
                p.append([a,b,c,d])
                sig=0
                sender.mdata=dat
                sender.r=r
                sender.init()
                sender.totxt2()
                # label=QLabel(sender.name+':')
                # label.setStyleSheet('font-size:30px;')
                self.tableWidget.setRowCount(self.tableWidget.rowCount()+2)
                newItem = QTableWidgetItem(sender.name+':')
                self.tableWidget.setSpan(self.tableWidget.rowCount()-1,0,1,2)
                self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
                #self.formLayout.addRow(label,QLabel('   '))
                for i in range(len(sender.sig)):
                    # label=QLabel(sender.sig[i])
                    # label2=QLabel(str(sender.set[i]))
                    self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
                    newItem = QTableWidgetItem(sender.sig[i])
                    newItem2 = QTableWidgetItem(str(sender.set[i]))
                    self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
                    self.tableWidget.setItem(self.tableWidget.rowCount()-1, 1, newItem2)
                    # self.formLayout.addRow(label,label2)
        else:
            if sig==0:
                self.front=sender.text()
                a=sender.x()
                b=sender.y()
                dat=sender.mdata
                sig=sig+1
                sender.totxt1()
            else:
                c=sender.x()
                d=sender.y()
                pub[0].setStyleSheet("QPushButton{color:black}""QPushButton{background-color:rgb(203, 248, 235)}")
                pub[0].setDisabled(False)
                pub.clear()
                p.append([a,b,c,d])
                sig=0
                sender.mdata=dat
                sender.r=r
                sender.do()
                sender.totxt2()
                # label=QLabel(sender.name+':')
                # label.setStyleSheet('font-size:30px;')
                self.tableWidget.setRowCount(self.tableWidget.rowCount()+2)
                newItem = QTableWidgetItem(sender.name+':')
                self.tableWidget.setSpan(self.tableWidget.rowCount()-1,0,1,2)
                self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
                #self.formLayout.addRow(label,QLabel('   '))
                for i in range(len(sender.sig)):
                    # label=QLabel(sender.sig[i])
                    # label2=QLabel(str(sender.set[i]))
                    self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
                    newItem = QTableWidgetItem(sender.sig[i])
                    newItem2 = QTableWidgetItem(str(sender.set[i]))
                    self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
                    self.tableWidget.setItem(self.tableWidget.rowCount()-1, 1, newItem2)
                    # self.formLayout.addRow(label,label2)
                if sender.text()=='svm' or sender.text()=='knn' or sender.text()=='mlp':
                    # label=QLabel('分类结果')
                    # label2=QLabel('')
                    # label.setStyleSheet('font-size:30px;')
                    self.tableWidget.setRowCount(self.tableWidget.rowCount()+2)
                    newItem = QTableWidgetItem('分类结果')
                    self.tableWidget.setSpan(self.tableWidget.rowCount()-1,0,1,2)
                    self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
                    # self.formLayout.addRow(label,label2)
                    # label=QLabel('标签预测')
                    # label2=QLabel(str(sender.b))
                    self.tableWidget.setRowCount(self.tableWidget.rowCount()+1)
                    newItem = QTableWidgetItem('标签预测')
                    newItem2 = QTableWidgetItem(str(sender.b))
                    self.tableWidget.setItem(self.tableWidget.rowCount()-1, 0, newItem)
                    self.tableWidget.setItem(self.tableWidget.rowCount()-1, 1, newItem2)
                    # self.formLayout.addRow(label,label2)
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