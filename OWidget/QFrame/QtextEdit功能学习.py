# 封装的类--功能部分
# 注意def selecr里面涉及到的反向设置
from PyQt5.Qt import *
class MyTextEdit(QTextEdit):
    def mousePressEvent(self, me):
        print(me.pos())
        link_str = self.anchorAt(me.pos())
        if len(link_str) >0:
            QDesktopServices.openUrl(QUrl(link_str))
        return super().mousePressEvent(me)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        QShortcut(QKeySequence(self.tr("Ctrl+W")), self, self.close)
        self.setWindowTitle("文本编辑器学习")
        self.resize(1000, 1000)
        self.setup_ui()

    def setup_ui(self):
        te = MyTextEdit( self)
        self.te = te     # 为了让下面的接收到这个te变量
        te.move(50, 50)
        te.resize(500, 500)
        te.setStyleSheet("background-color:pink;")
        te.insertHtml("<a href='https://gryffinbit.top'>Blog</a>")

        btn = QPushButton("button", self)
        btn.move(100, 100)
        btn.pressed.connect(self.button_test)

        self.button_test()
        return None      # 代表下面部分被注释了
        self.tip()
        self.text_content()
    def button_test(self):
        # self.te.clear()
        # # self.cursor_insert()
        # # self.image_insert()
        # self.fragement()
        # self.formatting()
        self.open_link()
    def open_link(self):
        self.te.insertHtml("<a name='https://gryffinbit.top'>Blog</a>")
    def edit(self):
        self.te.copy()
        self.te.selectAll()
        self.te.find("hello")
    def color(self):
        self.te.setTextColor(QColor(10, 200, 30))
    def set_font(self):
        # QFontDialog.getFont()    # 可以用来查看有什么字体
        self.te.setFontFamily("隶书")
        self.te.setFontWeight(QFont.Black)
        self.te.setFontUnderline(True)
        font = QFont()
        QFont.style()
        self.te.setCurrentFont(font)
    def auto_formatting(self):
        self.te.setAutoFormatting(QTextEdit.AutoBulletList)
    def begin_end(self):
        # 开始、结束标志块，这样在块内的操作，会被当成一次操作，一块撤销掉
        tc = self.te.textCursor()
        tc.beginEditBlock()
        tc.insertText("hello")
        tc.insertBlock()
        tc.insertText("world")
        tc.insertBlock()
        tc.insertText("fuck")
        tc.insertBlock()
        tc.insertText("you")
        tc.insertBlock()
        tc.endEditBlock()

    def select(self):
        tc = self.te.textCursor()
        tc.setPosition(6, QTextCursor.KeepAnchor)
        self.te.setTextCursor(tc)   # 反向设置
        self.te.setFocus()



    def tip(self):    # 占位文本的提示
        self.te.setPlaceholderText("input......")
    def text_content(self):   # 文本内容样式设置
        # # 设置普通文本
        # self.te.setPlainText("<h1>gagagagR</h1>")
        # 设置富文本
        # self.te.setHtml("<h1>I Love You 3000</h1>")
        # 自动识别是什么类型的文本
        # self.te.setText("<h1>I Love You 3000</h1>")   # html就会自动显示
        self.te.setText("I Love You 3000")
    #  测试这些类里的功能是否有效，该py下面的类被其他文件调用的时候，不会运行这个main。仅用于功能测试
    def cursor_insert(self):
        # 光标插入内容
        tcf = QTextCharFormat()
        tcf.setToolTip("nihao")
        tcf.setFontPointSize(70)
        tc = self.te.textCursor()
        tc.insertText("hello",tcf)
    def image_insert(self):
        # QTextCursor     insertImage(self, QTextImageFormat)
        ti = self.te.textCursor()
        tif = QTextImageFormat()
        tif.setName("../../心心相印.png")      # 图片路径
        ti.insertImage(tif)
    def fragement(self):
        # 插入文本片段
        # 文本不同的格式
        # QTextList
        fr = self.te.textCursor()
        fr.insertList(QTextListFormat.ListCircle)
    def formatting(self):
        # 格式设置和合并
        # QTextCursor
        tc = self.te.textCursor()
        tbf = QTextBlockFormat()
        tbf.setAlignment(Qt.AlignRight)

        tc.setBlockFormat(tbf)

        tbf2 = QTextCharFormat()
        tbf2.setFontFamily("宋体")
        tc.mergeBlockCharFormat(tbf2)


        return None
        tcf = QTextCharFormat()
        tc.setBlockCharFormat(tcf)
        tcf.setFontPointSize(70)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())