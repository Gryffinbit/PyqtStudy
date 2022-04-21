# 要求：创建一个窗口包含一个标签，鼠标进入标签时，展示"欢迎光临"。离开时谢谢惠顾
from PyQt5.Qt import *
import sys
class MyLabel(QLabel):
    def enterEvent(self, QEvent):
        print("鼠标进入")
        self.setText("欢迎光临")
    def leaveEvent(self, QEvent):
        print("鼠标离开")
        self.setText("谢谢惠顾")

# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("")
window.resize(500, 500)

label = MyLabel(window)    # 这个label就是父对象里面的self
label.resize(200, 200)
label.move(100, 100)
label.setStyleSheet("background-color:pink;")


# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())