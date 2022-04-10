from numpy.lib.arraysetops import _setxor1d_dispatcher
import pywt
import codecs
import random
from sklearn import manifold
from sklearn import random_projection
import scipy.fft as fft
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
import copy
import os
import time
from scipy import signal
from PyQt5.QtGui import QDrag,QPainter,QPen,QColor,QIcon
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QSpinBox
from PyQt5.QtCore import QTimer, pyqtSignal,Qt
from PyQt5.QtWidgets import QPushButton
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.cluster import KMeans
from sklearn import svm
import csv
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sqlalchemy import false
route=""
r3=[]
def Savecsv(name,data):
    with open(name,encoding='utf-8',mode='w',newline='') as f:
        writer=csv.writer(f)
        writer.writerow(r3)
        for i in data:
            writer.writerow(i)

def Distance(x, y):
    sum = 0
    leng  = len(x)
    for i in range(leng):
        sum = sum + abs(x[i]-y[i])**(leng)
    dis = sum**(1/leng)
    return dis
class window3(QDialog):
    def __init__(self):
        super().__init__()
        self.set_u()
        self.setWindowIcon(QIcon(r"C:\Users\qq\Pictures\src=http___pic.51yuansu.com_pic3_cover_03_06_80_5b35d9015cba3_610.jpg&refer=http___pic.51yuansu.jfif"))
        self.setWindowOpacity(0.90)
        self.pushButton_2.setStyleSheet("QPushButton{color:black}"
                                  "QPushButton:hover{color:red}"
                                  "QPushButton{background-color:rgb(78,2150,2150)}"
                                  "QPushButton{border:2px}"
                                  "QPushButton{border-radius:10px}"
                                  "QPushButton{padding:2px 4px}")
    def set_u(self):
        loadUi(r'untitled.ui', self)
class WJ(QPushButton):
    name="文件"
    sig=[]
    set=[]
    mdata=[]
    r=''
    ch=0
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            self.play()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
    def do(self):
        global route
        b=time.strftime("%Y-%m-%d_%H-%M-%S_", time.localtime())
        a=os.getcwd()
        route=b+self.r.rsplit("/")[-1][:-4]
        os.makedirs(a+'\\'+route)
    def play(self):
        # 韩东根写的代码
        self.win3=window3()
        
        try:
            ans=pd.read_csv(self.r,usecols=["others1"])
            ans2=pd.read_csv(self.r,usecols=["others2"])
        except ValueError:
            label=QLabel()
            line=QLineEdit()
            self.win3.formLayout.addRow(label,line)
        else:
            ans=np.array(ans).tolist()
            ans2=np.array(ans2).tolist()
            label=QLabel('文件路径')
            line=QLabel(self.r)
            self.win3.formLayout.addRow(label,line)
            for i in range(5):
                label=QLabel(ans[i][0])
                line=QLabel(ans2[i][0])
                self.win3.formLayout.addRow(label,line)
        self.win3.show()
        self.win3.pushButton_2.clicked.connect(self.win3.close)
class TD(QPushButton):
    name='通道选择'
    sig=[]
    set=[]
    mdata=[]
    r3=[]
    r=''
    ch=0
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            self.play()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
    def do(self):
        global route,r3
        r3=self.r3
        nx=[[row[i] for row in self.mdata] for i in range(len(self.mdata[0]))]
        Savecsv(route+"/"+'td.csv',nx)
    def play(self):
        print(len(self.mdata))
        for i in range(len(self.mdata)):
            plt.subplot(len(self.mdata),1,i+1)
            plt.plot(self.mdata[i])
        plt.show()
