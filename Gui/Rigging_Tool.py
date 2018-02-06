#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : David
# Email  :499313351@qq.com
# 2018/2/4


import PySide.QtCore as qc
import PySide.QtGui as qg


class RiggingTool(qg.QDialog):
    def __init__(self,):
        super(RiggingTool, self).__init__()

        # 设置主窗口

        self.setWindowTitle("Rigging Tool")
        self.setWindowFlags(qc.Qt.WindowStaysOnTopHint)
        self.setFixedHeight(500)
        self.setFixedWidth(355)

        # 添加tabWidget

        tab_widget = qg.QTabWidget()
        tab_widget.addTab(UsualSettingTab(), "Usual Setting")
        tab_widget.addTab(DeformerTab(), "Deformer Weight Manager")
        tab_widget.addTab(OtherTab(), "Other Tool")

        main_layout = qg.QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)


# TODO：设置Usual Setting标签
class UsualSettingTab(qg.QWidget):
    def __init__(self):
        super(UsualSettingTab, self).__init__()

        # 设置整体布局

        self.setLayout(qg.QVBoxLayout())
        newname_widget = qg.QWidget()
        newname_widget.setFixedHeight(285)
        newname_widget.setFixedWidth(330)
        newname_widget.setLayout(qg.QVBoxLayout())

        self.layout().addWidget(newname_widget)
        name_text_layout = qg. QHBoxLayout()
        # name_text_layout.layout().setAlignment(qc.Qt.AlignTop)
        newname_widget.layout().addLayout(name_text_layout)

        # 添加New Name 以及其文本编辑器

        name_text_lb = qg.QLabel("New Name:")
        name_le = qg.QLineEdit()

        name_text_layout.addWidget(name_text_lb)
        name_text_layout.addWidget(name_le)

        # 设置默认递增方式（1-9/a-1)

        incremental_layout = qg.QHBoxLayout()
        # incremental_layout.layout().setAlignment(qc.Qt.AlignTop)
        newname_widget.layout().addLayout(incremental_layout)

        incremental_lb = qg.QLabel('Incremental:')
        incremental_combo = qg.QComboBox()
        incremental_combo.addItem('Numbers (0-9)')
        incremental_combo.addItem('Letters (a-z)')
        incremental_combo.setFixedWidth(100)

        incremental_layout.addWidget(incremental_lb)
        incremental_layout.addWidget(incremental_combo)

        # 添加No.Padding:和 数字选择框以及大小写切换radio

        incremental_options_layout = qg.QHBoxLayout()
        incremental_options_layout.layout().setAlignment(qc.Qt.AlignTop)
        newname_widget.layout().addLayout(incremental_options_layout)

        incremental_lb = qg.QLabel('No. Padding:')
        incremental_spin = qg.QSpinBox()
        incremental_spin.setMinimum(0)
        incremental_spin.setMaximum(10)

        lower_radio_radio = qg.QRadioButton('Lowercase')
        upper_radio_radio = qg.QRadioButton('Uppercase')
        lower_radio_radio.setVisible(False)
        upper_radio_radio.setVisible(False)
        lower_radio_radio.setChecked(True)

        incremental_options_layout.addWidget(incremental_lb)
        incremental_options_layout.addWidget(incremental_spin)
        incremental_options_layout.addWidget(lower_radio_radio)
        incremental_options_layout.addWidget(upper_radio_radio)

        # TODO：两个check、两个LineEdit（Prefix、Suffix）

        # TODO：Rename按钮。。。

        # TODO：find和replace两个labe 和对应的两个LIneEdit

        # TODO：选择模式的两个Ridio（All、Selected)

        # TODO：Replace按钮

        # TODO: Ctrl Maker

        main_layout = qg.QVBoxLayout()
        main_layout.addWidget(newname_widget)
        self.setLayout(main_layout)


# TODO：设置Deformer Weight Manager标签
class DeformerTab(qg.QWidget):
    def __init__(self):
        super(DeformerTab, self).__init__()

        file_name_la = qg.QLabel("File Name:")

        main_layout = qg.QVBoxLayout()
        main_layout.addWidget(file_name_la)
        self.setLayout(main_layout)


# TODO：设置Other Tool 标签
class OtherTab(qg.QWidget):
    def __init__(self):
        super(OtherTab, self).__init__()

        file_name_la = qg.QLabel("File Name:")

        main_layout = qg.QVBoxLayout()
        main_layout.addWidget(file_name_la)
        self.setLayout(main_layout)


dialog = None


def create():
    global dialog
    if dialog is None:
        dialog = RiggingTool()
    dialog.show()