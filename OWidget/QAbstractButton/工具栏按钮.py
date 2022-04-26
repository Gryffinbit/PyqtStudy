from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QToolButton")
window.resize(500, 500)

tb = QToolButton(window)
tb.setText("hello")
# tb.setIcon(QIcon("../../心心相印.png"))
# tb.setIconSize(QSize(50, 50))
#
# # 鼠标放在图标上，会显示tip
# tb.setToolTip("这是爱你的开关")
# # 设置按钮风格
# tb.setToolButtonStyle(Qt.ToolButtonTextOnly)    # 只有文字
# # tb.setToolButtonStyle(Qt.ToolButtonIconOnly)    # 只有图标
# # tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)   #文本显示在图标下方
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)   # 文本显示在图标旁边



# *****************设置箭头图标*****************
# Qt.NoArrow   无箭头
# Qt.UpArrow   向上箭头
tb.setArrowType(Qt.LeftArrow)


# *****************平时扁平化，当鼠标放上去的时候，会自动凸起变成按钮(在mac上不能这样实现）*****************
tb.setAutoRaise(True)



# *****************给普通按钮设置菜单选项*****************
btn = QPushButton(window)
btn.setText("hello我是普通扁平按钮")
btn.move(100, 100)
btn.setFlat(True)

menu = QMenu(btn)
sub_menu = QMenu(menu)
sub_menu.setTitle(("子菜单"))
sub_menu.setIcon(QIcon("../../心心相印.png"))

action1 = QAction(QIcon("../../心心相印.png"), "行为1", menu)
action1.setData("行为1")
action2 = QAction(QIcon("../../心心相印.png"), "行为2", menu)
action2.setData("行为2")
# 把子菜单放进menu
menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action1)
menu.addAction(action2)

btn.setMenu(menu)

# *****************工具栏菜单弹出的设置*****************
# 默认是长按才会显示
tb.setPopupMode(QToolButton.MenuButtonPopup)

# *****************不同行为绑定一个槽函数，如何区分的问题*****************
# 绑定data，来区分不同的行为触发的槽函数
# 也就是下面这部分
# action1 = QAction(QIcon("../../心心相印.png"), "行为1", menu)
# action1.setData("行为1")
# action2 = QAction(QIcon("../../心心相印.png"), "行为2", menu)
# action2.setData("行为2")
def do_action(action):
    print("点击了行为", action.data())
tb.triggered.connect(do_action)










tb.setMenu(menu)



















# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())