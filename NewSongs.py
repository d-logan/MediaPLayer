import os
import vlc
import sys
import eyed3
import time
from mutagen.mp3 import MP3
from threading import Thread
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QListWidgetItem, QMessageBox,QMainWindow,QGraphicsDropShadowEffect,QFileDialog
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        uic.loadUi('Songs.ui', self)
        

        #self.btnExit.clicked.connect(self.close)
        #self.actionExit.triggered.connect(self.close)
        self.Play.clicked.connect(self.songs)
        #self.Stop.clicked.connect(self.stopp)
        self.Pause.clicked.connect(self.pause)

        #songpath = newpath
        songlist = os.listdir(newpath)
        songlist = [s.rsplit('.',1) [0] for s in os.listdir(newpath)]
        self.Play.hide()
        for string in songlist:
            self.SongList.addItem(string)
        self.SongList.itemDoubleClicked.connect(self.songs)


    def stopp(self):
        playsong.stop()
        #self.SongLabel.setText("")
        #self.ArtistLabel.setText("")
        #self.TimeLabel.setText("")
        file = open("sample.txt", "w")
        with open('sample.txt') as f:
            contents = f.read()
            self.TimeLabel.setText(contents)
        file.close()
    def pause(self):

        playsong.pause()

        def PauseSong(self):
            self.Pause.setStyleSheet('QPushButton { border-radius : 25;border : 2px solid white;color: white;background-color: white;background-image: url("pause.png")}')

            while 1:
                time.sleep(0.5)

                playsong.audio_set_volume(self.Volume.value())
                seconds = (playsong.get_time()/1000) % (24 * 3600)
                hour = seconds // 3600
                seconds %= 3600
                minutes = seconds // 60
                seconds %= 60
                self.TimeLabel.setText("%02d:%02d" % (minutes, seconds))
                if (playsong.is_playing() == 0):
                    self.Pause.setStyleSheet('QPushButton { border-radius : 25;border : 2px solid white;color: white;background-color: white;background-image: url("play.png")}')
                    break

        PauseSong = Thread(target = PauseSong, args=(self, ))
        PauseSong.start()

    def songs(self):
        self.Pause.setStyleSheet('QPushButton { border-radius : 25;border : 2px solid white;color: white;background-color: white;background-image: url("pause.png")}')

        SelectedSong = self.SongList.currentItem().text()
        global playsong
        playsong = vlc.MediaPlayer("C://Projects//Songs//" + SelectedSong + ".mp3")

        playsong.audio_set_volume(self.Volume.value())
        playsong.play()

        audio = eyed3.load(newpath + "/" + SelectedSong + ".mp3")
        audiolength = MP3(newpath + "/" + SelectedSong + ".mp3")
        
        self.SongLabel.setText(SelectedSong)
        self.ArtistLabel.setText(audio.tag.artist)
        def Volume(self):
            
            while 1:
                time.sleep(0.5)
                playsong.audio_set_volume(self.Volume.value())
                seconds = (playsong.get_time()/1000) % (24 * 3600)
                hour = seconds // 3600
                seconds %= 3600
                minutes = seconds // 60
                seconds %= 60
                file = open("sample.txt", "w")
                self.TimeLabel.setText("%02d:%02d" % (minutes, seconds))
                

                file.write("%02d:%02d" % (minutes, seconds))
                self.Play.setEnabled(False)
                
                if (playsong.is_playing() == 0):
                    with open('sample.txt') as f:
                        contents = f.read()
                        self.TimeLabel.setText(contents)
                    file.close()
                    self.Play.setEnabled(True)
                    break

        VolumeThread = Thread(target = Volume, args=(self, ))
        VolumeThread.start()


class Splash(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('splash.ui', self)
        self.FileButton.clicked.connect(self.getFile)

    def getFile(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.Directory)
        dialog.setViewMode(QFileDialog.Detail)
        if(dialog.exec()):
            global newpath
            path = dialog.selectedFiles()
            newpath = str(path)[2:-2]

            #self.label.setText(str(sliced))

            self.close()
            self.win = MainWindow()
            self.win.show()


def main():
    app = QApplication(sys.argv)

    window = Splash()
    window.show()


    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
