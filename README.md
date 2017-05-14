# raipy

This program provides you with a general graphical user interface for your python program.
Specifically,it takes charge of displaying measured values to LCD displays,
 drawing graphs,creating a data file and writing data to it.
 It also gives you a dynamic way to control your program. 

## Installation

	pip install raipy
	
## Usage
Type below in the interactive shell then a GUI window will open.
```python
import raipy
raipy.exe()
```
1.  **Load** your python program by the 'file' menu in the menubar.
See examples in the help menu and you can understand how to write your python program including how to 
display values to LCD displays,set graph data and accept values from 'control' tab.

2.  Push **'Run'** in the toolbar and select a file to write data.
After you choose your data file,your program will start automatically.You can stop it by 
**'Stop'** button in the toolbar.This button will forcibly terminate your program.

3.  Push **'show'** button in 'Graphs' of 'setting' tab after choosing x and y axes.
You can choose multi values for y axis if the dimensions are identical.

4.  **Manipulate components** in 'control' tab such as scroll bars,dials,buttons and input boxes 
      		and you can control your program dynamically.

## How to write your Python program

the **'template'** menu in the menu bar creates a template file for 
your python program.It may look like a little complex but what you have to do is to declare 
labels and implement the run method of programThread.Also see the examples .
Don't forget to push **'reload'** button after editing your program to update the GUI.

---

## Snap shots
![](https://github.com/threemeninaboat3247/raipy/blob/master/raipy.png)
![](https://github.com/threemeninaboat3247/raipy/blob/master/raipy2.png)
![](https://github.com/threemeninaboat3247/raipy/blob/master/raipy3.png)
