from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
window.setWindowTitle("顶层窗口操作-案例")
window.resize(500, 500)
window.setWindowFlag(Qt.FramelessWindowHint)
window.setWindowOpacity(0.9)


# 添加三个子控件



# 按钮在右上角
# btn_close = QPushButton(window)
# btn_close.setText("关闭")
# btn_close_w = btn_close.width()    # 获取按钮的宽度
# window_w = window.width()          # 获取窗口的宽度
# btn_close_x= window_w - btn_close_w # btn移动的距离 = 窗口宽度 - 按钮宽度
# btn_close_y = 10
# btn_close.move(btn_close_x, btn_close_y)

# 按钮在左上角
btn_close = QPushButton(window)
btn_close.setText("关闭")
btn_close.pressed.connect(window.close)      # 使用槽函数，发布被按下去的信号，执行窗口关闭的动作

btn_min = QPushButton(window)
btn_min.setText("最小化")
btn_min_x = btn_close.width()
btn_min.move(btn_min_x, 0)
btn_min.pressed.connect(window.showMinimized)

btn_max = QPushButton(window)
btn_max.setText("最大化")
btn_max_x = btn_close.width() + btn_min.width()
btn_max.move(btn_max_x, 0)
btn_max.pressed.connect(window.showMaximized)

# 监听窗口大小
class Window(QWidget):
    def resizeEvent(self, QResizeEvent):
        pass
# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())




# # 0. 导入需要的包和模块
# from PyQt5.Qt import *
# import sys
#
# class Window(QWidget):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.setWindowFlags(Qt.FramelessWindowHint)
#         self.setWindowOpacity(0.9)
#         # 2.2 设置控件
#         self.setWindowTitle("顶层窗口操作-案例")
#         self.resize(500, 500)
#
#         # 公共数据
#         self.top_margin = 10
#         self.btn_w = 80
#         self.btn_h = 40
#
#         self.setup_ui()
#
#     def setup_ui(self):
#
#         # 添加三个子控件 - 窗口的右上角
#         close_btn = QPushButton(self)
#         self.close_btn = close_btn
#         close_btn.setText("关闭")
#         close_btn.resize(self.btn_w, self.btn_h)
#
#         max_btn = QPushButton(self)
#         self.max_btn = max_btn
#         max_btn.setText("最大化")
#         max_btn.resize(self.btn_w, self.btn_h)
#
#         mini_btn = QPushButton(self)
#         self.mini_btn = mini_btn
#         mini_btn.setText("最小化")
#         mini_btn.resize(self.btn_w, self.btn_h)
#
#         close_btn.pressed.connect(self.close)
#
#         def max_normal():
#             if self.isMaximized():
#                 self.showNormal()
#                 max_btn.setText("最大化")
#             else:
#                 self.showMaximized()
#                 max_btn.setText("恢复")
#
#         max_btn.pressed.connect(max_normal)
#         mini_btn.pressed.connect(self.showMinimized)
#
#     def resizeEvent(self, QResizeEvent):
#         print("窗口大小发生了改变")
#         # close_btn_w = btn_w
#         window_w = self.width()
#         close_btn_x = window_w - self.btn_w
#         close_btn_y = self.top_margin
#         self.close_btn.move(close_btn_x, close_btn_y)
#
#         max_btn_x = close_btn_x - self.btn_w
#         max_btn_y = self.top_margin
#         self.max_btn.move(max_btn_x, max_btn_y)
#
#         mini_btn_x = max_btn_x - self.btn_w
#         mini_btn_y = self.top_margin
#         self.mini_btn.move(mini_btn_x, mini_btn_y)
#
#     def mousePressEvent(self, QMouseEvent):
#         # 判定点击的是否是鼠标左键
#         # 在此处设计一个标记, 用作判定是否需要移动
#         # 一个就是窗口的原始坐标
#         # 鼠标按下的点
#         pass
#
#     def mouseMoveEvent(self, QMouseEvent):
#         # if 窗口的移动标记 == True:
#             # 根据鼠标按下的点 计算移动向量
#             # 根据移动向量, 和窗口的原始坐标 = 最新坐标
#             # 移动整个窗口的位置
#         pass
#
#     def mouseReleaseEvent(self, QMouseEvent):
#         # 把这个标记, 进行重置  False
#         pass
#
# # 1. 创建一个应用程序对象
# app = QApplication(sys.argv)
#
# # 2. 控件的操作
# # 2.1 创建控件
# # window = QWidget(flags=Qt.FramelessWindowHint)
# window = Window()
#
#
# # 2.3 展示控件
# window.show()
# # 3. 应用程序的执行, 进入到消息循环
# sys.exit(app.exec_())