# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_select_window(object):
    def setupUi(self, select_window):
        select_window.setObjectName("select_window")
        select_window.resize(424, 580)
        self.centralwidget = QtWidgets.QWidget(select_window)
        self.centralwidget.setObjectName("centralwidget")
        self.info_table = QtWidgets.QTableWidget(self.centralwidget)
        self.info_table.setGeometry(QtCore.QRect(20, 260, 371, 192))
        self.info_table.setMaximumSize(QtCore.QSize(371, 192))
        self.info_table.setObjectName("info_table")
        self.info_table.setColumnCount(3)
        self.info_table.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.info_table.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.info_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.info_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.info_table.setHorizontalHeaderItem(2, item)
        self.flush_btn = QtWidgets.QPushButton(self.centralwidget)
        self.flush_btn.setGeometry(QtCore.QRect(150, 200, 91, 31))
        self.flush_btn.setObjectName("flush_btn")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(150, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 130, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.card_id_label = QtWidgets.QLabel(self.centralwidget)
        self.card_id_label.setGeometry(QtCore.QRect(120, 130, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.card_id_label.setFont(font)
        self.card_id_label.setText("")
        self.card_id_label.setObjectName("card_id_label")
        select_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(select_window)
        self.statusbar.setObjectName("statusbar")
        select_window.setStatusBar(self.statusbar)

        self.retranslateUi(select_window)
        QtCore.QMetaObject.connectSlotsByName(select_window)

    def retranslateUi(self, select_window):
        _translate = QtCore.QCoreApplication.translate
        select_window.setWindowTitle(_translate("select_window", "流水查询 "))
        item = self.info_table.verticalHeaderItem(0)
        item.setText(_translate("select_window", "1"))
        item = self.info_table.verticalHeaderItem(1)
        item.setText(_translate("select_window", "2"))
        item = self.info_table.verticalHeaderItem(2)
        item.setText(_translate("select_window", "3"))
        item = self.info_table.verticalHeaderItem(3)
        item.setText(_translate("select_window", "4"))
        item = self.info_table.verticalHeaderItem(4)
        item.setText(_translate("select_window", "5"))
        item = self.info_table.verticalHeaderItem(5)
        item.setText(_translate("select_window", "6"))
        item = self.info_table.verticalHeaderItem(6)
        item.setText(_translate("select_window", "7"))
        item = self.info_table.verticalHeaderItem(7)
        item.setText(_translate("select_window", "8"))
        item = self.info_table.verticalHeaderItem(8)
        item.setText(_translate("select_window", "9"))
        item = self.info_table.verticalHeaderItem(9)
        item.setText(_translate("select_window", "10"))
        item = self.info_table.horizontalHeaderItem(0)
        item.setText(_translate("select_window", "时间"))
        item = self.info_table.horizontalHeaderItem(1)
        item.setText(_translate("select_window", "款额"))
        item = self.info_table.horizontalHeaderItem(2)
        item.setText(_translate("select_window", "操作类型"))
        self.flush_btn.setText(_translate("select_window", "刷新"))
        self.label.setText(_translate("select_window", "流水查询"))
        self.label_2.setText(_translate("select_window", "卡号："))
