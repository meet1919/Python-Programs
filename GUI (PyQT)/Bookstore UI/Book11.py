# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Meet\Desktop\UI Converter\Book11.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(330, 225)
        self.verticalLayout = QtWidgets.QVBoxLayout(form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Book_title = QtWidgets.QLabel(form)
        self.Book_title.setObjectName("Book_title")
        self.horizontalLayout.addWidget(self.Book_title)
        self.t1 = QtWidgets.QLineEdit(form)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        self.b1 = QtWidgets.QPushButton(form)
        self.b1.setObjectName("b1")
        self.horizontalLayout.addWidget(self.b1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Price = QtWidgets.QLabel(form)
        self.Price.setObjectName("Price")
        self.horizontalLayout_4.addWidget(self.Price)
        self.t2 = QtWidgets.QLineEdit(form)
        self.t2.setText("")
        self.t2.setObjectName("t2")
        self.horizontalLayout_4.addWidget(self.t2)
        spacerItem = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(form)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Quantity = QtWidgets.QLabel(form)
        self.Quantity.setObjectName("Quantity")
        self.horizontalLayout_2.addWidget(self.Quantity)
        self.t3 = QtWidgets.QLineEdit(form)
        self.t3.setObjectName("t3")
        self.horizontalLayout_2.addWidget(self.t3)
        self.b2 = QtWidgets.QPushButton(form)
        self.b2.setObjectName("b2")
        self.horizontalLayout_2.addWidget(self.b2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.total = QtWidgets.QLabel(form)
        self.total.setObjectName("total")
        self.horizontalLayout_3.addWidget(self.total)
        self.t4 = QtWidgets.QLineEdit(form)
        self.t4.setText("")
        self.t4.setObjectName("t4")
        self.horizontalLayout_3.addWidget(self.t4)
        spacerItem2 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)

        self.retranslateUi(form)
        self.b1.clicked.connect(self.t2.show)
        self.b2.clicked.connect(self.t4.show)
        QtCore.QMetaObject.connectSlotsByName(form)
        form.setTabOrder(self.t1, self.b1)
        form.setTabOrder(self.b1, self.t2)
        form.setTabOrder(self.t2, self.t3)
        form.setTabOrder(self.t3, self.b2)
        form.setTabOrder(self.b2, self.t4)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Book Manager"))
        self.Book_title.setText(_translate("form", "Book Title"))
        self.b1.setText(_translate("form", "Get Price"))
        self.Price.setText(_translate("form", "Price (Rs.)"))
        self.Quantity.setText(_translate("form", "Quantity "))
        self.b2.setText(_translate("form", "Total"))
        self.total.setText(_translate("form", "Total (Rs.)"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = Ui_form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())
