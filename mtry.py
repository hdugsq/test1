from numpy.lib.arraysetops import _setxor1d_dispatcher
import pywt
import scipy.fft as fft
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import signal
from PyQt5.QtCore import pyqtSignal,Qt
from PyQt5.QtWidgets import QPushButton
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
class XB():
    sig=['小波基']
    set=['db8']
    mdata=[]
    r=''
    def mset(self,a):
        self.set=a
    def do(self):
        w = pywt.Wavelet(self.set[0])
        x=[None]*len(self.mdata)
        for i in range(len(self.mdata)):
            maxlev = pywt.dwt_max_level(len(self.mdata[i]), w.dec_len)
            coeffs = pywt.wavedec(self.mdata[i], self.set[0], level=maxlev)
            for j in range(1,len(coeffs)):
                coeffs[j] = pywt.threshold(coeffs[j], 0.04*max(coeffs[j]))
            x[i] = pywt.waverec(coeffs, self.set[0])
        self.mdata=x
class FFT():
    sig=['振幅/相位']
    set=['振幅']
    mdata=[]
    r=''
    def mset(self,a):
        self.set=a
    def do(self):
        x=[None]*len(self.mdata)
        for i in range(len(self.mdata)):
            complex_array =fft.fft(self.mdata[i],len(self.mdata[i]))
            if self.set[0]=='振幅':
                x[i]=np.abs(complex_array)
            elif self.set[0]=='相位':
                x[i]=np.angle(complex_array)
        self.mdata=x
class SVm():
    sig=['tr_s','tr_e','pr_s','pr_e']
    set=[100,400,410,428]
    mdata=[]
    r=''
    def mset(self,a):
        self.set=a
    def do(self):
        pr=[]
        label = pd.read_csv(self.r)
        a=len(self.mdata)
        self.mdata = [[row[i] for row in self.mdata] for i in range(len(self.mdata[0]))]
        x = np.array(self.mdata[self.set[0]:self.set[1]])
        y = label['bq'].values[self.set[0]:self.set[1]]
        for i in range(self.set[2],self.set[3]):
            pr.append(self.mdata[i])
        scaler = StandardScaler()
        X_train_std = scaler.fit_transform(x)
        pr=scaler.transform(pr)
        param_grid = {'C':[1e1,1e2,1e3, 5e3,1e4,5e4],
                    'gamma':[0.0001,0.0008,0.0005,0.008,0.005,]}
        clf = GridSearchCV(svm.SVC(kernel= 'rbf',class_weight='balanced',tol=0.01,probability=True),param_grid,cv=10)
        clf = clf.fit(X_train_std,y.ravel())
        b=clf.predict(pr)
        print(b)
class GLP():
    sig=['间接法/直接法']
    set=['间接法']
    mdata=[]
    r=''
    def mset(self,a):
        self.set=a
    def do(self):
        x=[None]*len(self.mdata)
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
class LvB():
    sig=["滤波方式","low","high"]
    set=["低通",0,0]
    mdata=[]
    r=''
    def mset(self,a):
        self.set=a
    def do(self):
        x = [i for i in self.mdata]
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
class DPP():
    sig=['无']
    set=['无']
    mdata=[]
    r=''
    def mset(self,a):
        self.set=a
    def do(self):
        x = [i for i in self.mdata]
        for i in range(len(self.mdata)):
            x[i] =fft.fft(x[i])
            x[i]=np.log(np.abs(x[i]))
            x[i]=fft.ifft(x[i])
            x[i]=x[i].real
        self.mdata=x
class KNN():
    sig=['tr_s','tr_e','pr_s','pr_e','n_neighbors']
    set=[0,300,311,324,3]
    mdata=[]
    r=''
    def mset(self,a):
        self.set=a
    def do(self):
        pr=[]
        label = pd.read_csv(self.r)
        self.mdata = [[row[i] for row in self.mdata] for i in range(len(self.mdata[0]))]
        x = np.array(self.mdata[self.set[0]:self.set[1]])
        y = label['bq'].values[self.set[0]:self.set[1]]
        for i in range(self.set[2],self.set[3]):
            pr.append(self.mdata[i])
        scaler = StandardScaler()
        X_train_std = scaler.fit_transform(x)
        pr=scaler.transform(pr)
        clf = KNeighborsClassifier(n_neighbors=self.set[4],algorithm='auto',weights='distance')
        clf = clf.fit(X_train_std,y.ravel())
        b=clf.predict(pr)
        print(b)
