from PyQt5.QtWidgets import QMainWindow, QLabel, QGraphicsScene, QFileDialog, QFrame, QApplication, QPushButton, QTextEdit, QMessageBox, QGraphicsView
from PyQt5 import uic
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
import sys
import resources

class Editpage(QMainWindow):
	def __init__(self, homepage, image_path):
		super().__init__()
		self.homepage = homepage
		self.image_path = image_path
		self.setupUi()
		
	def setupUi(self):	
		uic.loadUi("ui_edit.ui", self)
		self.penButton = self.findChild(QPushButton, "pen_button")
		self.eraserButton = self.findChild(QPushButton, "eraser_button")
		self.backButton = self.findChild(QPushButton, "back_button")
		self.nextButton = self.findChild(QPushButton, "next_button")
		self.titleBar = self.findChild(QFrame, "title_bar")
		self.infoLabel = self.findChild(QLabel, "info_label")
		self.imageView = self.findChild(QGraphicsView, "image_view")
		
		self.penButton.setProperty('selected',True)
		self.penButton.setStyle(self.penButton.style())
		self.eraserButton.setProperty('selected',False)
		self.eraserButton.setStyle(self.penButton.style())
		
		self.penButton.clicked.connect(self.penSelect)
		self.eraserButton.clicked.connect(self.eraserSelect)
		self.backButton.clicked.connect(self.goBack)
		self.nextButton.clicked.connect(self.processImage)

		flags = Qt.WindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint)
		self.setWindowFlags(flags)
		self.setAttribute(Qt.WA_TranslucentBackground)

		self.scene = QGraphicsScene()
		self.imageView.setScene(self.scene)	
		self.imageView.aspectRatioMode = Qt.KeepAspectRatio
		self.imageView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
		self.imageView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
		self.image = QImage(self.image_path)
		self.pixmap = QPixmap.fromImage(self.image)
		self.scene.addPixmap(self.pixmap)
		self.imageView.setSceneRect(QRectF(self.pixmap.rect()))
		self.show()
		self.imageView.fitInView(self.imageView.sceneRect(), Qt.KeepAspectRatio)

		


	def penSelect(self):
		self.penButton.setProperty('selected',True)
		self.penButton.setStyle(self.penButton.style())
		self.eraserButton.setProperty('selected',False)
		self.eraserButton.setStyle(self.penButton.style())

	def eraserSelect(self):
		self.penButton.setProperty('selected',False)
		self.penButton.setStyle(self.penButton.style())
		self.eraserButton.setProperty('selected',True)
		self.eraserButton.setStyle(self.penButton.style())


	def goBack(self):
		self.homepage.show()
		self.hide()
		

	def processImage(self):
		pass


	def mousePressEvent(self, event):
		pass

	def mouseMoveEvent(self, event):
		pass

	
if __name__ == "__main__":
    app = QApplication(sys.argv)
    editpage = Editpage()
    editpage.show()
    app.exec()
		



'''
		isTest = widget.property(‘Test’)

		buttonReply = QMessageBox.question(self, 'test message', "Do you like PyQt5?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if buttonReply == QMessageBox.Yes:
			print("Yes")
		else:
			print("No")			
			
		#fileName, _ = QFileDialog.getOpenFileName(None, "Open image file...")
		#editpage = Editpage(fileName)

'''