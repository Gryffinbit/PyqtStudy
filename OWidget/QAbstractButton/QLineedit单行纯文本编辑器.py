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

# le = QLineEdit("请输入", window)
# le.insert("nihao")   # 在当前光标后，插入内容
#
# btn = QPushButton(window)
# btn.setText("按钮")
# btn.move(100, 100)
# btn.pressed.connect(lambda : le.insert("18"))    # 在指定位置插入
# btn.pressed.connect(lambda : print(le.text()))     # 获取真实文本内容
# btn.pressed.connect(lambda : print(le.displayText()))     # 获取用户能看到的文本内容

# *****************功能测试案例*****************
# le1 = QLineEdit(window)
# le1.move(100, 100)
# le2 = QLineEdit(window)
# le2.move(100, 200)
#
# btn = QPushButton(window)
# btn.setText("copy")
# btn.move(100, 300)
#
# def copy():
#     text_A = le1.text()
#     le2.insert(text_A)
#
# btn.pressed.connect(copy)

# *****************输出模式设定*****************
le = QLineEdit(window)
le.move(100, 100)
le.setEchoMode(2 )
# NoEcho = 1   # Normal =0  Password =2   command + QLineedit看官方文档
# le.setEchoMode(2)   # 即 le.setEchoMode(QLineEdit.Password)
btn = QPushButton(window)
btn.setText("copy")
btn.move(100, 300)
def display():
    print(le.text())
    print(le.displayText())
btn.pressed.connect(display)















# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())