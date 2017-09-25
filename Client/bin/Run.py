import sys
from threading import Thread

from PyQt5 import QtWidgets

from bin.ServerInterface import ServerInterface
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
server_watchdog = Thread(target=Utils.set_server_state, args=(serv, ui), daemon=True)
server_watchdog.start()

# serv.send_vlc_play_stream("https://www.youtube.com/watch?v=QH2-TGUlwu4")
sys.exit(app.exec_())
