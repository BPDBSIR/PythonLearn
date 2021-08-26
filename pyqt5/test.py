from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("PyQt Hello")
window.resize(600, 500)

btn = QPushButton(window)

btn.setText("按钮")
btn.resize(120, 30)
btn.move(100, 100)
btn.setStyleSheet("background-color:green;font-size;16px;")

label = QLabel(window)
label.setText("标签")
label.show()
window.show()

sys.exit(app.exec_())
