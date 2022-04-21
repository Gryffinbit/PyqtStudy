from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("内容边距")
window.resize(500, 500)

label = QLabel(window)
label.setText("hello world")
label.resize(300, 300)
label.setStyleSheet("background-color:cyan;")

# 设置内容区域
label.setContentsMargins(100, 200, 0, 0) # 左上右下

# 查看内容区域
print(label.contentsRect())



# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())