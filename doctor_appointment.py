# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dap1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMouseTracking(False)
        MainWindow.setStyleSheet("background-color: rgb(199, 200, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 30, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 120, 136, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 240, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 300, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 360, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 420, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 480, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(260, 120, 271, 31))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 180, 271, 31))
        self.textEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(260, 240, 271, 31))
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(260, 300, 271, 31))
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(260, 360, 271, 31))
        self.textEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(260, 420, 271, 31))
        self.textEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(260, 480, 271, 31))
        self.textEdit_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit_7.setObjectName("textEdit_7")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 500, 93, 28))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Doctor Appointment"))
        self.label_2.setText(_translate("MainWindow", "Patient Name"))
        self.label_3.setText(_translate("MainWindow", "Mobile Number"))
        self.label_4.setText(_translate("MainWindow", "Gender"))
        self.label_5.setText(_translate("MainWindow", "Age"))
        self.label_6.setText(_translate("MainWindow", "Appointment Id"))
        self.label_7.setText(_translate("MainWindow", "Appointment Day"))
        self.label_8.setText(_translate("MainWindow", "Checkup Type"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))


if __name__ == "__main__":
    import sys
    import mysql.connector
    con = mysql.connector.connect(
    host="localhost", user="root", password="root", database="daapt")
if con.is_connected():
    print("conect ayyindhi bhaiyya")

my_cursor = con.cursor()
create_table_query = """
    CREATE TABLE IF NOT EXISTS patientinfo (
        patient_name VARCHAR(255),
        mobile_number VARCHAR(20),
        gender VARCHAR(10),
        age VARCHAR(20),
        appointment_id VARCHAR(20),
        appointment_day VARCHAR(20),
        checkup_type VARCHAR(50)
    );

   """
my_cursor.execute(create_table_query)


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
def submit_data():
        patient_name = ui.textEdit.toPlainText()
        mobile_number = ui.textEdit_2.toPlainText()
        gender = ui.textEdit_3.toPlainText()
        age = ui.textEdit_4.toPlainText()
        appointment_id = ui.textEdit_5.toPlainText()
        appointment_day = ui.textEdit_6.toPlainText()
        checkup_type = ui.textEdit_7.toPlainText()
         # Check if any field is empty
        if not (patient_name and mobile_number and gender and age and appointment_id and appointment_day and checkup_type):
           QtWidgets.QMessageBox.critical(None, "Error", "Please fill out all fields.")
           return

        # Insert data into the table
        insert_query = """
            INSERT INTO patientinfo (patient_name, mobile_number, gender, age, appointment_id, appointment_day, checkup_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        data = (
            patient_name, mobile_number, gender, age, appointment_id, appointment_day, checkup_type
        )
        my_cursor.execute(insert_query, data)
        con.commit()
        QtWidgets.QMessageBox.information(None, "Success", "Data inserted successfully")

ui.pushButton.clicked.connect(submit_data) 

sys.exit(app.exec_())
