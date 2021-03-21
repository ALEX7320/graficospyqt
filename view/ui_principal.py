# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_principalWKYbSF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Principal(object):
    def setupUi(self, Principal):
        if not Principal.objectName():
            Principal.setObjectName(u"Principal")
        Principal.resize(771, 669)
        self.centralwidget = QWidget(Principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(30, 30, 30, 30)
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(15, 15, 15, 15)
        self.btn_prebar = QPushButton(self.groupBox)
        self.btn_prebar.setObjectName(u"btn_prebar")
        self.btn_prebar.setMinimumSize(QSize(0, 45))

        self.verticalLayout.addWidget(self.btn_prebar)

        self.btn_perbar = QPushButton(self.groupBox)
        self.btn_perbar.setObjectName(u"btn_perbar")
        self.btn_perbar.setMinimumSize(QSize(0, 45))

        self.verticalLayout.addWidget(self.btn_perbar)


        self.gridLayout_3.addWidget(self.groupBox, 2, 0, 1, 1)

        self.gridgrafico = QGridLayout()
        self.gridgrafico.setObjectName(u"gridgrafico")

        self.gridLayout_3.addLayout(self.gridgrafico, 1, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setStyleSheet(u"font-size:25px;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 150))
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.btn_prepie = QPushButton(self.groupBox_2)
        self.btn_prepie.setObjectName(u"btn_prepie")
        self.btn_prepie.setMinimumSize(QSize(0, 45))

        self.verticalLayout_2.addWidget(self.btn_prepie)

        self.btn_perpie = QPushButton(self.groupBox_2)
        self.btn_perpie.setObjectName(u"btn_perpie")
        self.btn_perpie.setMinimumSize(QSize(0, 45))

        self.verticalLayout_2.addWidget(self.btn_perpie)


        self.gridLayout_3.addWidget(self.groupBox_2, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principal)

        QMetaObject.connectSlotsByName(Principal)
    # setupUi

    def retranslateUi(self, Principal):
        Principal.setWindowTitle(QCoreApplication.translate("Principal", u"Graficos - ALEX7320", None))
        self.groupBox.setTitle(QCoreApplication.translate("Principal", u"BARRAS", None))
        self.btn_prebar.setText(QCoreApplication.translate("Principal", u"Predeterminado", None))
        self.btn_perbar.setText(QCoreApplication.translate("Principal", u"Personalizado", None))
        self.label.setText(QCoreApplication.translate("Principal", u"GR\u00c1FICOS", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Principal", u"PIE", None))
        self.btn_prepie.setText(QCoreApplication.translate("Principal", u"Predeterminado", None))
        self.btn_perpie.setText(QCoreApplication.translate("Principal", u"Personalizado", None))
    # retranslateUi

