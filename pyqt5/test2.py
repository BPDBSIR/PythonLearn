from test1 import CustomWindow
from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)
window = CustomWindow()
window.show()
sys.exit(app.exec_())
