# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/cnc/6x11-sg-grinder-linuxcnc-config/SurfaceGrinder-linuxcnc-ui/debian/python3-semiauto-surfacegrinder/usr/lib/python3.11/dist-packages/semiauto_surfacegrinder/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(927, 484)
        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(89, 0))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.run_stop_button = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.run_stop_button.sizePolicy().hasHeightForWidth())
        self.run_stop_button.setSizePolicy(sizePolicy)
        self.run_stop_button.setMaximumSize(QtCore.QSize(120, 120))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.run_stop_button.setFont(font)
        self.run_stop_button.setCheckable(True)
        self.run_stop_button.setObjectName("run_stop_button")
        self.verticalLayout_2.addWidget(self.run_stop_button)
        self.halbutton_2 = HalButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.halbutton_2.sizePolicy().hasHeightForWidth())
        self.halbutton_2.setSizePolicy(sizePolicy)
        self.halbutton_2.setMaximumSize(QtCore.QSize(120, 120))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.halbutton_2.setFont(font)
        self.halbutton_2.setCheckable(True)
        self.halbutton_2.setObjectName("halbutton_2")
        self.verticalLayout_2.addWidget(self.halbutton_2)
        self.ref_all_button = ActionButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ref_all_button.sizePolicy().hasHeightForWidth())
        self.ref_all_button.setSizePolicy(sizePolicy)
        self.ref_all_button.setMinimumSize(QtCore.QSize(32, 27))
        self.ref_all_button.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ref_all_button.setFont(font)
        self.ref_all_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.ref_all_button.setStyleSheet("")
        self.ref_all_button.setObjectName("ref_all_button")
        self.verticalLayout_2.addWidget(self.ref_all_button)
        self.power_abutton_6 = ActionButton(self.groupBox_2)
        self.power_abutton_6.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.power_abutton_6.sizePolicy().hasHeightForWidth())
        self.power_abutton_6.setSizePolicy(sizePolicy)
        self.power_abutton_6.setMinimumSize(QtCore.QSize(32, 27))
        self.power_abutton_6.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.power_abutton_6.setFont(font)
        self.power_abutton_6.setCheckable(True)
        self.power_abutton_6.setObjectName("power_abutton_6")
        self.verticalLayout_2.addWidget(self.power_abutton_6)
        self.estop_abutton_5 = ActionButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.estop_abutton_5.sizePolicy().hasHeightForWidth())
        self.estop_abutton_5.setSizePolicy(sizePolicy)
        self.estop_abutton_5.setMinimumSize(QtCore.QSize(32, 27))
        self.estop_abutton_5.setMaximumSize(QtCore.QSize(100, 100))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.estop_abutton_5.setFont(font)
        self.estop_abutton_5.setCheckable(True)
        self.estop_abutton_5.setObjectName("estop_abutton_5")
        self.verticalLayout_2.addWidget(self.estop_abutton_5)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.Tabs = QtWidgets.QTabWidget(self.centralwidget)
        self.Tabs.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Tabs.sizePolicy().hasHeightForWidth())
        self.Tabs.setSizePolicy(sizePolicy)
        self.Tabs.setTabPosition(QtWidgets.QTabWidget.South)
        self.Tabs.setObjectName("Tabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(-1, 13, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.statusled_6 = StatusLED(self.tab)
        self.statusled_6.setObjectName("statusled_6")
        self.gridLayout_2.addWidget(self.statusled_6, 4, 1, 1, 1)
        self.statusled_7 = StatusLED(self.tab)
        self.statusled_7.setObjectName("statusled_7")
        self.gridLayout_2.addWidget(self.statusled_7, 3, 1, 1, 1)
        self.direction_indicator = HalLedIndicator(self.tab)
        self.direction_indicator.setState(False)
        self.direction_indicator.setProperty("pinBaseName", "")
        self.direction_indicator.setObjectName("direction_indicator")
        self.gridLayout_2.addWidget(self.direction_indicator, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 0, 1, 1)
        self.drolabel = DROLabel(self.tab)
        self.drolabel.setProperty("referenceType", 1)
        self.drolabel.setProperty("axisNumber", 0)
        self.drolabel.setProperty("latheMode", 0)
        self.drolabel.setObjectName("drolabel")
        self.gridLayout_2.addWidget(self.drolabel, 2, 0, 1, 1)
        self.statusled_2 = StatusLED(self.tab)
        self.statusled_2.setObjectName("statusled_2")
        self.gridLayout_2.addWidget(self.statusled_2, 0, 1, 1, 1)
        self.statusled = StatusLED(self.tab)
        self.statusled.setState(False)
        self.statusled.setObjectName("statusled")
        self.gridLayout_2.addWidget(self.statusled, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.drolabel_3 = DROLabel(self.tab)
        self.drolabel_3.setProperty("referenceType", 1)
        self.drolabel_3.setProperty("axisNumber", 2)
        self.drolabel_3.setProperty("latheMode", 0)
        self.drolabel_3.setObjectName("drolabel_3")
        self.gridLayout_2.addWidget(self.drolabel_3, 3, 0, 1, 1)
        self.drolabel_2 = DROLabel(self.tab)
        self.drolabel_2.setProperty("referenceType", 1)
        self.drolabel_2.setProperty("axisNumber", 1)
        self.drolabel_2.setProperty("latheMode", 0)
        self.drolabel_2.setObjectName("drolabel_2")
        self.gridLayout_2.addWidget(self.drolabel_2, 4, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_3.setAutoFillBackground(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayout_2 = QtWidgets.QFormLayout(self.groupBox_3)
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.traverse_limit_min = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.traverse_limit_min.setFont(font)
        self.traverse_limit_min.setText("")
        self.traverse_limit_min.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.traverse_limit_min.setObjectName("traverse_limit_min")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.traverse_limit_min)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.traverse_limit_max = QtWidgets.QLineEdit(self.groupBox_3)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.traverse_limit_max.setFont(font)
        self.traverse_limit_max.setText("")
        self.traverse_limit_max.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.traverse_limit_max.setObjectName("traverse_limit_max")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.traverse_limit_max)
        self.axisLabel = QtWidgets.QLabel(self.groupBox_3)
        self.axisLabel.setObjectName("axisLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.axisLabel)
        self.traverse_axis = QtWidgets.QComboBox(self.groupBox_3)
        self.traverse_axis.setObjectName("traverse_axis")
        self.traverse_axis.addItem("")
        self.traverse_axis.addItem("")
        self.traverse_axis.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.traverse_axis)
        self.traverse_speed = QtWidgets.QSpinBox(self.groupBox_3)
        self.traverse_speed.setMaximum(2000)
        self.traverse_speed.setObjectName("traverse_speed")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.traverse_speed)
        self.traverseLabel = QtWidgets.QLabel(self.groupBox_3)
        self.traverseLabel.setObjectName("traverseLabel")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.traverseLabel)
        self.gridLayout_4.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_4.setAutoFillBackground(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayout_3 = QtWidgets.QFormLayout(self.groupBox_4)
        self.formLayout_3.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.infeed_limit_min = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.infeed_limit_min.setFont(font)
        self.infeed_limit_min.setText("")
        self.infeed_limit_min.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.infeed_limit_min.setObjectName("infeed_limit_min")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.infeed_limit_min)
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.infeed_limit_max = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.infeed_limit_max.setFont(font)
        self.infeed_limit_max.setText("")
        self.infeed_limit_max.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.infeed_limit_max.setObjectName("infeed_limit_max")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.infeed_limit_max)
        self.axisLabel_2 = QtWidgets.QLabel(self.groupBox_4)
        self.axisLabel_2.setObjectName("axisLabel_2")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.axisLabel_2)
        self.infeed_axis = QtWidgets.QComboBox(self.groupBox_4)
        self.infeed_axis.setObjectName("infeed_axis")
        self.infeed_axis.addItem("")
        self.infeed_axis.addItem("")
        self.infeed_axis.addItem("")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.infeed_axis)
        self.stepoverLabel = QtWidgets.QLabel(self.groupBox_4)
        self.stepoverLabel.setObjectName("stepoverLabel")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.stepoverLabel)
        self.infeed_stepover = QtWidgets.QLineEdit(self.groupBox_4)
        self.infeed_stepover.setObjectName("infeed_stepover")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.infeed_stepover)
        self.infeed_speed = QtWidgets.QSpinBox(self.groupBox_4)
        self.infeed_speed.setMaximum(2000)
        self.infeed_speed.setObjectName("infeed_speed")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.infeed_speed)
        self.infeedLabel = QtWidgets.QLabel(self.groupBox_4)
        self.infeedLabel.setObjectName("infeedLabel")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.infeedLabel)
        self.gridLayout_4.addWidget(self.groupBox_4, 0, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_limits_button = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_limits_button.sizePolicy().hasHeightForWidth())
        self.save_limits_button.setSizePolicy(sizePolicy)
        self.save_limits_button.setMaximumSize(QtCore.QSize(120, 120))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.save_limits_button.setFont(font)
        self.save_limits_button.setCheckable(False)
        self.save_limits_button.setObjectName("save_limits_button")
        self.horizontalLayout.addWidget(self.save_limits_button)
        self.cancel_edit_limits = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_edit_limits.sizePolicy().hasHeightForWidth())
        self.cancel_edit_limits.setSizePolicy(sizePolicy)
        self.cancel_edit_limits.setMaximumSize(QtCore.QSize(120, 120))
        font = QtGui.QFont()
        font.setFamily("Sans")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.cancel_edit_limits.setFont(font)
        self.cancel_edit_limits.setCheckable(True)
        self.cancel_edit_limits.setObjectName("cancel_edit_limits")
        self.horizontalLayout.addWidget(self.cancel_edit_limits)
        self.gridLayout_4.addWidget(self.groupBox, 1, 1, 1, 2)
        self.Tabs.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 901, 441))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setObjectName("formLayout")
        self.infeedTypeLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.infeedTypeLabel.setObjectName("infeedTypeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.infeedTypeLabel)
        self.infeed_type = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.infeed_type.setObjectName("infeed_type")
        self.infeed_type.addItem("")
        self.infeed_type.addItem("")
        self.infeed_type.addItem("")
        self.infeed_type.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.infeed_type)
        self.infeedRepeatLabel_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.infeedRepeatLabel_2.setObjectName("infeedRepeatLabel_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.infeedRepeatLabel_2)
        self.infeed_reverse = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.infeed_reverse.setObjectName("infeed_reverse")
        self.infeed_reverse.addItem("")
        self.infeed_reverse.addItem("")
        self.infeed_reverse.addItem("")
        self.infeed_reverse.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.infeed_reverse)
        self.horizontalLayout_3.addLayout(self.formLayout)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.horizontalLayout_3.addLayout(self.formLayout_5)
        self.Tabs.addTab(self.tab_3, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_1)
        self.horizontalLayout_2.setContentsMargins(9, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(14)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.notificationwidget_2 = NotificationWidget(self.tab_1)
        self.notificationwidget_2.setObjectName("notificationwidget_2")
        self.horizontalLayout_2.addWidget(self.notificationwidget_2)
        self.Tabs.addTab(self.tab_1, "")
        self.gridLayout_3.addWidget(self.Tabs, 0, 1, 1, 1)
        Form.setCentralWidget(self.centralwidget)

        self.retranslateUi(Form)
        self.Tabs.setCurrentIndex(0)
        self.infeed_axis.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "MAIN"))
        self.run_stop_button.setText(_translate("Form", "START"))
        self.halbutton_2.setText(_translate("Form", "ENABLE"))
        self.halbutton_2.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}], \"property\": \"Enable\", \"expression\": \"ch[0]\", \"name\": \"isHomed\"}]"))
        self.halbutton_2.setProperty("pinBaseName", _translate("Form", "halui.user-enable"))
        self.ref_all_button.setText(_translate("Form", "REF ALL"))
        self.ref_all_button.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}], \"property\": \"Text\", \"expression\": \"\'HOMED\' if ch[0] else \'REF ALL\'\", \"name\": \"reference_all\"}]"))
        self.ref_all_button.setProperty("actionName", _translate("Form", "machine.home.all"))
        self.power_abutton_6.setText(_translate("Form", "POWER"))
        self.power_abutton_6.setProperty("actionName", _translate("Form", "machine.power.toggle"))
        self.estop_abutton_5.setText(_translate("Form", "E-STOP"))
        self.estop_abutton_5.setProperty("actionName", _translate("Form", "machine.estop.toggle"))
        self.statusled_6.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:joint.2.velocity\", \"trigger\": true}], \"property\": \"On\", \"expression\": \"bool(ch[0])\", \"name\": \"Motion\"}]"))
        self.statusled_7.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:joint.1.velocity\", \"trigger\": true}], \"property\": \"On\", \"expression\": \"bool(ch[0])\", \"name\": \"Motion\"}]"))
        self.label_6.setText(_translate("Form", "HOMED"))
        self.drolabel.setProperty("inchFormat", _translate("Form", "%9.4f"))
        self.drolabel.setProperty("millimeterFormat", _translate("Form", "%10.3f"))
        self.drolabel.setProperty("degreeFormat", _translate("Form", "%10.2f"))
        self.statusled_2.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:all_axes_homed\", \"trigger\": true}], \"property\": \"On\", \"expression\": \"ch[0]\", \"name\": \"Homed\"}]"))
        self.statusled.setProperty("rules", _translate("Form", "[{\"channels\": [{\"url\": \"status:joint.0.velocity\", \"trigger\": true}], \"property\": \"On\", \"expression\": \"bool(ch[0])\", \"name\": \"Motion\"}]"))
        self.label_9.setText(_translate("Form", "DIRECTION"))
        self.drolabel_3.setProperty("inchFormat", _translate("Form", "%9.4f"))
        self.drolabel_3.setProperty("millimeterFormat", _translate("Form", "%10.3f"))
        self.drolabel_3.setProperty("degreeFormat", _translate("Form", "%10.2f"))
        self.drolabel_2.setProperty("inchFormat", _translate("Form", "%9.4f"))
        self.drolabel_2.setProperty("millimeterFormat", _translate("Form", "%10.3f"))
        self.drolabel_2.setProperty("degreeFormat", _translate("Form", "%10.2f"))
        self.groupBox_3.setTitle(_translate("Form", "Traverse Limit"))
        self.label_8.setToolTip(_translate("Form", "AKA Table Left and Right"))
        self.label_8.setText(_translate("Form", "Min"))
        self.label_11.setToolTip(_translate("Form", "AKA Spindle Up and Down"))
        self.label_11.setText(_translate("Form", "Max"))
        self.axisLabel.setText(_translate("Form", "Axis"))
        self.traverse_axis.setItemText(0, _translate("Form", "X"))
        self.traverse_axis.setItemText(1, _translate("Form", "Z"))
        self.traverse_axis.setItemText(2, _translate("Form", "Y"))
        self.traverseLabel.setText(_translate("Form", "Spd"))
        self.groupBox_4.setTitle(_translate("Form", "Infeed Limit"))
        self.label_10.setToolTip(_translate("Form", "AKA Table Left and Right"))
        self.label_10.setText(_translate("Form", "Min"))
        self.label_12.setToolTip(_translate("Form", "AKA Spindle Up and Down"))
        self.label_12.setText(_translate("Form", "Max"))
        self.axisLabel_2.setText(_translate("Form", "Axis"))
        self.infeed_axis.setItemText(0, _translate("Form", "X"))
        self.infeed_axis.setItemText(1, _translate("Form", "Z"))
        self.infeed_axis.setItemText(2, _translate("Form", "Y"))
        self.stepoverLabel.setText(_translate("Form", "STP"))
        self.infeedLabel.setText(_translate("Form", "SPD"))
        self.groupBox.setTitle(_translate("Form", "Update"))
        self.save_limits_button.setText(_translate("Form", "Save"))
        self.cancel_edit_limits.setText(_translate("Form", "CANCEL"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab), _translate("Form", "TRAVERSE"))
        self.infeedTypeLabel.setText(_translate("Form", "Infeed Type"))
        self.infeed_type.setItemText(0, _translate("Form", "Left and Right Stops"))
        self.infeed_type.setItemText(1, _translate("Form", "Right Stop Only"))
        self.infeed_type.setItemText(2, _translate("Form", "Left Stop Only"))
        self.infeed_type.setItemText(3, _translate("Form", "None"))
        self.infeedRepeatLabel_2.setText(_translate("Form", "Infeed Repeat"))
        self.infeed_reverse.setItemText(0, _translate("Form", "Reverse At Either"))
        self.infeed_reverse.setItemText(1, _translate("Form", "Restart At Min"))
        self.infeed_reverse.setItemText(2, _translate("Form", "Restart At Max"))
        self.infeed_reverse.setItemText(3, _translate("Form", "None"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_3), _translate("Form", "Options"))
        self.Tabs.setTabText(self.Tabs.indexOf(self.tab_1), _translate("Form", "NOTIFICATIONS"))
from qtpyvcp.widgets.button_widgets.action_button import ActionButton
from qtpyvcp.widgets.display_widgets.dro_label import DROLabel
from qtpyvcp.widgets.display_widgets.notification_widget import NotificationWidget
from qtpyvcp.widgets.display_widgets.status_led import StatusLED
from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpyvcp.widgets.hal_widgets.hal_button import HalButton
from qtpyvcp.widgets.hal_widgets.hal_led import HalLedIndicator
