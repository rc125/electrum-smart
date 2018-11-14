import os
import traceback

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from electrum_smart import bitcoin
from electrum_smart.util import PrintError, bfh

from . import util

class SmartrewardsTab(QWidget):
    def __init__(self, parent=None):
        super(SmartrewardsTab, self).__init__(parent)
        self.create_layout()
        self.manager = None

    def create_layout(self):
        self.setObjectName("SmartrewardsList")
        self.resize(811, 457)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(9, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QWidget(self)
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setMinimumSize(QSize(0, 60))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_11 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_17 = QLabel(self.widget_2)
        font = QFont()
        font.setPointSize(19)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_12.addWidget(self.label_17)
        self.roundLabel = QLabel(self.widget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.roundLabel.sizePolicy().hasHeightForWidth())
        self.roundLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.roundLabel.setFont(font)
        self.roundLabel.setObjectName("roundLabel")
        self.horizontalLayout_12.addWidget(self.roundLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_19 = QLabel(self.widget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(13)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_13.addWidget(self.label_19)
        self.nextRoundLabel = QLabel(self.widget_2)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nextRoundLabel.sizePolicy().hasHeightForWidth())
        self.nextRoundLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.nextRoundLabel.setFont(font)
        self.nextRoundLabel.setObjectName("nextRoundLabel")
        self.horizontalLayout_13.addWidget(self.nextRoundLabel)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_21 = QLabel(self.widget_2)
        font = QFont()
        font.setPointSize(19)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_14.addWidget(self.label_21)
        self.percentLabel = QLabel(self.widget_2)
        font = QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.percentLabel.setFont(font)
        self.percentLabel.setObjectName("percentLabel")
        self.horizontalLayout_14.addWidget(self.percentLabel)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_14)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.tableWidget = QTableWidget(self.widget)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.widget1 = QWidget(self.widget)
        self.widget1.setMinimumSize(QSize(0, 40))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QSpacerItem(152, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QLabel(self.widget1)
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.sumLabel = QLabel(self.widget1)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.sumLabel.setFont(font)
        self.sumLabel.setObjectName("sumLabel")
        self.horizontalLayout_2.addWidget(self.sumLabel)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem1 = QSpacerItem(151, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.widget1)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, SmartrewardsList):
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("SmartrewardsList", "Form"))
        self.label_17.setText(_translate("SmartrewardsList", "SmartRewards round"))
        self.roundLabel.setText(_translate("SmartrewardsList", "0"))
        self.label_19.setText(_translate("SmartrewardsList", "Round ends"))
        self.nextRoundLabel.setText(_translate("SmartrewardsList", "25.12.1999"))
        self.label_21.setText(_translate("SmartrewardsList", "Current reward"))
        self.percentLabel.setText(_translate("SmartrewardsList", "0.00%"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SmartrewardsList", "Label"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SmartrewardsList", "Address"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SmartrewardsList", "Amount"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SmartrewardsList", "Eligible Amount"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SmartrewardsList", "Estimated SmartReward"))
        self.label.setText(_translate("SmartrewardsList", "Estimated SmartRewards"))
        self.sumLabel.setText(_translate("SmartrewardsList", "0 SMART"))

    def load_smartrewards(self, manager):
        self.manager = manager
        self.manager.send_subscriptions()

    def update(self):
        self.roundLabel.setText(self.manager.smartrewards_cycle.get_rewards_cycle())
        self.percentLabel.setText(str(self.manager.smartrewards_cycle.get_estimated_percent()))
        self.nextRoundLabel.setText(str(self.manager.smartrewards_cycle.get_rounds_end()))

    def subscribe_to_smartrewards(self):
        self.manager.subscribe_to_smartrewards()