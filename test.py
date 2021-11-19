
"""
Created on 2021/5/13
@author: Irony
@site: https://pyqt.site , https://github.com/PyQt5
@email: 892768447@qq.com
@file: CpuLineChart
@description: 
"""

import sys

from PyQt5.QtChart import QChartView, QChart, QSplineSeries, QDateTimeAxis, QValueAxis
from PyQt5.QtCore import Qt, QTimer, QDateTime, QPointF
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtWidgets import QApplication
from psutil import cpu_percent


class CpuLineChart(QChart):

    def __init__(self,*args, **kwargs):
        super(CpuLineChart, self).__init__(*args, **kwargs)
        self.m_count = 1
        # 隐藏图例
        self.legend().hide()
        self.m_series = QSplineSeries(self)
        # 设置画笔
        self.m_series.setPen(QPen(QColor('#3B8CFF'), 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        self.addSeries(self.m_series)
        # x轴
        self.m_axisX = QValueAxis(self)
        self.m_axisX.setLabelFormat('%d')  # 设置文本格式
        self.m_axisX.setMinorTickCount(0)  # 设置小刻度线的数目
        self.m_axisX.setTickCount(self.m_count + 1)
        self.m_axisX.setRange(0, 100)
        self.m_axisX.setGridLineVisible(False)
        self.m_axisX.setLabelsVisible(False)
        self.addAxis(self.m_axisX, Qt.AlignBottom)
        self.m_series.attachAxis(self.m_axisX)
        # y轴
        self.m_axisY = QValueAxis(self)
        self.m_axisY.setLabelFormat('%d')  # 设置文本格式
        self.m_axisY.setMinorTickCount(0)  # 设置小刻度线的数目
        self.m_axisY.setTickCount(self.m_count + 1)
        self.m_axisY.setRange(0, 100)
        self.m_axisY.setGridLineVisible(False)
        self.m_axisY.setLabelsVisible(False)
        self.addAxis(self.m_axisY, Qt.AlignLeft)
        self.m_series.attachAxis(self.m_axisY)

        # 填充11个初始点，注意x轴 需要转为秒的时间戳
        self.m_series.append(
            [QPointF(0, 0) for i in range(11)])
        print(self.m_series.pointsVector())
        # 定时器获取数据
        self.m_timer = QTimer()
        self.m_timer.timeout.connect(self.update_data)
        self.m_timer.start(1000)

    def update_data(self):
        value = cpu_percent()
        now = QDateTime.currentDateTime()
        self.m_axisX.setRange(now.addSecs(-self.m_count), now)  # 重新调整x轴的时间范围
        # 获取原来的所有点,去掉第一个并追加新的一个
        points = self.m_series.pointsVector()
        points.pop(0)
        points.append(QPointF(now.toMSecsSinceEpoch(), value))
        print(points)
        # 替换法速度更快
        self.m_series.replace(points)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chart = CpuLineChart()
    # chart.setAnimationOptions(QChart.SeriesAnimations)

    view = QChartView(chart)
    view.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
    view.resize(800, 600)
    view.show()
    sys.exit(app.exec_())