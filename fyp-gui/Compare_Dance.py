import sys
import shutil
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class App(QWidget):

    target = r'D:/All Projects/dancing-ai-robot/fyp-gui/pose_est/videos'

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 file dialogs - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.openFileNameDialog()
        # self.openFileNamesDialog()
        # self.saveFileDialog()
        
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;MP4 (.mp4);; MOV (.mov);; WMV (.wmv);; FLV (.flv);; AVI (.avi)", options=options)
        
        # Need to include authentication to verify file format
        if fileName:
            original = fileName
            shutil.copy(original, self.target)
            print(fileName)
            sys.exit()
            
    
    # def openFileNamesDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py);;CSV Files (*.csv)", options=options)
    #     if files:
    #         print(files)
    
    # def saveFileDialog(self):
    #     options = QFileDialog.Options()
    #     options |= QFileDialog.DontUseNativeDialog
    #     fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
    #     if fileName:
    #         original = fileName
    #         shutil.copyfile(original, self.target)
    #         print(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())