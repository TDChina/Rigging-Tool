#!/usr/bin/env python
# coding:utf-8
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
        self.setFixedWidth(380)

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

        # 设置整体的布局方式

        self.setLayout(qg.QVBoxLayout())

        # ---------------------- Rename模块 ---------------------- #

        # 设置rename模块的布局

        usual_setting_widget = qg.QWidget()  # FIXME:改成占位符置顶
        usual_setting_widget.setFixedHeight(450)
        usual_setting_widget.setFixedWidth(350)
        usual_setting_widget.setLayout(qg.QVBoxLayout())
        self.layout().addWidget(usual_setting_widget)

        # 添加 RENAME 分割线

        rename_splitter = Splitter("RENAME")
        usual_setting_widget.layout().addWidget(rename_splitter)

        # 添加New Name 以及其文本编辑器

        name_text_layout = qg.QHBoxLayout()
        usual_setting_widget.layout().addLayout(name_text_layout)

        name_text_lb = qg.QLabel("New Name:")
        name_le = qg.QLineEdit()

        name_text_layout.addWidget(name_text_lb)
        name_text_layout.addWidget(name_le)

        # 设置默认递增方式（1-9/a-1)

        incremental_layout = qg.QHBoxLayout()
        usual_setting_widget.layout().addLayout(incremental_layout)

        incremental_lb = qg.QLabel('Incremental:')
        incremental_combo = qg.QComboBox()
        incremental_combo.addItem('Numbers (0-9)')
        incremental_combo.addItem('Letters (a-z)')
        incremental_combo.setFixedWidth(100)

        incremental_layout.addWidget(incremental_lb)
        incremental_layout.addWidget(incremental_combo)

        # 添加No.Padding:和 数字选择框以及大小写切换radio

        incremental_options_layout = qg.QHBoxLayout()
        usual_setting_widget.layout().addLayout(incremental_options_layout)

        incremental_lb = qg.QLabel('No. Padding:')
        incremental_spin = qg.QSpinBox()
        incremental_spin.setFixedWidth(35)
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

        # 两个check、两个LineEdit（Prefix、Suffix）
        fix_layout = qg.QHBoxLayout()
        usual_setting_widget.layout().addLayout(fix_layout)

        prefix_check = qg.QCheckBox('Prefix:')
        prefix_le = qg.QLineEdit()
        prefix_le.setEnabled(False)
        prefix_le.setFixedWidth(85)

        suffix_check = qg.QCheckBox('Suffix:')
        suffix_le = qg.QLineEdit()
        suffix_le.setEnabled(False)
        suffix_le.setFixedWidth(85)

        fix_layout.addWidget(prefix_check)
        fix_layout.addWidget(prefix_le)
        fix_layout.addWidget(suffix_check)
        fix_layout.addWidget(suffix_le)

        # Rename按钮。。。
        rename_bttn_layout = qg.QHBoxLayout()
        usual_setting_widget.layout().addLayout(rename_bttn_layout)

        rename_lb = qg.QLabel('e.g.')
        rename_bttn = qg.QPushButton('Rename')
        rename_bttn.setFixedWidth(55)
        rename_bttn.setFixedHeight(20)

        rename_bttn_layout.addWidget(rename_lb)
        rename_bttn_layout.addWidget(rename_bttn)

        # 添加 FIND/REPLACE 分割线

        replace_splitter = Splitter("FIND/REPLACE")
        usual_setting_widget.layout().addWidget(replace_splitter)

        # find和replace两个labe 和对应的两个LIneEdit

        find_layout = qg.QHBoxLayout()
        usual_setting_widget.layout().addLayout(find_layout)

        find_lb = qg.QLabel('Find:')
        find_lb.setFixedWidth(55)
        find_le = qg.QLineEdit()

        find_layout.addWidget(find_lb)
        find_layout.addWidget(find_le)

        replace_layout = qg.QHBoxLayout()
        usual_setting_widget.layout().addLayout(replace_layout)

        replace_lb = qg.QLabel('Replace:')
        replace_lb.setFixedWidth(55)
        replace_le = qg.QLineEdit()

        replace_layout.addWidget(replace_lb)
        replace_layout.addWidget(replace_le)

        # 选择模式的两个Ridio（All、Selected)

        selectkion_layout = qg.QHBoxLayout()
        usual_setting_widget.layout().addLayout(selectkion_layout)

        selectkion_mode_lb = qg.QLabel('Selection Mode:')
        all_radio = qg.QRadioButton('All')
        all_radio.setChecked(True)
        selectkion_radio = qg.QRadioButton('Selected')

        selectkion_layout.addWidget(selectkion_mode_lb)
        spacer_item = qg.QSpacerItem(5, 5, qg.QSizePolicy.Expanding)
        selectkion_layout.addSpacerItem(spacer_item)
        selectkion_layout.addWidget(all_radio)
        selectkion_layout.addWidget(selectkion_radio)

        # Replace和FindRename按钮

        replace_bttn_layout = qg.QVBoxLayout()
        replace_bttn_layout.layout().setAlignment(qc.Qt.AlignRight)
        usual_setting_widget.layout().addLayout(replace_bttn_layout)

        replace_bttn = qg.QPushButton('Replace')
        replace_bttn.setFixedWidth(70)
        replace_bttn.setFixedHeight(20)
        find_rename_bttn = qg.QPushButton('FindRename')
        find_rename_bttn.setFixedWidth(70)
        find_rename_bttn.setFixedHeight(20)

        replace_bttn_layout.addWidget(replace_bttn)
        replace_bttn_layout.addWidget(find_rename_bttn)

        # ---------------------- Ctrl Maker 模块 --------------------- #

        # TODO：设置Ctrl Maker模块的布局

        # 添加 CTRL MAKER 分割线

        ctrl_maker_splitter = Splitter("CTRL MAKER")
        usual_setting_widget.layout().addWidget(ctrl_maker_splitter)

        # 添加颜色设置

        color_setting_layout = qg.QHBoxLayout()
        usual_setting_widget.layout().addLayout(color_setting_layout)

        color_lb = qg.QLabel('Color:')
        rgt_color_bttn = qg.QPushButton('Rgt')
        rgt_color_bttn.setFixedWidth(50)
        mid_color_bttn = qg.QPushButton('Mid')
        mid_color_bttn.setFixedWidth(50)
        lft_color_bttn = qg.QPushButton('Lft')
        lft_color_bttn.setFixedWidth(50)
        other_color_lb = qg.QLabel('Other:')
        other_color_combo = qg.QComboBox()
        other_color_combo.addItem('Black')
        other_color_combo.addItem('Grey')
        other_color_combo.addItem('Blue')
        other_color_combo.addItem('DarkBlue')
        other_color_combo.addItem('Green')
        other_color_combo.addItem('DarkGreen')
        other_color_combo.addItem('Pink')
        other_color_combo.addItem('Orange')
        other_color_combo.addItem('Brown')
        other_color_combo.addItem('Purple')

        # 设置按钮背景颜色

        rgt_color_bttn.setStyleSheet("background-color: rgb(255, 0, 0);")
        mid_color_bttn.setStyleSheet("background-color: rgb(0, 255, 0);")
        lft_color_bttn.setStyleSheet("background-color: rgb(0, 0, 255);")
        other_color_combo.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, \
                                                stop:0 rgba(0, 0, 0, 255), \
                                                stop:0.099 rgba(0, 0, 0, 255), \
                                                stop:0.1 rgba(190, 190, 190, 255), \
                                                stop:0.199 rgba(190, 190, 190, 255), \
                                                stop:0.2 rgba(0, 0, 190, 255), \
                                                stop:0.29902 rgba(0, 0, 190, 255), \
                                                stop:0.3 rgba(0, 0, 128, 255), \
                                                stop:0.399 rgba(0, 0, 128, 255), \
                                                stop:0.4 rgba(0, 255, 0, 255), \
                                                stop:0.499 rgba(0, 255, 0, 255), \
                                                stop:0.5 rgba(0, 100, 0, 255), \
                                                stop:0.599 rgba(0, 100, 0, 255), \
                                                stop:0.6 rgba(255, 192, 203, 255), \
                                                stop:0.699 rgba(255, 192, 203, 255), \
                                                stop:0.7 rgba(255, 165, 0, 255), \
                                                stop:0.799 rgba(255, 165, 0, 255), \
                                                stop:0.803922 rgba(165, 42, 42, 255), \
                                                stop:0.899 rgba(165, 42, 42, 255), \
                                                stop:0.9 rgba(160, 32, 240, 255));")

        color_setting_layout.addWidget(color_lb)
        color_setting_layout.addWidget(rgt_color_bttn)
        color_setting_layout.addWidget(mid_color_bttn)
        color_setting_layout.addWidget(lft_color_bttn)
        color_setting_layout.addWidget(other_color_lb)
        color_setting_layout.addWidget(other_color_combo)

        # 添加至整体布局中

        main_layout = qg.QVBoxLayout()
        main_layout.addWidget(usual_setting_widget)
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


# ---------------------- 定义分割线的类 --------------------- #


class Splitter(qg.QWidget):
    def __init__(self, text=None):
        super(Splitter, self).__init__()

        self.setMinimumHeight(2)
        self.setLayout(qg.QHBoxLayout())
        self.layout().setContentsMargins(0, 0, 0, 0)
        self.layout().setSpacing(0)
        self.layout().setAlignment(qc.Qt.AlignVCenter)

        first_line = qg.QFrame()
        first_line.setFrameStyle(qg.QFrame.HLine)
        self.layout().addWidget(first_line)

        if text is None:
            return

        first_line.setMaximumWidth(5)

        font = qg.QFont()
        font.setBold(True)

        text_width = qg.QFontMetrics(font)
        width = text_width.width(text) + 6

        label = qg.QLabel()
        label.setText(text)
        label.setFont(font)
        label.setMaximumWidth(width)
        label.setAlignment(qc.Qt.AlignHCenter | qc.Qt.AlignVCenter)

        self.layout().addWidget(label)

        second_line = qg.QFrame()
        second_line.setFrameStyle(qg.QFrame.HLine)
        self.layout().addWidget(second_line)


dialog = None


def create():
    global dialog
    if dialog is None:
        dialog = RiggingTool()
    dialog.show()