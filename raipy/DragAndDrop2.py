# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:03:58 2017

@author: Yuki
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class DragButton(QPushButton):
    MARGIN=5
    STATE=False #Falseが平行移動時 Trueが拡大　
    TOP=0
    TOP_RIGHT=1
    RIGHT=2
    BOTTOM_RIGHT=3
    BOTTOM=4
    BOTTOM_LEFT=5
    LEFT=6
    TOP_LEFT=7
    CENTER=8
    
    def __init__(self,*args):
        super().__init__(*args)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
#        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.STATE=self.getLocation(event.pos())
            print(self.STATE)
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(DragButton, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.STATE:
            if event.buttons() == Qt.LeftButton:
                # adjust offset from clicked point to origin of widget
                currPos = self.mapToGlobal(self.pos())
                globalPos = event.globalPos()
                diff = globalPos - self.__mouseMovePos
                xdiff=diff.x()
                ydiff=diff.y()
                x=self.geometry().x()
                y=self.geometry().y()
                xsize=self.geometry().width()
                ysize=self.geometry().height()
                self.setGeometry(x,y,xsize+xdiff,ysize+ydiff)
                self.__mouseMovePos = globalPos
        else:
            if event.buttons() == Qt.LeftButton:
                currPos = self.mapToGlobal(self.pos())
                globalPos = event.globalPos()
                diff = globalPos - self.__mouseMovePos
                newPos = self.mapFromGlobal(currPos + diff)
                self.move(newPos)
                self.__mouseMovePos = globalPos
        super(DragButton, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return
        super(DragButton, self).mouseReleaseEvent(event)
        
    def getLocation(self,point):
        x=point.x()
        y=point.y()
        geo=self.geometry()
        w=geo.width()
        h=geo.height()
        if x < self.MARGIN:
            if y < self.MARGIN:
                return self.TOP_LEFT
            elif h-self.MARGIN < y:
                return self.BOTTOM_LEFT
            else:
                return self.LEFT
        elif w-self.MARGIN < x:
            if y < self.MARGIN:
                return self.TOP_RIGHT
            elif h-self.MARGIN < y:
                return self.BOTTOM_RIGHT
            else:
                return self.RIGHT
        else:
            if y < self.MARGIN:
                return self.TOP
            elif h-self.MARGIN < y:
                return self.BOTTOM
            else:
                return self.CENTER
                
    def expand(self,state,event):
        if state==self.TOP:
            currPos = self.mapToGlobal(self.pos())
            globalPos = event.globalPos()
            diff = globalPos - self.__mouseMovePos
            xdiff=diff.x()
            ydiff=diff.y()
            x=self.geometry().x()
            y=self.geometry().y()
            xsize=self.geometry().width()
            ysize=self.geometry().height()
            self.setGeometry(x,y,xsize+xdiff,ysize+ydiff)
            self.__mouseMovePos = globalPos

def clicked():
    print('click as normal')

if __name__ == "__main__":
    app = QApplication([])
    w = QWidget()
    w.resize(800,600)

    button = DragButton("Drag", w)
    button.clicked.connect(clicked)

    w.show()
    app.exec_()