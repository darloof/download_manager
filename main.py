#!/usr/bin/python
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import urllib.request

import os
import os.path
from PyQt5.uic import loadUiType

ui, _ = loadUiType('main.ui')

class MainApp(QMainWindow, ui):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.InitUI()
        self.Handle_Button()
        self.Handle_FileName_From_Path()

    def InitUI(self):
        # self.timer = QTimer()
        # self.timer.setInterval(1500)
        self.tab_main.tabBar().setVisible(False)
        self.Move_gb1()
        self.Move_gb2()
        self.Move_gb3()
        self.Move_gb4()

    def Handle_FileName_From_Path(self):
        self.le_main_url.textChanged.connect(self.Get_Name_From_Url_Main)

    def Handle_Button(self):
        self.btn_main_dl.clicked.connect(self.Download)
        self.btn_main_browse.clicked.connect(self.Handle_Browse)
        self.btn_home.clicked.connect(self.OpenHome)
        self.btn_filedl.clicked.connect(self.OpenFileDl)
        self.btn_videodl.clicked.connect(self.OpenVideoDl)
        self.btn_settings.clicked.connect(self.OpenSettings)
        self.btn_quit.clicked.connect(self.Quit)

    ########## Home animations
    def Move_gb1(self):
        box_animation1 = QPropertyAnimation(self.gb_home_1, b'geometry')
        box_animation1.setDuration(2000)
        box_animation1.setStartValue(QRect(0, 0, 0, 0))
        box_animation1.setEndValue(QRect(40, 30, 221, 111))
        box_animation1.start()
        self.box_animation1 = box_animation1
    def Move_gb2(self):
        box_animation2 = QPropertyAnimation(self.gb_home_2, b'geometry')
        box_animation2.setDuration(2000)
        box_animation2.setStartValue(QRect(0, 0, 0, 0))
        box_animation2.setEndValue(QRect(320, 30, 221, 111))
        box_animation2.start()
        self.box_animation2 = box_animation2
    def Move_gb3(self):
        box_animation3 = QPropertyAnimation(self.gb_home_3, b'geometry')
        box_animation3.setDuration(2000)
        box_animation3.setStartValue(QRect(0, 0, 0, 0))
        box_animation3.setEndValue(QRect(40, 180, 221, 111))
        box_animation3.start()
        self.box_animation3 = box_animation3
    def Move_gb4(self):
        box_animation4 = QPropertyAnimation(self.gb_home_4, b'geometry')
        box_animation4.setDuration(2000)
        box_animation4.setStartValue(QRect(0, 0, 0, 0))
        box_animation4.setEndValue(QRect(320, 180, 221, 111))
        box_animation4.start()
        self.box_animation4 = box_animation4

    ############# Handle main menu buttons
    def OpenHome(self):
        self.tab_main.setCurrentIndex(0)
    def OpenFileDl(self):
        self.tab_main.setCurrentIndex(1)
    def OpenVideoDl(self):
        self.tab_main.setCurrentIndex(2)
    def OpenSettings(self):
        self.tab_main.setCurrentIndex(3)
    def Quit(self):
        sys.exit()

    def Handle_Progress(self, blocknum, blocksize, totalsize):
        readed_data = blocknum * blocksize
        if totalsize > 0:
            download_precentage = readed_data * 100 / totalsize
            download_precentage = int(download_precentage)
            self.pb_main.setValue(download_precentage)
            QApplication.processEvents()

    def Handle_Browse(self):
        save_location = QFileDialog.getSaveFileName(self, caption='Save as', directory='.', filter='All Files(*.*)')
        self.le_main_savelocation.setText(str(save_location[0]))

    def Download(self):
        dl_done = False
        download_url = self.le_main_url.text()
        save_location = self.le_main_savelocation.text()
        if download_url == '' or save_location == '':
            QMessageBox.warning(self, 'Data Error!', 'Provide a valid URL or save location', QMessageBox.Ok)
        else:
            try:
                urllib.request.urlretrieve(download_url, save_location, self.Handle_Progress)
                dl_done = True
            except Exception:
                QMessageBox.warning(self, 'Download Error!' ,'Provide a valid URL or save location')
                return
        if dl_done:
            QMessageBox.information(self, 'Download Completed :)', 'The Downlaod completed successfully')
        self.le_main_url.setText('')
        self.le_main_savelocation.setText('')
        self.pb_main.setValue(0)

    def Save_Browse(self):
        pass

    def Get_Name_From_Url_Main(self):
        extensions = []
        url = self.le_main_url.text()
        fname = url.split('/')[-1]
        fextension = fname.split('.')[-1]
        print(fname, fextension)

def main():
    App = QApplication(sys.argv)
    window = MainApp()
    window.show()
    App.exec_()

if __name__ == '__main__':
    main()