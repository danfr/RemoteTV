import sys

from PyQt5 import QtWidgets

from bin.ServerInterface import ServerInterface
from bin.UIManager import UIManager
from bin.Utils import Utils
from view.MainWindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

config = Utils.load_configuration()
ui.server_url.setText(config["SERVER"]["URL"])

serv = ServerInterface()
uim = UIManager(serv, ui)
uim.initialize()

# serv.send_vlc_play_stream("https://www.youtube.com/watch?v=QH2-TGUlwu4")
sys.exit(app.exec_())
