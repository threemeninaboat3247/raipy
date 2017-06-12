# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 23:53:11 2017

@author: Yuki
"""

from multiprocessing import Process,Queue

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QColor
from PyQt5.QtCore import pyqtSignal,QRect
#プロット関係のライブラリ
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import sys

import time

GRAPH_RATE=10  #グラフのアップデート頻度(ms)

class MyGraphicsWindow(pg.GraphicsWindow):
    currentSize=pyqtSignal(int,int,int,int)
    def __init__(self,que):
        super().__init__()
        self.que=que
    
    def closeEvent(self,event):
        geo=self.geometry()
        self.que.put(geo)

class PlotWindow:
    DEFAULT=QRect(50,50,800,600)
    def __init__(self,x_label,x_unit,y_labels,y_unit,colors,x_init,y_inits,size=None,m_que=None,g_que=None):
        #プロット初期設定
        self.win=MyGraphicsWindow(g_que)
        self.win.setWindowTitle('Graph')
        if size==None:
            self.win.setGeometry(self.DEFAULT)
        else:
            self.win.setGeometry(size)
        self.plt=self.win.addPlot()
        self.plt.addLegend()
        self.plt.showGrid(x=True,y=True)
        
        self.x=x_init
        self.xlabel=x_label
        self.x_unit=x_unit

        self.ys=y_inits
        self.ylabels=y_labels
        self.ys_unit=y_unit
        
        self.colors=colors
        self.que=m_que

        fontCss = {'font-family': "Times New Roman, メイリオ", 'font-size': '14pt', "color": 'white'}
        self.plt.getAxis('bottom').setLabel(**fontCss)
        self.plt.getAxis('left').setLabel(**fontCss)
        self.plt.setLabel('bottom',self.xlabel, units=self.x_unit)
        self.plt.setLabel('left', 'Ys', units=self.ys_unit)
        
        self.curves={}
        for data,ylabel,color in zip(self.ys,self.ylabels,colors):
            self.curves[ylabel]=self.plt.plot(self.x,data,pen=color,name=ylabel)
        
        self.points={}
        #set markers at latest values if data lenght is not zero.
        if len(self.x)>0:
            self.x_last=self.x[-1]
            self.ys_last=[y[-1] for y in self.ys]
            for y_last,ylabel in zip(self.ys_last,self.ylabels):
                self.points[ylabel]=self.plt.plot([self.x_last],[y_last],symbolBrush='w')
        
        
        #アップデート時間設定
        self.timer=QtCore.QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.start(GRAPH_RATE)
        
    def update(self):
        mylist=self.empty_que()
        if len(mylist)>0:
            xappended=[d[self.xlabel] for d in mylist]
            self.x=self.x+xappended
            self.x_last=xappended[-1]
            self.ys_last=[]
            for index,ylabel in enumerate(self.ylabels):
                yappended=[d[ylabel] for d in mylist]
                self.ys[index]=self.ys[index]+yappended
                self.ys_last.append(yappended[-1])
                self.curves[ylabel].setData(self.x,self.ys[index])
                if len(self.points)>0:
                    self.plt.removeItem(self.points.pop(ylabel))
            for y_last,ylabel,color in zip(self.ys_last,self.ylabels,self.colors):
                self.points[ylabel]=self.plt.plot([self.x_last],[y_last],symbolBrush='w')
        
    def empty_que(self):
        '''take out the data from the que and return them in a list. コネクションにたまっているdictionary型を全て取り出してlist形式にして返す'''
        mylist=[]
        while True:
            if not self.que.empty():
                mylist.append(self.que.get())
            else:
                break
        return mylist
        
def graphDraw(x_label,x_unit,y_labels,y_unit,colors,x_init,y_inits,size,m_que,g_que):
    app = QApplication(sys.argv)
    graph=PlotWindow(x_label,x_unit,y_labels,y_unit,colors,x_init,y_inits,size,m_que,g_que)
    sys.exit(app.exec_())

if __name__=='__main__':
    app = QApplication(sys.argv)
    x=np.arange(0,10000,0.1)
    y1=np.random.rand(100000)
    y2=np.random.rand(100000)+1
    que1=Queue()
    que2=Queue()
    g=PlotWindow('x','A',['y1','y2'],'V',[QColor(255,0,0),QColor(0,255,0)],x,[y1,y2],None,que1,que2)
    import time
    time.sleep(5)
    sys.exit(app.exec_())