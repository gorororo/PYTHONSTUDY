import numpy as np
import matplotlib.pyplot as plt

# from PyQt5.QtWidgets import *
# from PyQt5 import uic

# from_class = uic.loadUiType("F:\\gorororo\\PYTHONSTUDY\\temp\\temp2\\01matploblic_practice")

# class WindowClass(QMainWindow, from_class):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

x= np.linspace(0,2*np.pi,20)
y= np.linspace(0,2*np.pi,20)
grid_x,grid_y = np.meshgrid(x,y)

z= np.sin(grid_x)*np.sin(grid_y)

hfig = plt.figure()
hax = hfig.gca(projection='3d')
hax.plot_surface(grid_x,grid_y,z,cmap='jet')
hax.set_xlabel('x')
hax.set_ylabel('y')
hax.set_zlabel('z')
#3d 그래프를 돌려서 플롯 하려면 스파이더에서 Preferences Ipython console 을 Qt5 로 바꾸어서 실행하면 새창에 플롯이뜨고 돌려몰수 있다
