from PyQt5.Qt import *
import sys


# *****************右键菜单*****************
# class Window(QWidget):
#     def contextMenuEvent(self, evt):
#         print("展示菜单")
#         menu = QMenu(self)
#         # 添加子菜单， 最近打开
#         # 添加行为动作，新建、打开、分割线、退出
#         new_action = QAction(QIcon("../../心心相印.png"), "新建", menu)
#
#         # 繁琐写法
#         # new_action.setText("新建")
#         # new_action.setIcon(QIcon("../../心心相印.png"))
#         new_action.triggered.connect(lambda: print("新建文件"))  # 监听行为
#
#         open_action = QAction(QIcon("../../心心相印.png"), "打开", menu)
#         open_action.triggered.connect(lambda: print("打开文件"))
#
#         exit_action = QAction(QIcon("../../心心相印.png"), "退出", menu)
#         exit_action.triggered.connect(lambda: print("退出"))
#
#         open_recent = QMenu("最近打开", menu)  # 创建子菜单
#         open_recent.setIcon(QIcon("../../心心相印.png"))
#
#         # 新建一个行为
#         file_open_recent = QAction("PYQT编程教学")
#
#         menu.addAction(new_action)
#         menu.addAction(open_action)
#         menu.addMenu(open_recent)  # 子菜单设置
#         open_recent.addAction(file_open_recent)  # 把这个行为file_open_recent，加到open——recent这个菜单的后面
#         menu.addSeparator()
#         menu.addAction(exit_action)
#
#         btn = QPushButton(window)
#         btn.setText("菜单")
#         btn.setMenu(menu)
#
#         # 创建了菜单，用这个方法来展示，执行的时候会传递一个对象point，是菜单展示的位置. 找def contextMenuEvent里面提供的方法，实现全局定位point
#         menu.exec_(evt.globalPos())

# 1建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("菜单功能")
window.resize(500, 500)


# *****************边框扁平化*****************
# print(btn.isFlat())     # 默认非扁平化
# btn.setFlat(True)       # 设置为扁平化，设置扁平化之后，按钮背景样式就没了

# *****************设置默认选项*****************
btn2 = QPushButton(window)
btn2.setText("默认选项")
btn2.move(100, 100)
# btn2.setAutoDefault(True)    # 要用户点击了按钮之后，才会被 设置默认，而不是一开始就被设置为默认
# 对比默认和非默认的两个按钮
# print(btn.autoDefault())
# print(btn2.autoDefault())
# btn2.setDefault(True)   # 一开始就被设置为默认选项


# *****************第二种显示右键菜单的方式*****************
def show_menu(point):
    print("自定义上下文菜单", point)
    menu = QMenu(window)
    # 添加子菜单， 最近打开
    # 添加行为动作，新建、打开、分割线、退出
    new_action = QAction(QIcon("../../心心相印.png"), "新建", menu)

    # 繁琐写法
    # new_action.setText("新建")
    # new_action.setIcon(QIcon("../../心心相印.png"))
    new_action.triggered.connect(lambda: print("新建文件"))  # 监听行为

    open_action = QAction(QIcon("../../心心相印.png"), "打开", menu)
    open_action.triggered.connect(lambda: print("打开文件"))

    exit_action = QAction(QIcon("../../心心相印.png"), "退出", menu)
    exit_action.triggered.connect(lambda: print("退出"))

    open_recent = QMenu("最近打开", menu)  # 创建子菜单
    open_recent.setIcon(QIcon("../../心心相印.png"))

    # 新建一个行为
    file_open_recent = QAction("PYQT编程教学")

    menu.addAction(new_action)
    menu.addAction(open_action)
    menu.addMenu(open_recent)  # 子菜单设置
    open_recent.addAction(file_open_recent)  # 把这个行为file_open_recent，加到open——recent这个菜单的后面
    menu.addSeparator()
    menu.addAction(exit_action)

    btn = QPushButton(window)
    btn.setText("菜单")
    btn.setMenu(menu)

    # point的点要做一个全局映射
    dest_point = window.mapToGlobal(point)
    menu.exec_(dest_point)
window.setContextMenuPolicy(Qt.CustomContextMenu)
window.customContextMenuRequested.connect(show_menu)



















# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())