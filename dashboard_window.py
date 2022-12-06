import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QPushButton, QWidget, QMessageBox
)
from PyQt5.QtCore import (
    pyqtSlot, QFile, QTextStream, QSize, Qt, QPoint
)
from PyQt5.QtGui import (
    QIcon, QMouseEvent, QPixmap
)
from sidebar import Ui_MainWindow
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
        if self.ui.email_edit.text() == "" or self.ui.password_edit2.text() == "" or \
                self.ui.phone_edit.text() == "" or self.ui.username_edit2.text() == "" or \
                self.ui.address_edit.text() == "":
            self.input_warning()
        else:
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
            self.ui.username_edit2.clear()
            self.ui.password_edit2.clear()
            self.ui.email_edit.clear()
            self.ui.phone_edit.clear()
            self.ui.address_edit.clear()
            reply = msgbox2.exec()
            if reply == QMessageBox.Ok:
                msgbox2.close()
                self.ui.func_widget.setCurrentIndex(0)

    @pyqtSlot()
    def on_register_btn_clicked(self):
        self.ui.func_widget.setCurrentIndex(1)

    @pyqtSlot()
    def on_login_btn_clicked(self):
        username = self.ui.username_edit1.text().strip()
        password = self.ui.password_edit1.text().strip()
        if username == "" or password == "":
            self.input_warning()
            return
        elif username not in username_list and password not in password_list:
            self.warning_message()
            return
        else:
            window.show()
            window2.close()

    @pyqtSlot()
    def on_back_btn_clicked(self):
        self.ui.func_widget.setCurrentIndex(0)

    def input_warning(self):
        msgbox = QMessageBox(self)
        msgbox.setWindowIcon(QIcon(r"Icons/exclamation.png"))
        msgbox.setIconPixmap(QPixmap(r"Icons/shield-exclamation.png"))
        msgbox.setWindowTitle("W a r n i n g !")
        msgbox.setText("You must enter all inputs !")
        msgbox.setStandardButtons(QMessageBox.Ok)
        reply = msgbox.exec()
        if reply == QMessageBox.Ok:
            msgbox.close()

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
        msgbox2.setWindowIcon(QIcon(r"Icons/exclamation.png"))
        msgbox2.setIconPixmap(QPixmap(r"Icons/shield-exclamation.png"))
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


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Toyota")
        self.ui.full_menu_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn.setChecked(True)
        self.ui.page_name.setText(self.ui.home_btn2.text())
        self.ui.profile_side.clicked.connect(self.on_user_btn_clicked)
        self.ui.notifications.clicked.connect(self.on_nots_btn_clicked)
        self.ui.settings_btn.clicked.connect(self.on_setting_btn1_toggled)
        self.ui.settings_btn2.clicked.connect(self.on_setting_btn1_toggled)

    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)
        search_text = self.ui.search_box.text()
        if search_text:
            self.ui.label_8.setText(search_text)

    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.profile_btn.setChecked(True)
        self.ui.profile_btn2.setChecked(True)
        self.ui.page_name.setText(self.ui.profile_btn2.text())

    def on_nots_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(8)
        self.ui.page_name.setText(self.ui.notifications.text())

    def on_stackWidget_currentChanged(self, index):
        btn_list = self.ui.icon_menu_widget.findChildren(QPushButton) \
                   + self.ui.full_menu_widget.findChildren(QPushButton)

        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)

    def on_home_btn1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.page_name.setText(self.ui.home_btn2.text())

    def on_home_btn2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.page_name.setText(self.ui.home_btn2.text())

    def on_saved_btn1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.page_name.setText(self.ui.saved_btn2.text())

    def on_saved_btn2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.page_name.setText(self.ui.saved_btn2.text())

    def on_profile_btn1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.page_name.setText(self.ui.profile_btn2.text())

    def on_profile_btn2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.page_name.setText(self.ui.profile_btn2.text())

    def on_support_btn1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.page_name.setText(self.ui.support_btn2.text())

    def on_support_btn2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)
        self.ui.page_name.setText(self.ui.support_btn2.text())

    def on_about_btn1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.page_name.setText(self.ui.about_btn2.text())

    def on_about_btn2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.page_name.setText(self.ui.about_btn2.text())

    def on_setting_btn1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.page_name.setText(self.ui.settings_btn2.text())

    def on_rumion_btn_toggled(self):
        self.ui.stackedWidget_2.setCurrentIndex(1)

    @pyqtSlot()
    def on_logout_btn_clicked(self):
        window2.show()
        window.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # with open('style.css', 'r') as style_file:
    #     style_str = style_file.read()
    style_file = QFile("style.css")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())
    window = MainWindow()
    window2 = LoginWindow()
    window2.show()
    window.setWindowTitle("Toyota")
    window.setWindowIcon(QIcon(r"Icons/toyota-car-logo-6961.png"))
    sys.exit(app.exec())
