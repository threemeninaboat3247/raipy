# -*- coding: utf-8 -*-

from PyQt5.QtGui import QColor
import time
import numpy as np
import raipy.UserClassBase as UserClassBase
from raipy.GpibInst import GpibInst
from datetime import datetime

class programThread(UserClassBase.ThreadBase):
    def run(self):
        #initialization
        
        while not self.stop_event.is_set():
            ###The main body of your program
            ###example: Call self.lcdSignal.emit({'Temperature':1,'Voltage':2}) if you want to display 1 on 'Temperature' display and 2 on 'Voltage' display.
            
            pass
        
        #end processing

class Output(UserClassBase.OutputBase):
    ###Write the labels of your measured values with dimensions
    #format：[[label],[unit]] example:graph_outputs=[['Temperature','K'],['Voltage','V']]
    outputs=[]
    
    ###Write the settings you want to show up in Graphs in advance
    #format:[[x axis label,[y axis label 1,y axis label 2],[color 1,color 2]],[settings for the second graph]] example：[['Time',['Voltage','Current'],[QColor(255,255,0),QColor(0,255,255)]]]
    graph_settings=[]
    
class Control(UserClassBase.ControlBase):
    ###Write your control parameters with initial values
    bools=[]    #format:bools=[['label',bool]] example：bools=[['flag_A',True],['flag_B',False]]
    sliders=[] #format：sliders=[['label',minimum(int)、maximum（int）、initial value（int）]] example：sliders=[['slider_A',0,10,5],['slider_B',0,200,0]]
    dials=[]    #same on 
    floats=[]   #format：floats=[['label',initial value（float）]] example：floats=[['param_PI',3.14159265],[param_E,2.71828]]