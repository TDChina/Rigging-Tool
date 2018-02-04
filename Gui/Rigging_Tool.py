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
        self.setMinimumHeight(500)
        self.setMinimumWidth(400)

        # 添加tabWidget

        tab_widget = qg.QTabWidget()
        tab_widget.addTab(NameTab(), "Name")
        tab_widget.addTab(DeformerTab(), "Deformer Weight Manager")
        tab_widget.addTab(OtherTab(), "Other Tool")

        main_layout = qg.QVBoxLayout()
        main_layout.addWidget(tab_widget)
        self.setLayout(main_layout)


# TODO：设置Name标签
class NameTab(qg.QWidget):
    def __init__(self):
        super(NameTab, self).__init__()

        file_name_la = qg.QLabel("File Name:")

        main_layout = qg.QVBoxLayout()
        main_layout.addWidget(file_name_la)
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