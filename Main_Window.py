# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MnD.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_MainUI(object):
    def setupUi(self, MainUI):
        if not MainUI.objectName():
            MainUI.setObjectName(u"MainUI")
        MainUI.resize(800, 600)
        self.horizontalLayout_7 = QHBoxLayout(MainUI)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Select_M1 = QPushButton(MainUI)
        self.Select_M1.setObjectName(u"Select_M1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.Select_M1.sizePolicy().hasHeightForWidth())
        self.Select_M1.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.Select_M1)

        self.Label_M1 = QLabel(MainUI)
        self.Label_M1.setObjectName(u"Label_M1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.Label_M1.sizePolicy().hasHeightForWidth())
        self.Label_M1.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.Label_M1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Select_M2 = QPushButton(MainUI)
        self.Select_M2.setObjectName(u"Select_M2")
        sizePolicy.setHeightForWidth(self.Select_M2.sizePolicy().hasHeightForWidth())
        self.Select_M2.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.Select_M2)

        self.Label_M2 = QLabel(MainUI)
        self.Label_M2.setObjectName(u"Label_M2")
        sizePolicy1.setHeightForWidth(self.Label_M2.sizePolicy().hasHeightForWidth())
        self.Label_M2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.Label_M2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.Horizontal_Line1 = QFrame(MainUI)
        self.Horizontal_Line1.setObjectName(u"Horizontal_Line1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.Horizontal_Line1.sizePolicy().hasHeightForWidth())
        self.Horizontal_Line1.setSizePolicy(sizePolicy2)
        self.Horizontal_Line1.setFrameShape(QFrame.HLine)
        self.Horizontal_Line1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.Horizontal_Line1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Label_R1 = QLabel(MainUI)
        self.Label_R1.setObjectName(u"Label_R1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(2)
        sizePolicy3.setHeightForWidth(self.Label_R1.sizePolicy().hasHeightForWidth())
        self.Label_R1.setSizePolicy(sizePolicy3)

        self.horizontalLayout.addWidget(self.Label_R1)

        self.LineEdit_R1 = QLineEdit(MainUI)
        self.LineEdit_R1.setObjectName(u"LineEdit_R1")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.LineEdit_R1.sizePolicy().hasHeightForWidth())
        self.LineEdit_R1.setSizePolicy(sizePolicy4)

        self.horizontalLayout.addWidget(self.LineEdit_R1)

        self.Label_R1_unit = QLabel(MainUI)
        self.Label_R1_unit.setObjectName(u"Label_R1_unit")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.Label_R1_unit.sizePolicy().hasHeightForWidth())
        self.Label_R1_unit.setSizePolicy(sizePolicy5)

        self.horizontalLayout.addWidget(self.Label_R1_unit)

        self.Slider_R1 = QSlider(MainUI)
        self.Slider_R1.setObjectName(u"Slider_R1")
        sizePolicy1.setHeightForWidth(self.Slider_R1.sizePolicy().hasHeightForWidth())
        self.Slider_R1.setSizePolicy(sizePolicy1)
        self.Slider_R1.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.Slider_R1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.Label_R2 = QLabel(MainUI)
        self.Label_R2.setObjectName(u"Label_R2")
        sizePolicy3.setHeightForWidth(self.Label_R2.sizePolicy().hasHeightForWidth())
        self.Label_R2.setSizePolicy(sizePolicy3)

        self.horizontalLayout_2.addWidget(self.Label_R2)

        self.LineEdit_R2 = QLineEdit(MainUI)
        self.LineEdit_R2.setObjectName(u"LineEdit_R2")
        sizePolicy4.setHeightForWidth(self.LineEdit_R2.sizePolicy().hasHeightForWidth())
        self.LineEdit_R2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_2.addWidget(self.LineEdit_R2)

        self.Label_R2_unit = QLabel(MainUI)
        self.Label_R2_unit.setObjectName(u"Label_R2_unit")
        sizePolicy5.setHeightForWidth(self.Label_R2_unit.sizePolicy().hasHeightForWidth())
        self.Label_R2_unit.setSizePolicy(sizePolicy5)

        self.horizontalLayout_2.addWidget(self.Label_R2_unit)

        self.Slider_R2 = QSlider(MainUI)
        self.Slider_R2.setObjectName(u"Slider_R2")
        sizePolicy1.setHeightForWidth(self.Slider_R2.sizePolicy().hasHeightForWidth())
        self.Slider_R2.setSizePolicy(sizePolicy1)
        self.Slider_R2.setOrientation(Qt.Horizontal)

        self.horizontalLayout_2.addWidget(self.Slider_R2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Label_U = QLabel(MainUI)
        self.Label_U.setObjectName(u"Label_U")
        sizePolicy3.setHeightForWidth(self.Label_U.sizePolicy().hasHeightForWidth())
        self.Label_U.setSizePolicy(sizePolicy3)

        self.horizontalLayout_3.addWidget(self.Label_U)

        self.LineEdit_U = QLineEdit(MainUI)
        self.LineEdit_U.setObjectName(u"LineEdit_U")
        sizePolicy4.setHeightForWidth(self.LineEdit_U.sizePolicy().hasHeightForWidth())
        self.LineEdit_U.setSizePolicy(sizePolicy4)

        self.horizontalLayout_3.addWidget(self.LineEdit_U)

        self.label_U_unit = QLabel(MainUI)
        self.label_U_unit.setObjectName(u"label_U_unit")
        sizePolicy5.setHeightForWidth(self.label_U_unit.sizePolicy().hasHeightForWidth())
        self.label_U_unit.setSizePolicy(sizePolicy5)

        self.horizontalLayout_3.addWidget(self.label_U_unit)

        self.Slider_U = QSlider(MainUI)
        self.Slider_U.setObjectName(u"Slider_U")
        sizePolicy1.setHeightForWidth(self.Slider_U.sizePolicy().hasHeightForWidth())
        self.Slider_U.setSizePolicy(sizePolicy1)
        self.Slider_U.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.Slider_U)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.Vertical_Line1 = QFrame(MainUI)
        self.Vertical_Line1.setObjectName(u"Vertical_Line1")
        self.Vertical_Line1.setFrameShape(QFrame.VLine)
        self.Vertical_Line1.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_7.addWidget(self.Vertical_Line1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Figure_Name = QLabel(MainUI)
        self.Figure_Name.setObjectName(u"Figure_Name")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(5)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Figure_Name.sizePolicy().hasHeightForWidth())
        self.Figure_Name.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.Figure_Name)

        self.Figure_SelectBox = QComboBox(MainUI)
        self.Figure_SelectBox.setObjectName(u"Figure_SelectBox")
        sizePolicy6.setHeightForWidth(self.Figure_SelectBox.sizePolicy().hasHeightForWidth())
        self.Figure_SelectBox.setSizePolicy(sizePolicy6)

        self.horizontalLayout_6.addWidget(self.Figure_SelectBox)

        self.Button_Draw = QPushButton(MainUI)
        self.Button_Draw.setObjectName(u"Button_Draw")
        sizePolicy7 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(2)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.Button_Draw.sizePolicy().hasHeightForWidth())
        self.Button_Draw.setSizePolicy(sizePolicy7)

        self.horizontalLayout_6.addWidget(self.Button_Draw)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.Figure_Frame = QFrame(MainUI)
        self.Figure_Frame.setObjectName(u"Figure_Frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(12)
        sizePolicy8.setVerticalStretch(6)
        sizePolicy8.setHeightForWidth(self.Figure_Frame.sizePolicy().hasHeightForWidth())
        self.Figure_Frame.setSizePolicy(sizePolicy8)
        self.Figure_Frame.setMinimumSize(QSize(500, 350))
        self.Figure_Frame.setFrameShape(QFrame.StyledPanel)
        self.Figure_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.Figure_Frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Figure_Frame_Layout = QVBoxLayout()
        self.Figure_Frame_Layout.setObjectName(u"Figure_Frame_Layout")

        self.verticalLayout_6.addLayout(self.Figure_Frame_Layout)


        self.verticalLayout_4.addWidget(self.Figure_Frame)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 9)

        self.horizontalLayout_7.addLayout(self.verticalLayout_4)


        self.retranslateUi(MainUI)

        QMetaObject.connectSlotsByName(MainUI)
    # setupUi

    def retranslateUi(self, MainUI):
        MainUI.setWindowTitle(QCoreApplication.translate("MainUI", u"\u7535\u673a\u62d3\u5c55\u5b9e\u9a8c\u9879\u76ee", None))
        self.Select_M1.setText(QCoreApplication.translate("MainUI", u"\u9009\u62e9\u7535\u673a\u6a21\u578b", None))
        self.Label_M1.setText(QCoreApplication.translate("MainUI", u"TextLabel", None))
        self.Select_M2.setText(QCoreApplication.translate("MainUI", u"\u9009\u62e9\u8d1f\u8f7d\u6a21\u578b", None))
        self.Label_M2.setText(QCoreApplication.translate("MainUI", u"TextLabel", None))
        self.Label_R1.setText(QCoreApplication.translate("MainUI", u"\u8c03\u901f\u7535\u963b", None))
        self.Label_R1_unit.setText(QCoreApplication.translate("MainUI", u"\u03a9", None))
        self.Label_R2.setText(QCoreApplication.translate("MainUI", u"\u5f31\u78c1\u7535\u963b", None))
        self.Label_R2_unit.setText(QCoreApplication.translate("MainUI", u"\u03a9", None))
        self.Label_U.setText(QCoreApplication.translate("MainUI", u"\u8f93\u5165\u7535\u538b", None))
        self.label_U_unit.setText(QCoreApplication.translate("MainUI", u"V", None))
        self.Figure_Name.setText(QCoreApplication.translate("MainUI", u"\u673a\u7535\u53c2\u6570\u66f2\u7ebf", None))
        self.Button_Draw.setText(QCoreApplication.translate("MainUI", u"\u7ed8\u5236", None))
    # retranslateUi

