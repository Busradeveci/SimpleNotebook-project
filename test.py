import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Test")
window.setGeometry(100, 100, 400, 300)
window.show()
sys.exit(app.exec_())