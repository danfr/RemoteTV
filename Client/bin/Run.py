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

if sys.argv[1:]:
    if sys.argv[1] == "STREAM" and sys.argv[2]:
        print("STREAM " + sys.argv[2])
        serv.send_vlc_play_file(sys.argv[2])
    elif sys.argv[1] == "TRANSFER" and sys.argv[2]:
        print("TRANSFER " + sys.argv[2])
        serv.send_vlc_send_file(sys.argv[2])
    else:
        print("Bad arguments : " + sys.argv[1] + ", " + sys.argv[2])

# serv.send_vlc_play_stream("https://www.youtube.com/watch?v=QH2-TGUlwu4")
sys.exit(app.exec_())
