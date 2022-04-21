from PyQt5 import *
import sys

from PyQt5.Qt import *


class Window(QWidget):  #继承父类QWidget
     def __init__(self):  # 默认的self，是创建出来的实类对象，即对象的名字
         super().__init__()     # 继承父类的初始化
         # print("xxx")   # 这个子类初始化需要做的事情
         # self.setWindowTittle("QLabel")
         self.resize(500, 500)

         label = QLabel(self)
         label.setText("xxx")

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)
# 2. 控件的操作
# 2.1 创建控件
window = Window()
#2.2 设置控件
# window.setWindowTittle("QLabel")
# window.resize(500, 500)
#
# label = QLabel(window)
# label.setText("xxx")
#
# lable = QLabel(window)
# lable.setText("xxx")

# 2.3 展示控件
window.show()
# 3. 应用程序的执行，进入到消息循环
sys.exit(app.exec())