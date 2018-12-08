import sys
import os
from PyQt5.QtWidgets import QMainWindow, QPushButton,\
    QApplication, QInputDialog, QLineEdit, QLabel, \
    QFileDialog, QTextEdit, QSpinBox, QVBoxLayout,\
    QComboBox, QGroupBox, QFormLayout
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'BME 590 Image Processor'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.init_gui()
        self.next = None

    def init_gui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Welcome!')
        self.display_text()
        self.button_new_user()
        self.button_existing_user()
        self.show()

    def display_text(self):
        label = QLabel('Author: ', self)
        label.move(200, 350)

    def button_new_user(self):
        button = QPushButton('Create New User', self)
        button.setMinimumSize(200, 40)
        button.setToolTip('This is an example button')
        button.move(100, 200)
        button.clicked.connect(self.get_text)

    def button_existing_user(self):
        button = QPushButton('Existing User', self)
        button.setMinimumSize(200, 40)
        button.setToolTip('This is an example button')
        button.move(320, 200)
        button.clicked.connect(self.get_text)

    def get_text(self):
        text, ok_pressed = QInputDialog.getText(
            self, "Account Information", "Username:", QLineEdit.Normal, "")
        if ok_pressed and text != '':
            self.create_user(text)
            self.close()
            self.next = App2()

    @pyqtSlot()
    def create_user(self, text):
        print(text)
        # place holder for a post function


class App2(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Processor'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.label = QLabel()
        self.next = None
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Step 1: Choose Images!')
        self.button_choose()
        self.show()

    def button_choose(self):
        button = QPushButton('Choose Image', self)
        button.setMinimumSize(200, 40)
        button.setToolTip('This is an example button')
        button.move(220, 200)
        button.clicked.connect(self.image_dialog)

    def image_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileNames(
            self, "QFileDialog.getOpenFileNames()", "",
            "All Files (*)", options=options)
        if file_name:
            print(file_name)
            self.next = App3(file_name)
        else:
            print("Warning: Empty")


# this will page will display image and choose images to upload.
# this for now only works for one image
class App3(QMainWindow):

    def __init__(self, filename=""):
        super().__init__()
        self.title = 'Image Processor'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.path, self.filename = os.path.split(filename[0])
        self.next = None
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Step 2: Upload Image(s)!')
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap(os.path.join(self.path, self.filename))
        pixmap2 = pixmap.scaledToWidth(400)
        label.setPixmap(pixmap2)
        label.setGeometry(120, 20, 640, 280)
        self.button_upload()
        self.show()

    def button_upload(self):
        button = QPushButton('Upload Image', self)
        button.setMinimumSize(200, 40)
        button.setToolTip('This is an example button')
        button.move(220, 300)
        button.clicked.connect(self.next_window)

    def next_window(self):
        self.next = App4(self.path, self.filename)
    # place holder for zip file scroll down menu
    # def list_image(self)


class App4(QMainWindow):

    def __init__(self, path="", filename=""):
        super().__init__()
        self.title = 'Image Processor'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 400
        self.next = None
        self.path = path
        self.filename = filename
        self.init_gui()

    def init_gui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('Step 3: Process Image(s)!')
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap(os.path.join(self.path, self.filename))
        pixmap2 = pixmap.scaledToWidth(250)
        label.setPixmap(pixmap2)
        label.setGeometry(50, 20, 640, 280)
        self.button1()
        self.button2()
        self.button3()
        self.button4()
        self.show()

    def button1(self):
        button = QPushButton('Histogram Equalization', self)
        button.setMinimumSize(200, 40)
        button.setToolTip('This is an example button')
        button.move(360, 60)
        button.clicked.connect(self.on_click)

    def button2(self):
        button = QPushButton('Contrast Stretching', self)
        button.setMinimumSize(200, 40)
        button.setToolTip('This is an example button')
        button.move(360, 120)
        button.clicked.connect(self.on_click)

    def button3(self):
        button = QPushButton('Log Compression', self)
        button.setMinimumSize(200, 40)
        button.setToolTip('This is an example button')
        button.move(360, 180)
        button.clicked.connect(self.on_click)

    def button4(self):
        button = QPushButton('Reverse Video', self)
        button.setMinimumSize(200, 40)
        button.setToolTip('This is an example button')
        button.move(360, 240)
        button.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        # place holder for get and post request

    # place holder for zip file scroll down menu
    # def list_image(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
