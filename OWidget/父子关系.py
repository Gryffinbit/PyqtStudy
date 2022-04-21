from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("父子关系")
window.resize(500, 500)

label1 = QLabel(window)
label1.setText("标签1")

label2 = QLabel(window)
label2.setText("标签2")
label2.move(50, 50)

label3 = QLabel(window)
label3.setText("标签3")
label3.move(100, 100)

# 查看某个位置是否有子控件
print(window.childAt(50, 50))
# 查看父控件
print(label2.parentWidget())
# 查看所有子控件组成的边界矩形
print(window.childrenRect())
# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())