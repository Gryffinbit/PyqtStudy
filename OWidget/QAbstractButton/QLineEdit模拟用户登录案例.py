from PyQt5.Qt import *
import sys

# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("模拟用户登录")
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


# *****************自动补全*****************

completer = QCompleter(["helloworld", "gryffinbit", "fuckyou"], le1)
le1.setCompleter(completer)




# *****************限制输入内容*****************
# 最大长度限制
le1.setMaxLength(5)
# 只读
le1.setReadOnly(True)
le1.setText("不可以色色")




















# 2.3 展示控件
QShortcut(QKeySequence(window.tr("Ctrl+W")), window, window.close)
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())