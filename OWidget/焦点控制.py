from PyQt5.Qt import *
import sys

# 监听窗口的点击时间
class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):
        # 打印焦点的那个控件
        print(self.focusWidget())
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle("焦点控制")
window.resize(500, 500)

# 文本框
txt = QLineEdit(window)
txt.move(50, 50)

txt1 = QLineEdit(window)
txt1.move(50, 100)
txt1.setFocus()    # 初始默认的焦点框

txt2 = QLineEdit(window)
txt2.move(50, 150)

# 设置焦点策略
# txt1.setFocusPolicy(Qt.TabFocus)   # 只能通过Tab来获取txt1的焦点
# txt1.setFocusPolicy(Qt.ClickFocus)   # 只能通过鼠标点击来获取txt1的焦点
txt1.setFocusPolicy(Qt.StrongFocus)  # 可以通过两种方式来获取
txt.setFocusPolicy(Qt.NoFocus)   # 不能通过以上任何一种方式获取焦点，只能通过setfoucs获取
txt2.clearFocus()    # 清空焦点.但如果只有这么一个文本框的话，就还是会焦点它

# 获取当前窗口内部，所有子控件当中获取焦点的那个控件
print(window.focusWidget())



# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())