class XB(QPushButton):
    name='小波去噪'
    sig=['小波基']
    set=['db8']
    mdata=[]
    r=''
    ch=0
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            if len(self.mdata)==0:
                self.setwin()
            else:
                self.play()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
    def do(self):
        w = pywt.Wavelet(self.set[0])
        x = copy.deepcopy(self.mdata)
        for i in range(len(self.mdata)):
            maxlev = pywt.dwt_max_level(len(self.mdata[i]), w.dec_len)
            coeffs = pywt.wavedec(self.mdata[i], self.set[0], level=maxlev)
            for j in range(1,len(coeffs)):
                coeffs[j] = pywt.threshold(coeffs[j], 0.04*max(coeffs[j]))
            x[i] = pywt.waverec(coeffs, self.set[0])
        self.mdata=x
        Savecsv(route+"/"+'xb.csv',[[row[i] for row in self.mdata] for i in range(len(self.mdata[0]))])
    def play(self):
        neww=dwin()
        neww.figure.clear()
        neww.canvas.clear()
        neww.ax.clear()
        for i in range(neww.formLayout.count()):
            neww.formLayout.itemAt(i).widget().deleteLater()
        neww.data=self.mdata
        neww.show()
    def setwin(self):
        win3=window3()
        def aa():
            for i in range(len(self.sig)):
                self.set[i]=win3.formLayout.itemAt(i,1).widget().text()
        for i in range(len(self.sig)):
            label=QLabel(self.sig[i])
            line=QLineEdit(str(self.set[i]))
            win3.formLayout.addRow(label,line)
        win3.show()
        win3.pushButton_2.clicked.connect(aa)
        win3.pushButton_2.clicked.connect(win3.close)
    def totxt1(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nmydata=xb'+str(self.ch)+'.mdata')
    def totxt2(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nxb'+str(self.ch)+'=XB()')
            f.write('\nxb'+str(self.ch)+'.mdata=mydata')
            f.write('\nxb'+str(self.ch)+'.mset([')
            for i in range(len(self.set)-1):
                f.write('\''+self.set[i]+'\',')
            f.write('\''+self.set[len(self.set)-1]+'\'])')
            f.write('\nxb'+str(self.ch)+'.do()')
class FFT(QPushButton):
    name='fft'
    sig=['振幅/相位']
    set=['振幅']
    mdata=[]
    r=''
    ch=0
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            if len(self.mdata)==0:
                self.setwin()
            else:
                self.play()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
    def do(self):
        x = copy.deepcopy(self.mdata)
        for i in range(len(self.mdata)):
            complex_array =fft.fft(self.mdata[i],len(self.mdata[i]))
            if self.set[0]=='振幅':
                x[i]=np.abs(complex_array)
            elif self.set[0]=='相位':
                x[i]=np.angle(complex_array)
        self.mdata=x
        Savecsv(route+"/"+'fft.csv',[[row[i] for row in self.mdata] for i in range(len(self.mdata[0]))])
    def play(self):
        for i in range(len(self.mdata)):
            plt.subplot(len(self.mdata),1,i+1)
            plt.plot(self.mdata[i])
        plt.show()
    def setwin(self):
        win3=window3()
        def aa():
            for i in range(len(self.sig)):
                self.set[i]=win3.formLayout.itemAt(i,1).widget().text()
        for i in range(len(self.sig)):
            label=QLabel(self.sig[i])
            line=QLineEdit(str(self.set[i]))
            win3.formLayout.addRow(label,line)
        win3.show()
        win3.pushButton_2.clicked.connect(aa)
        win3.pushButton_2.clicked.connect(win3.close)
    def totxt1(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nmydata=fFt'+str(self.ch)+'.mdata')
    def totxt2(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nfFt'+str(self.ch)+'=FFT()')
            f.write('\nfFt'+str(self.ch)+'.mdata=mydata')
            f.write('\nfFt'+str(self.ch)+'.mset([')
            for i in range(len(self.set)-1):
                f.write('\''+self.set[i]+'\',')
            f.write('\''+self.set[len(self.set)-1]+'\'])')
            f.write('\nfFt'+str(self.ch)+'.do()')
class SVm(QPushButton):
    name='svm分类'
    sig=['tr_s','tr_e','pr_s','pr_e']
    set=[0,300,311,324]
    mdata=[]
    r=''
    ch=0
    b=[]
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            if len(self.mdata)==0:
                self.setwin()
            else:
                self.play()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
    def do(self):
        pr=[]
        label = pd.read_csv(self.r)
        a=len(self.mdata)
        nx = copy.deepcopy(self.mdata)
        nx = [[row[i] for row in nx] for i in range(len(nx[0]))]
        x = np.array(nx[self.set[0]:self.set[1]])
        y = label['bq'].values[self.set[0]:self.set[1]]
        for i in range(self.set[2],self.set[3]):
            pr.append(nx[i])
        scaler = StandardScaler()
        X_train_std = scaler.fit_transform(x)
        pr = scaler.transform(pr)
        param_grid = {'C':[1e1,1e2,1e3, 5e3,1e4,5e4],
                    'gamma':[0.0001,0.0008,0.0005,0.008,0.005,]}
        clf = GridSearchCV(svm.SVC(kernel= 'rbf',class_weight='balanced',tol=0.01,probability=True),param_grid,cv=10)
        clf = clf.fit(X_train_std,y.ravel())
        self.b=clf.predict(pr)
        print(self.b)
    def setwin(self):
        al=pd.read_csv(self.r)
        al=np.array(al).tolist()
        lena=len(al)
        win3=window3()
        def aa():
            for i in range(len(self.sig)):
                self.set[i]=int(win3.formLayout.itemAt(i,1).widget().value())
        for i in range(len(self.sig)):
            label=QLabel(self.sig[i])
            line=QSpinBox()
            line.setMinimum(0)
            line.setMaximum(lena)
            line.setValue(self.set[i])
            win3.formLayout.addRow(label,line)
        win3.show()
        win3.pushButton_2.clicked.connect(aa)
        win3.pushButton_2.clicked.connect(win3.close)
    def play(self):
        pass
    def totxt1(self):
        pass
    def totxt2(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nsvm'+str(self.ch)+'=SVm()')
            f.write('\nsvm'+str(self.ch)+'.r=r')
            f.write('\nsvm'+str(self.ch)+'.mdata=mydata')
            f.write('\nsvm'+str(self.ch)+'.mset([')
            for i in range(len(self.set)-1):
                if type(self.set[i])==type(1):
                    f.write(str(self.set[i])+',')
                else:
                    f.write('\''+self.set[i]+'\',')
            f.write(str(self.set[len(self.set)-1])+'])')
            f.write('\nsvm'+str(self.ch)+'.do()')
class GLP(QPushButton):
    name='功率谱'
    sig=['间接法/直接法']
    set=['间接法']
    mdata=[]
    r=''
    ch=0
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            if len(self.mdata)==0:
                self.setwin()
            else:
                self.play()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
    def do(self):
        x = copy.deepcopy(self.mdata)
        if self.set[0]=='间接法':
            for i in range(len(self.mdata)):
                a=np.correlate(self.mdata[i],self.mdata[i],'same')
                num=len(a)
                a=fft.fft(a,num)
                pows=np.abs(a)
                x[i]=pows/np.max(pows)
        elif self.set[0]=='直接法':
            for i in range(len(self.mdata)):
                complex_array =fft.fft(self.mdata[i],len(self.mdata[i]))
                pows=np.abs(complex_array)
                x[i]=pows**2/len(self.mdata[i])
        self.mdata=x
        Savecsv(route+"/"+'glp.csv',[[row[i] for row in self.mdata] for i in range(len(self.mdata[0]))])
    def play(self):
        neww=dwin()
        neww.figure.clear()
        neww.canvas.clear()
        neww.ax.clear()
        for i in range(neww.formLayout.count()):
            neww.formLayout.itemAt(i).widget().deleteLater()
        neww.data=20*np.log10(self.mdata[:][:])
        neww.show()
        # for i in range(len(self.mdata)):
        #     plt.subplot(len(self.mdata),1,i+1)
        #     plt.plot(20*np.log10(self.mdata[i][:len(self.mdata[i])//2]),'b')
        # plt.show()
    def setwin(self):
        win3=window3()
        def aa():
            for i in range(len(self.sig)):
                self.set[i]=win3.formLayout.itemAt(i,1).widget().text()
        for i in range(len(self.sig)):
            label=QLabel(self.sig[i])
            line=QLineEdit(str(self.set[i]))
            win3.formLayout.addRow(label,line)
        win3.show()
        win3.pushButton_2.clicked.connect(aa)
        win3.pushButton_2.clicked.connect(win3.close)
    def totxt1(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nmydata=glp'+str(self.ch)+'.mdata')
    def totxt2(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nglp'+str(self.ch)+'=GLP()')
            f.write('\nglp'+str(self.ch)+'.mdata=mydata')
            f.write('\nglp'+str(self.ch)+'.mset([')
            for i in range(len(self.set)-1):
                f.write('\''+self.set[i]+'\',')
            f.write('\''+self.set[len(self.set)-1]+'\'])')
            f.write('\nglp'+str(self.ch)+'.do()')
class LvB(QPushButton):
    name='滤波'
    sig=["滤波方式","low","high"]
    set=["低通",0.3,3]
    mdata=[]
    r=''
    ch=0
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            if len(self.mdata)==0:
                self.setwin()
            else:
                self.play()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
    def do(self):
        x = copy.deepcopy(self.mdata)
        try:
            ans=pd.read_csv(self.r,usecols=["Time"])
        except ValueError:
            self.setDisabled(True)
            freqs=1000
            print("无法获取Time数据")
        else:
            ans=np.array(ans).tolist()
            freqs=ans[1][0]-ans[0][0]
            freqs=1/freqs
        low=(self.set[1]*2)/freqs
        high=(self.set[2]*2)/freqs
        if self.set[0]=='低通':
            b, a = signal.butter(1, high, 'lowpass')
        elif self.set[0]=='高通':
            b,a = signal.butter(1, low, 'highpass')
        else:
            b,a = signal.butter(1, [low,high], 'bandpass')
        self.mdata = signal.filtfilt(b, a, x[0:])
        Savecsv(route+"/"+'lvb.csv',[[row[i] for row in self.mdata] for i in range(len(self.mdata[0]))])
    def play(self):
        neww=dwin()
        neww.figure.clear()
        neww.canvas.clear()
        neww.ax.clear()
        for i in range(neww.formLayout.count()):
            neww.formLayout.itemAt(i).widget().deleteLater()
        neww.data=self.mdata
        neww.show()
        # for i in range(len(self.mdata)):
        #     plt.subplot(len(self.mdata),1,i+1)
        #     plt.plot(self.mdata[i],'b')
        # plt.show()
    def setwin(self):
        win3=window3()
        def aa():
            for i in range(len(self.sig)):
                self.set[i]=win3.formLayout.itemAt(i,1).widget().text()
            self.set[1]=float(self.set[1])
            self.set[2]=float(self.set[2])
        for i in range(len(self.sig)):
            label=QLabel(self.sig[i])
            line=QLineEdit(str(self.set[i]))
            win3.formLayout.addRow(label,line)
        win3.show()
        win3.pushButton_2.clicked.connect(aa)
        win3.pushButton_2.clicked.connect(win3.close)
    def totxt1(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nmydata=lvb'+str(self.ch)+'.mdata')
    def totxt2(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nlvb'+str(self.ch)+'=LvB()')
            f.write('\nlvb'+str(self.ch)+'.mdata=mydata')
            f.write('\nlvb'+str(self.ch)+'.mset([')
            for i in range(len(self.set)-1):
                if type(self.set[i])==type(1.1):
                    f.write(str(self.set[i])+',')
                else:
                    f.write('\''+str(self.set[i])+'\',')
            f.write(str(self.set[len(self.set)-1])+'])')
            f.write('\nlvb'+str(self.ch)+'.do()')
class DPP(QPushButton):
    name='倒频谱'
    sig=['无']
    set=['无']
    mdata=[]
    r=''
    ch=0
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            if len(self.mdata)==0:
                self.setwin()
            else:
                self.play()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
    def do(self):
        x = copy.deepcopy(self.mdata)
        for i in range(len(self.mdata)):
            x[i] =fft.fft(x[i])
            x[i]=np.log(np.abs(x[i]))
            x[i]=fft.ifft(x[i])
            x[i]=x[i].real
        self.mdata=x
        Savecsv(route+"/"+'dpp.csv',[[row[i] for row in self.mdata] for i in range(len(self.mdata[0]))])
    def play(self):
        neww=dwin()
        neww.figure.clear()
        neww.canvas.clear()
        neww.ax.clear()
        for i in range(neww.formLayout.count()):
            neww.formLayout.itemAt(i).widget().deleteLater()
        neww.data=self.mdata
        neww.show()
        # for i in range(len(self.mdata)):
        #     plt.subplot(len(self.mdata),1,i+1)
        #     plt.plot(self.mdata[i],'b')
        # plt.show()
    def setwin(self):
        win3=window3()
        def aa():
            for i in range(len(self.sig)):
                self.set[i]=win3.formLayout.itemAt(i,1).widget().text()
        for i in range(len(self.sig)):
            label=QLabel(self.sig[i])
            line=QLineEdit(str(self.set[i]))
            win3.formLayout.addRow(label,line)
        win3.show()
        win3.pushButton_2.clicked.connect(aa)
        win3.pushButton_2.clicked.connect(win3.close)
    def totxt1(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nmydata=dpp'+str(self.ch)+'.mdata')
    def totxt2(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\ndpp'+str(self.ch)+'=DPP()')
            f.write('\ndpp'+str(self.ch)+'.mdata=mydata')
            f.write('\ndpp'+str(self.ch)+'.mset([')
            for i in range(len(self.set)-1):
                f.write('\''+self.set[i]+'\',')
            f.write('\''+self.set[len(self.set)-1]+'\'])')
            f.write('\ndpp'+str(self.ch)+'.do()')
class KNN(QPushButton):
    name='KNN分类'
    sig=['tr_s','tr_e','pr_s','pr_e','n_neighbors']
    set=[0,300,311,324,3]
    mdata=[]
    r=''
    ch=0
    b=[]
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            if len(self.mdata)==0:
                self.setwin()
            else:
                self.play()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
    def do(self):
        pr=[]
        label = pd.read_csv(self.r)
        nx = copy.deepcopy(self.mdata)
        nx = [[row[i] for row in nx] for i in range(len(nx[0]))]
        self.set[1]=len(label.values)
        x = np.array(nx[self.set[0]:self.set[1]])
        y = label['bq'].values[self.set[0]:self.set[1]]
        for i in range(self.set[2],self.set[3]):
            pr.append(nx[i])
        scaler = StandardScaler()
        X_train_std = scaler.fit_transform(x)
        pr = scaler.transform(pr)
        clf = KNeighborsClassifier(n_neighbors=self.set[4],algorithm='auto',weights='distance')
        clf = clf.fit(X_train_std,y.ravel())
        self.b=clf.predict(pr)
        print(self.b)
    def play(self):
        pr=[]
        label = pd.read_csv(self.r)
        nx = copy.deepcopy(self.mdata)
        nx = [[row[i] for row in nx] for i in range(len(nx[0]))]
        pca=PCA(n_components=2)
        nx=pca.fit_transform(nx)
        x = np.array(nx[self.set[0]:self.set[1]])
        y = label['bq'].values[self.set[0]:self.set[1]]
        print(self.set)
        pca=PCA(n_components=2)
        for i in range(self.set[2],self.set[3]):
            pr.append(copy.deepcopy(nx[i]))
        scaler = StandardScaler()
        X_train_std = scaler.fit_transform(x)
        pr=np.array(pr)
        pr2=scaler.transform(pr)
        clf = KNeighborsClassifier(n_neighbors=self.set[4],algorithm='auto',weights='distance')
        clf = clf.fit(X_train_std,y.ravel())
        self.b=clf.predict(pr2)
        print(self.b)
        x1_min, x1_max=X_train_std[:,0].min(), X_train_std[:,0].max()/5 #第0维特征的范围
        x2_min, x2_max=X_train_std[:,1].min(), X_train_std[:,1].max() #第1维特征的范围
        x1,x2=np.mgrid[x1_min:x1_max:800j, x2_min:x2_max:800j ] #生成网络采样点
        grid_test=np.stack((x1.flat,x2.flat) ,axis=1) #测试点
        grid_hat = clf.predict(grid_test)       # 预测分类值
        grid_hat = grid_hat.reshape(x1.shape)  # 使之与输入的形状相同
        matplotlib.rcParams['font.sans-serif']=['SimHei']
        cm_light=matplotlib.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
        cm_dark=matplotlib.colors.ListedColormap(['g','r','b'] )
        plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)     # 预测值的显示
        plt.scatter(X_train_std[:, 0], X_train_std[:, 1], c=y[:], s=30,cmap=cm_dark)  # 样本
        plt.scatter(pr2[:,0],pr2[:,1], c=self.b[:],s=30,edgecolors='k', zorder=2,cmap=cm_dark) #圈中测试集样本点
        plt.xlabel('5', fontsize=13)
        plt.ylabel('6', fontsize=13)
        plt.xlim(x1_min,x1_max)
        plt.ylim(x2_min,x2_max)
        plt.title('特征分类')
        plt.show()
    def setwin(self):
        al=pd.read_csv(self.r)
        al=np.array(al).tolist()
        lena=len(al)
        win3=window3()
        def aa():
            for i in range(len(self.sig)):
                self.set[i]=int(win3.formLayout.itemAt(i,1).widget().value())
        for i in range(len(self.sig)):
            label=QLabel(self.sig[i])
            line=QSpinBox()
            line.setMinimum(0)
            line.setMaximum(lena)
            line.setValue(self.set[i])
            win3.formLayout.addRow(label,line)
        win3.show()
        win3.pushButton_2.clicked.connect(aa)
        win3.pushButton_2.clicked.connect(win3.close)
    def totxt1(self):
        pass
    def totxt2(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nknn'+str(self.ch)+'=KNN()')
            f.write('\nknn'+str(self.ch)+'.r=r')
            f.write('\nknn'+str(self.ch)+'.mdata=mydata')
            f.write('\nknn'+str(self.ch)+'.mset([')
            for i in range(len(self.set)-1):
                if type(self.set[i])==type(1):
                    f.write(str(self.set[i])+',')
                else:
                    f.write('\''+self.set[i]+'\',')
            f.write(str(self.set[len(self.set)-1])+'])')
            f.write('\nknn'+str(self.ch)+'.do()')
            f.write('\ndpp'+str(self.ch)+'.do()')
class MLP(QPushButton):
    name='MLP分类'
    sig=['tr_s','tr_e','pr_s','pr_e']
    set=[0,400,211,224]
    mdata=[]
    r=''
    ch=0
    b=[]
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            if len(self.mdata)==0:
                self.setwin()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
    def do(self):
        pr=[]
        label = pd.read_csv(self.r)
        nx = copy.deepcopy(self.mdata)
        nx = [[row[i] for row in nx] for i in range(len(nx[0]))]
        self.set[1]=len(label.values)
        x = np.array(nx[self.set[0]:self.set[1]])
        y = label['bq'].values[self.set[0]:self.set[1]]
        for i in range(self.set[2],self.set[3]):
            pr.append(nx[i])
        scaler = StandardScaler()
        X_train_std = scaler.fit_transform(x)
        pr = scaler.transform(pr)
        clf = MLPClassifier(activation='relu', alpha=1e-05, batch_size='auto', beta_1=0.9,
            beta_2=0.999, early_stopping=False, epsilon=1e-08,
            hidden_layer_sizes=(3, 3), learning_rate='constant',
            learning_rate_init=0.001, max_iter=100000, momentum=0.9,
            nesterovs_momentum=True, power_t=0.5, random_state=1, shuffle=True,
            solver='adam', tol=0.0001, validation_fraction=0.1, verbose=False,
            warm_start=False)
        clf = clf.fit(X_train_std,y.ravel())
        self.b=clf.predict(pr)
        print(self.b)
    def setwin(self):
        al=pd.read_csv(self.r)
        al=np.array(al).tolist()
        lena=len(al)
        win3=window3()
        def aa():
            for i in range(len(self.sig)):
                self.set[i]=int(win3.formLayout.itemAt(i,1).widget().value())
        for i in range(len(self.sig)):
            label=QLabel(self.sig[i])
            line=QSpinBox()
            line.setMinimum(0)
            line.setMaximum(lena)
            line.setValue(self.set[i])
            win3.formLayout.addRow(label,line)
        win3.show()
        win3.pushButton_2.clicked.connect(aa)
        win3.pushButton_2.clicked.connect(win3.close)
    def totxt1(self):
        pass
    def totxt2(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nmlp'+str(self.ch)+'=MLP()')
            f.write('\nmlp'+str(self.ch)+'.r=r')
            f.write('\nmlp'+str(self.ch)+'.mdata=mydata')
            f.write('\nmlp'+str(self.ch)+'.mset([')
            for i in range(len(self.set)-1):
                if type(self.set[i])==type(1):
                    f.write(str(self.set[i])+',')
                else:
                    f.write('\''+self.set[i]+'\',')
            f.write(str(self.set[len(self.set)-1])+'])')
            f.write('\nmlp'+str(self.ch)+'.do()')
class HB(QPushButton):
    name='合并输入'
    sig=['pca/tsne/RP']
    set=['pca']
    mdata=[]
    ndata=[]
    sign=0
    r=''
    ch=0
    b=[]
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            if len(self.mdata)==0:
                self.setwin()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
    def init(self):
        ddata=copy.deepcopy(self.mdata)
        ddata = [[row[i] for row in ddata] for i in range(len(ddata[0]))]
        self.ndata.append(np.array(ddata))
    def do(self):
        a=np.array(self.ndata)
        b=[]
        for i in range(len(a[0])):
            for j in range(len(a[0][0])):
                b.append(a[:,i][:,j])
        if self.set[0]=='pca':
            DR=PCA(n_components=1)
        elif self.set[0]=='tsne':
            DR=manifold.TSNE(n_components=1)
        else:
            DR=random_projection.SparseRandomProjection(n_components=1,random_state=42)
        nx=DR.fit_transform(b)
        c=[]
        d=[]
        for i in range(len(nx)):
            if i%len(a[0][0])==0:
                d.append(c)
                c=nx[i]
            else:
                c=np.append(c,nx[i])
        d=d[1:]
        d.append(c)
        d= [[row[i] for row in d] for i in range(len(d[0]))]
        self.mdata=d
        Savecsv(route+"/"+'hb.csv',[[row[i] for row in self.mdata] for i in range(len(self.mdata[0]))])
    def setwin(self):
        win3=window3()
        def aa():
            for i in range(len(self.sig)):
                self.set[i]=win3.formLayout.itemAt(i,1).widget().text()
        for i in range(len(self.sig)):
            label=QLabel(self.sig[i])
            line=QLineEdit(self.set[i])
            win3.formLayout.addRow(label,line)
        win3.show()
        win3.pushButton_2.clicked.connect(aa)
        win3.pushButton_2.clicked.connect(win3.close)
    def totxt1(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nhb'+str(self.ch)+'.do()')
            f.write('\nmydata=hb'+str(self.ch)+'.mdata')
    def totxt2(self):
        with codecs.open('data.txt','a','utf-8') as f:
            if self.sign==0:
                f.write('\nhb'+str(self.ch)+'=HB()')
                f.write('\nhb'+str(self.ch)+'.r=r')
                f.write('\nhb'+str(self.ch)+'.mset([')
            f.write('\nhb'+str(self.ch)+'.mdata=mydata')
            for i in range(len(self.set)-1):
                if type(self.set[i])==type(1):
                    f.write(str(self.set[i])+',')
                else:
                    f.write('\''+self.set[i]+'\',')
            f.write('\''+str(self.set[len(self.set)-1])+'\'])')
            f.write('\nhb'+str(self.ch)+'.init()')
        self.sign=1
def showtime(ax,canvas,x):
    ax.clear()
    ax.plot(x)
    ax.axis('off')
    canvas.draw()
    canvas.update()
    canvas.flush_events()
class dwin(QDialog):
    figure=[]
    canvas=[]
    ax=[]
    data=[]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_u()
        self.pushButton.clicked.connect(self.init)
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda:self.do())
    def init(self):
        for i in range(len(r3)):
            self.figure.append(plt.figure())
            self.canvas.append(FigureCanvas(self.figure[i]))
            self.formLayout.addRow(r3[i],self.canvas[i])
            self.canvas[i].setMaximumSize(1000,60)
            self.ax.append(self.figure[i].add_axes([0, 0.1, 1, 0.8]))
            self.ax[i].axis('off')
        for i in range(len(r3)):
            self.ax[i].plot(self.data[i],'b')
            self.canvas[i].draw()
    def do(self):
        None
    def set_u(self):
        loadUi(r'untitled3.ui', self)
class win(QDialog):
    t=-20
    r=''
    r3=[]
    figure=[]
    canvas=[]
    ax=[]
    def __init__(self,mr,mr3, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.r=mr
        self.r3=mr3
        self.set_u()
        self.x=[[] for i in range(len(self.r3))]
        for i in range(len(self.x)):
            self.x[i]=[0]*300
        self.init()
        self.pushButton.clicked.connect(self.startTimer)
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda:self.do())
    def do(self):
        self.t=self.t+20
        self.data=pd.read_csv(self.r)
        for i,element in enumerate(self.r3):
            data=np.array(self.data[element])
            try:
                for j in range(20):
                    self.x[i].append(data[self.t+j])
            except IndexError:
                return
            else:
                for j in range(20):
                    del self.x[i][0]
            showtime(self.ax[i],self.canvas[i],self.x[i])
    def init(self):
        for i in range(len(self.r3)):
            self.figure.append(plt.figure())
            self.canvas.append(FigureCanvas(self.figure[i]))
            self.formLayout.addRow(self.r3[i],self.canvas[i])
            self.canvas[i].setMaximumSize(1000,60)
            self.ax.append(self.figure[i].add_axes([0, 0.1, 1, 0.8]))
            self.ax[i].axis('off')
            
    def startTimer(self):
        self.timer.start((200))
    def set_u(self):
        loadUi(r'untitled2.ui', self)
class Kmeans(QPushButton):
    name='Kmeans聚类'
    sig=['tr_s','tr_e','pr_s','pr_e','n_clusters']
    set=[0,300,311,324,3]
    mdata=[]
    r=''
    ch=0
    b=[]
    rightClicked = pyqtSignal()
    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        if evt.button()==Qt.RightButton:
            self.rightClicked.emit()
            if len(self.mdata)==0:
                self.setwin()
            else:
                self.play()
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setFixedWidth(135)
        self.setStyleSheet("background-color: #000000")
        self.sig=['tr_s','tr_e','pr_s','pr_e','n_clusters']
        self.set=[0,300,311,324,3]
        self.mdata=[]
        self.b=[]
    def do(self):
        pr=[]
        label = pd.read_csv(self.r)
        nx = copy.deepcopy(self.mdata)
        nx = [[row[i] for row in nx] for i in range(len(nx[0]))]
        self.set[1]=len(label.values)
        x = np.array(nx[self.set[0]:self.set[1]])
        for i in range(self.set[2],self.set[3]):
            pr.append(nx[i])
        scaler = StandardScaler()
        X_train_std = scaler.fit_transform(x)
        pr = scaler.transform(pr)
        clf  = KMeans(n_clusters=self.set[4], random_state=9)
        train=clf.fit_predict(X_train_std)
        pr=clf.predict(pr)
    def play(self):
        label = pd.read_csv(self.r)
        nx = copy.deepcopy(self.mdata)
        nx = [[row[i] for row in nx] for i in range(len(nx[0]))]
        pca=PCA(n_components=2)
        nx=pca.fit_transform(nx)
        x = np.array(nx[:])
        pca=PCA(n_components=2)
        scaler = StandardScaler()
        X_train_std = scaler.fit_transform(x)
        clf  = KMeans(n_clusters=self.set[4], random_state=9)
        x_p1 = clf.fit_predict(X_train_std)
        x1_min, x1_max=X_train_std[:,0].min(), X_train_std[:,0].max() #第0维特征的范围
        x2_min, x2_max=X_train_std[:,1].min(), X_train_std[:,1].max() #第1维特征的范围
        x1,x2=np.mgrid[x1_min:x1_max:800j, x2_min:x2_max:800j ] #生成网络采样点
        grid_test=np.stack((x1.flat,x2.flat) ,axis=1) #测试点
        grid_hat = clf.predict(grid_test)       # 预测分类值
        grid_hat = grid_hat.reshape(x1.shape)  # 使之与输入的形状相同
        matplotlib.rcParams['font.sans-serif']=['SimHei']
        cm_light=matplotlib.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF','#FFFFCC'])
        cm_dark=matplotlib.colors.ListedColormap(['g','r','b','y'])
        plt.pcolormesh(x1, x2, grid_hat, cmap=cm_light)     # 预测值的显示
        plt.scatter(X_train_std[:, 0], X_train_std[:, 1], c=x_p1, s=30,cmap=cm_dark)  # 样本
        plt.xlabel('5', fontsize=13)
        plt.ylabel('6', fontsize=13)
        plt.xlim(x1_min,x1_max)
        plt.ylim(x2_min,x2_max)
        plt.title('特征分类')
        plt.show()
    def setwin(self):
        al=pd.read_csv(self.r)
        al=np.array(al).tolist()
        lena=len(al)
        win3=window3()
        def aa():
            for i in range(len(self.sig)):
                self.set[i]=int(win3.formLayout.itemAt(i,1).widget().value())
        for i in range(len(self.sig)):
            label=QLabel(self.sig[i])
            line=QSpinBox()
            line.setMinimum(0)
            line.setMaximum(lena)
            line.setValue(self.set[i])
            win3.formLayout.addRow(label,line)
        win3.show()
        win3.pushButton_2.clicked.connect(aa)
        win3.pushButton_2.clicked.connect(win3.close)
    def totxt1(self):
        pass
    def totxt2(self):
        with codecs.open('data.txt','a','utf-8') as f:
            f.write('\nkmeans'+str(self.ch)+'=Kmeans()')
            f.write('\nkmeans'+str(self.ch)+'.r=r')
            f.write('\nkmeans'+str(self.ch)+'.mdata=mydata')
            f.write('\nkmeans'+str(self.ch)+'.mset([')
            for i in range(len(self.set)-1):
                if type(self.set[i])==type(1):
                    f.write(str(self.set[i])+',')
                else:
                    f.write('\''+self.set[i]+'\',')
            f.write(str(self.set[len(self.set)-1])+'])')
            f.write('\nkmeans'+str(self.ch)+'.do()')
            f.write('\ndpp'+str(self.ch)+'.do()')