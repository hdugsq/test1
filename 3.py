from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QDialog,QApplication
from PyQt5.QtCore import QTimer
import matplotlib.pyplot as plt
from PyQt5.uic import loadUi
import sys
import pandas as pd
from pylab import *
def showtime(ax,canvas,x):
    ax.clear()
    ax.plot(x)
    ax.axis('off')
    canvas.draw()
    canvas.update()
    canvas.flush_events()
class window(QDialog):
    t=-20
    r='train2.csv'
    r3=['1','2','3','4','5','6','7','8','9','10','2','3','4','5','6','7','8','9','10','2','3','4','5','6','7','8','9','10','2','3','4','5','6','7','8','9','10','2','3','4','5','6','7','8','9','10']
    figure=[]
    canvas=[]
    ax=[]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
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
            self.formLayout.addRow(str(i),self.canvas[i])
            self.canvas[i].setMaximumSize(1000,60)
            self.ax.append(self.figure[i].add_axes([0, 0.1, 1, 0.8]))
            self.ax[i].axis('off')
            
    def startTimer(self):
        self.timer.start((200))
    def set_u(self):
        loadUi(r'untitled2.ui', self)
if __name__ == "__main__":        
    app = QApplication(sys.argv)
    window = window()
    window.show()
    app.exec_()
        
