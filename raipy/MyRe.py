# -*- coding: utf-8 -*-
"""
Created on Wed May 17 01:51:33 2017

@author: Yuki
"""



def toFloat(string):
    import re
    pattern=re.compile('^[\+-]{0,1}\d*\.\d*E\d+')
    return float(pattern.match(string).group())