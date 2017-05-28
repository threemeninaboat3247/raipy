# -*- coding: utf-8 -*-
"""
Created on Sun May 28 22:03:58 2017

@author: Yuki
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class DragButton(QPushButton):
    
    def __init__(self,*args):
        super().__init__(*args)
        self.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)

    def mousePressEvent(self, event):
        self.__mousePressPos = None
        self.__mouseMovePos = None
        if event.button() == Qt.LeftButton:
            self.__mousePressPos = event.globalPos()
            self.__mouseMovePos = event.globalPos()

        super(DragButton, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
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
#            size.setWidth(xsize+xdiff)
#            size.setHeight(ysize+ydiff)
            print(self.sizeHint())

            self.__mouseMovePos = globalPos

        super(DragButton, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPos() - self.__mousePressPos 
            if moved.manhattanLength() > 3:
                event.ignore()
                return

        super(DragButton, self).mouseReleaseEvent(event)

def clicked():
    print('click as normal')

if __name__ == "__main__":
    app = QApplication([])
    w = QWidget()
    w.resize(800,600)

    button = DragButton("Drag", w)
    button.clicked.connect(clicked)
    button2 = DragButton("Drag", w)
    button2.clicked.connect(clicked)

    w.show()
    app.exec_()