from PyQt5.Qt import *
import sys

# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("按钮的功能测试-抽象类")
window.resize(500, 500)

# *****************文本操作*****************
btn = QPushButton(window)
btn.setText("1")

def plus_one():
    # 每次点击之后都会加1
    num = int(btn.text()) + 1     # 获取按钮上文本的内容
    btn.setText(str(num))

btn.pressed.connect(plus_one)




# *****************图标操作*****************
icon = QIcon("../../心心相印.png")
btn.setIcon(icon)
size = QSize(30, 30)
btn.setIconSize(size)



# *****************给按钮快捷键的设定*****************
btn.setShortcut("Meta+a")





# *****************自动重复*****************
# 按钮按键不松，会重复触发槽函数
# btn.setAutoRepeat(True)
# btn.setAutoRepeatDelay(2000)     # 长按多久才触发重复   单位ms
# btn.setAutoRepeatInterval(1000)   # 触发频率






# *****************设置按钮被按下*****************
radio_button = QRadioButton(window)
radio_button.setText("我是一个radiobutton")
radio_button.move(100, 50)
# radio_button.setDown(True)   # 设置默认按下状态

push_button = QPushButton(window)
push_button.setText("我是一个pushbotton")
push_button.move(100, 150)
# push_button.setDown(True)

checkbox = QCheckBox(window)
checkbox.setText("我是一个checkbox")
checkbox.move(100, 200)
# checkbox.setDown(True)

# 设置按下之后的样式  QSS样式表
# push_button.setStyleSheet("QPushButton:pressed{background:pink;}")
# radio_button.setStyleSheet("QRadioButton:pressed{background:pink;}")
# checkbox.setStyleSheet("QCheckBox:pressed{background:pink;}")



# *****************默认按钮被选中状态*****************
push_button.setCheckable(True)     # 设定它可以被选中   pushbutton默认不可以被选中
radio_button.setCheckable(True)
checkbox.setCheckable(True)

push_button.setChecked(True)     # 设定默认以及选中
radio_button.setChecked(True)
checkbox.setChecked(True)

# 检查是否被选中、
print(checkbox.isChecked())

# 切换选中域非选中状态 toggle
def cao():
    push_button.toggle()
    radio_button.toggle()
    checkbox.toggle()
btn.pressed.connect(cao)









# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())