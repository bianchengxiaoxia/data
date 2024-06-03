from tkinter import *
from register import Register

class Basedesk:
    """
    基准框模块
    """

    def __init__(self, master):
        # 主界面
        self.root = master  # 窗口传入
        self.root.config()  # 顶层菜单
        self.root.title('教务管理系统')
        self.width = 600  # 界面宽
        self.height = 300  # 界面高
        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        self.screenwidth = self.root.winfo_screenwidth()  # 屏幕宽
        self.screenheight = self.root.winfo_screenheight()  # 屏幕高
        self.alignstr = '%dx%d+%d+%d' % (
            self.width, self.height, (self.screenwidth - self.width) / 2, (self.screenheight - self.height) / 2)
        self.root.geometry(self.alignstr)

        # 进入应用
        self.R = Register(self.root)
        self.R.register()




