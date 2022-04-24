from PyQt5.Qt import *
import sys
# 1. 创建一个对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("功能测试2")
window.resize(500, 500)

# # *****************排他性*****************
# # 选中一个之后，就不能选定其他的了
# for i in range(0, 3):
#     btn = QPushButton(window)
#     btn.setText("btn" + str(i))
#     btn.move(50*i, 50*i)
#     # 查看默认排他性
#     print(btn.autoExclusive())
#     # 设置可选
#     btn.setCheckable(True)
#     # 设置排他性
#     btn.setAutoExclusive(True)
# 
# # 只有同级控件之间才有相同排他性，如果在别的控件中，就不会有相同排他性
# btn = QPushButton(window)
# btn.setText("btn3")
# btn.move(200, 200)
# btn.setCheckable(True)

# *****************按钮模拟点击*****************
btn = QPushButton(window)
btn.setText("这是按钮")
btn.move(50, 50)
btn.pressed.connect(lambda: print("按钮被点击"))
btn.released.connect(lambda: print("按钮被释放 "))
# btn.click()  # 模拟点击
btn.animateClick(2000)  # 带动画的点击




# *****************快速构造*****************
btn = QPushButton(QIcon("../../心心相印.png"), "按钮", window)
# 繁杂版
# btn = QPushButton()
# btn.setParent(window)
# btn.setText("狗屎")
# btn.setIcon(QIcon("../../心心相印.png"))























# 2.3 展示控件
window.show()
# 3. 应用程序的执行
sys.exit(app.exec())