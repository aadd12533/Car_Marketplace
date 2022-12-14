from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent, QIcon, QPixmap
import sys

from login import Ui_Form

username_list = []
password_list = []


class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self._startPos = None
        self._endPos = None
        self._tracking = False

        self.ui.func_widget.setCurrentIndex(0)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    @pyqtSlot()
    def on_exit_btn_clicked(self):
        msgbox = QMessageBox(self)
        msgbox.setWindowIcon(QIcon(r"Icons/question.png"))
        msgbox.setIconPixmap(QPixmap(r"Icons/question (1).png"))

        msgbox.setWindowTitle("E X I T ?")
        msgbox.setText("Are you sure to E X I T ?")
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        reply = msgbox.exec()
        if reply == QMessageBox.Yes:
            self.close()
        else:
            return

    @pyqtSlot()
    def on_create_btn_clicked(self):
        user_name = self.ui.username_edit2.text().strip()
        password = self.ui.password_edit2.text().strip()
        username_list.append(user_name)
        password_list.append(password)
        msgbox2 = QMessageBox(self)
        msgbox2.setWindowIcon(QIcon(r"Icons/7337780431582534641-128.png"))
        msgbox2.setIconPixmap(QPixmap(r"Icons/full_mark.png"))
        msgbox2.setWindowTitle("R e g i s t e r !")
        msgbox2.setText("Yor are now a member")
        msgbox2.setStandardButtons(QMessageBox.Ok)
        reply = msgbox2.exec()
        if reply == QMessageBox.Ok:
            msgbox2.close()

    @pyqtSlot()
    def on_register_btn_clicked(self):
        self.ui.func_widget.setCurrentIndex(1)

    @pyqtSlot()
    def on_login_btn_clicked(self):
        # username = self.ui.username_edit1.text().strip()
        # password = self.ui.password_edit1.text().strip()
        # if username not in username_list and password not in password_list:
        #     self.warning_message()
        #     return
        # else:
        #     return "yes"
        pass

    @pyqtSlot()
    def on_back_btn_clicked(self):
        self.ui.func_widget.setCurrentIndex(0)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if self._tracking:
            self._endPos = a0.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._startPos = QPoint(a0.x(), a0.y())
            self._tracking = True

    def warning_message(self):
        msgbox2 = QMessageBox(self)
        msgbox2.setWindowIcon(QIcon(r"Icons/7337780431582534641-128.png"))
        msgbox2.setIconPixmap(QPixmap(r"Icons/full_mark.png"))
        msgbox2.setWindowTitle("W a r n i n g !")
        msgbox2.setText("Yor username or password is wrong !")
        msgbox2.setStandardButtons(QMessageBox.Ok)
        reply = msgbox2.exec()
        if reply == QMessageBox.Ok:
            msgbox2.close()

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._tracking = True
            self._startPos = None
            self._endPos = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window2 = MainWindow()
    sys.exit(app.exec())
