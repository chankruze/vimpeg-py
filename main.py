import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class Vimpeg(QMainWindow):
    def __init__(self):
        super().__init__()
        self.name = "Vimpeg"
        self.version = "0.0.2"
        self.init()

    def init(self):
        self.setWindowTitle(f"{self.name} {self.version}")
        self.setGeometry(100, 100, 1200, 600)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vimpeg = Vimpeg()
    vimpeg.show()
    sys.exit(app.exec_())
