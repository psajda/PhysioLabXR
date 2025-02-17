import multiprocessing
import os
import sys

from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QSystemTrayIcon, QMenu

from rena.configs.configs import AppConfigs
from rena.ui.SplashScreen import SplashScreen

AppConfigs(_reset=False)  # create the singleton app configs object
from MainWindow import MainWindow
from rena.startup import load_settings, apply_patches

app = None

if __name__ == '__main__':
    multiprocessing.freeze_support()  # for built exe

    # load the qt application
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    tray_icon = QSystemTrayIcon(QIcon(AppConfigs()._app_logo), parent=app)
    tray_icon.setToolTip('PhysioLabXR')
    tray_icon.show()

    # create the splash screen
    splash = SplashScreen()
    splash.show()

    # load default settings
    load_settings(revert_to_default=False, reload_presets=False)
    apply_patches()
    # main window init
    print("Creating main window")
    window = MainWindow(app=app)

    window.setWindowIcon(QIcon(AppConfigs()._app_logo))
    # make tray menu
    menu = QMenu()
    exit_action = menu.addAction('Exit')
    exit_action.triggered.connect(window.close)

    print("Closing splash screen, showing main window")
    # splash screen destroy
    splash.close()
    window.show()

    print("Entering exec loop")
    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        print('App terminate by KeyboardInterrupt')
        sys.exit()
