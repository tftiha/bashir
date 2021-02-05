import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
from main2 import Ui_MainWindow

class Test(QtWidgets.QMainWindow):
  def __init__(self,parent=None):
    super(Test, self).__init__(parent)
    self.ui = Ui_MainWindow()
    self.ui.setupUi(self)

if __name__ == '__main__':
  app = QtWidgets.QApplication(sys.argv)
  window = Test()
  window.show()
  sys.exit(app.exec_())

