from PyQt5.Qt import *
import sys


class CustomWindow(QWidget):
    def __int__(self):
        super().__init__()
        self.setWindowTitle("软件名称")
        self.resize(600, 500)
        self.func_list()

    def func_list(self):
        self.func()
        self.func1()

    def func(self):
        btn = QPushButton(self)
        btn.setText("按钮")
        btn.resize(120, 30)
        btn.move(100, 100)

    def func1(self):
        label = QLabel(self)
        label.setText("标签")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CustomWindow()
    window.show()
    sys.exit(app.exec_())
