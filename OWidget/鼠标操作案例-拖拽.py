# 完成窗口，用户区支持拖拽. 要求，鼠标点击了用户区拖拽也可以移动窗口
# 封装的类--功能部分
from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.move_flag = False    # 与下面的flag，让他能找到self
        self.setWindowTitle("窗口移动")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pass
    def mousePressEvent(self, evt):
        if evt.button() == Qt.LeftButton:
            # 写一个flag，让只有这个执行之后，下面的才会执行，避免出bug
            self.move_flag = True
            #print("鼠标按下")
            # 确定两个点（鼠标第一次按下的点，窗口当前所在的原始点）
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            # print(self.mouse_x, self.mouse_y)

            self.origin_x = self.x()
            self.origin_y = self.y()


    def mouseMoveEvent(self, evt):
        if self.move_flag:
            # 移动位置 = 当前位置 - 鼠标第一次按下的位置
            # print(evt.globalX(), evt.globalY())
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            # print(self.move_x, self.move_y)

            # 目标位置 = 原始位置 + 移动了的位置
            dest_x = self.origin_x + move_x
            dest_y = self.origin_y + move_y
            self.move(dest_x, dest_y)

    def mouseReleaseEvent(self, QMouseEvent):
        self.move_flag = False


#  测试这些类里的功能是否有效，该py下面的类被其他文件调用的时候，不会运行这个main。仅用于功能测试

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window =Window()
    window.show()
    window.setMouseTracking(True)
    sys.exit(app.exec())