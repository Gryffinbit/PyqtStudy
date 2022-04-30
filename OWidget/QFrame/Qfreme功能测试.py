from PyQt5.Qt import *
import sys

# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("功能测试")
window.resize(500, 500)


# frame边框相关
frame = QFrame(window)
frame.move(100, 200)
frame.resize(100, 100)
frame.setStyleSheet("background-color:pink;")
# frame.setFrameShape(QFrame.Box)
# frame.setFrameShadow(QFrame.Sunken)

# 便捷设置的方式，两个一起设置
# frame.setFrameShape(QFrame.Box |QFrame.Sunken)
frame.setFrameShadow(QFrame.Box |QFrame.Sunken)

# 设置阴影等配置
frame.setLineWidth(6)
frame.setMidLineWidth(6)

# 设置矩形
frame.setFrameRect(QRect(10, 70, 39, 40))
# 2.3 展示控件
QShortcut(QKeySequence(window.tr("Ctrl+W")), window, window.close)
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())