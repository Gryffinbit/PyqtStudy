# 创建一个窗口，添加两个文本框，一个按钮
# 要求：一个用作账号，一个用作密码
# 点击登陆按钮后，获取账号和密码信息
# 进行比对账号密码信息，（提前设定正确账号、正确密码）
# 如果账号错误，则清空账号框和密码框
# 密码错误则清空密码框
from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("用户登陆")
window.resize(500, 500)

le1 = QLineEdit(window)
le1.move(100, 100)
le2 = QLineEdit(window)
le2.move(100, 200)
le2.setEchoMode(2)

btn = QPushButton(window)
btn.setText("log in")
btn.move(100, 300)

def compare():
    txt1 = le1.text()
    txt2 = le2.text()
    if txt1 == "gryffinbit" and txt2 == "mypasswd":
        print("successful")
    else:
        if txt1 == "gryffinbit" and txt2 != "mypasswd":
            print("wrong password")
            le2.setText("")
        if txt1 != "gryffinbit":
            print("wrong accunt")
            le1.setText("")
            le2.setText("")


btn.pressed.connect(compare)


# *****************占位文本的提示*****************
le1.setPlaceholderText("请输入账号")

le2.setPlaceholderText("请输入密码")

# *****************一键清空*****************
le1.setClearButtonEnabled(True)
le2.setClearButtonEnabled(True)

# *****************设置密文可见切换*****************
action = QAction(QIcon("close.png"),  "close",  le2)
# action.setIcon(QIcon("open.png"))
le2.addAction(action, QLineEdit.TrailingPosition)   # 放在末尾
def changed():
    if le2.echoMode() == 0:
        action.setIcon(QIcon("open.png"))
        le2.setEchoMode(2)
    else:
        action.setIcon(QIcon("close.png"))
        le2.setEchoMode(0)

# 监听acttion
action.triggered.connect(changed)















# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())