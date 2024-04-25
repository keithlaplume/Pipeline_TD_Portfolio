"""This code is considered proprietary property of Snowball Studios and its affiliates and is not for re-use in any way.
It is being provided to as sample code and portions have been blocked out to make it deliberately unusable.
If you are interested in reviewing a more complete code example with me please contact me at contact@keithlaplume.com"""


import os
import sys
import requests

from Qt import QtWidgets
from Qt import QtCore
from Qt import QtGui
from Qt.QtWidgets import QFileDialog
from Qt.QtWidgets import QAbstractItemView

import pathlib
from █████████ import ██████████
from █████████ import █████████


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        #Set up variables
        args = ██████████(sys.argv[1:])

        os.environ['██████'] = args.api.lower()
        os.environ['SB_SUBMIT'] = args.submit.lower()
        os.environ['SB_LOCATION'] = args.location.lower()
        os.environ['SB_SYNC_API'] = args.sync.lower()
        os.environ['SB_PATHS_API'] = args.paths.lower()
        os.environ['SB_MAYA_LIGHT_IMPORT'] = '1'
        os.environ['SB_FROST'] = str(pathlib.Path(__file__).parent.resolve())

        api = os.getenv('██████', '████████████████████████████')

        shows = █████████(api)

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)

        style = os.path.join(os.path.dirname(__file__), '../ui/frost.qss')
        qss_file = open(os.path.expandvars(style)).read()

        MainWindow.setStyleSheet(qss_file)

        MainWindow.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), '../ui/frost_dark.png')))
        MainWindow.setWindowTitle("Automator")

████████████████████
███████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████
█
        #Header
        self.header = QtWidgets.QHBoxLayout()
        self.header.setContentsMargins(20, 20, 20, 20)
        self.header.setObjectName("header")
        self.frost_logo = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.frost_logo.setFont(font)
        self.frost_logo.setText("")
        self.frost_logo.setPixmap(QtGui.QPixmap("ui/frost_dark.png"))
        self.frost_logo.setObjectName("frost_logo")
        self.header.addWidget(self.frost_logo)
        self.automator_title = QtWidgets.QLabel(self.centralwidget)
        self.automator_title.setText("AUTOMATOR/")
        font = QtGui.QFont()
        font.setPointSize(24)
        self.automator_title.setFont(font)
        self.automator_title.setProperty('style', 'h1')
        self.automator_title.setObjectName("automator_title")
        self.header.addWidget(self.automator_title)

        #Select Shows
        self.show_box = QtWidgets.QComboBox(self.centralwidget)
        self.show_box.setObjectName("show_box")
        for show in shows:
            self.show_box.addItem(show.upper())
██████████████████████████████
████████████████████████████████████
█████████████████████████████████████████████████
█████████████████████████████████████████████████████████
█████████████████████████████████████████
████████████████████████████████████████████████████████████████
█████████████████████████████████████████████

        spacerItem = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.header.addItem(spacerItem)

        #Select Server
        self.storm_label = QtWidgets.QLabel(self.centralwidget)
        self.storm_label.setText("STORM:")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.storm_label.setFont(font)
        self.storm_label.setObjectName("storm_label")
        self.storm_label.setProperty('style', 'h3')
        self.header.addWidget(self.storm_label)

        self.server_box = QtWidgets.QComboBox(self.centralwidget)
        self.server_box.addItems(['production', 'staging'])
        self.server_box.setObjectName("server_box")

        self.header.addWidget(self.server_box)

█████████████████████████████████████████████████████
█
██████████████
████████████████████████████████████████████████████████████████
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        #Left Column
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")

        self.column_left = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.column_left.setContentsMargins(5, 0, 5, 0)
        self.column_left.setObjectName("column_left")

        self.filters = QtWidgets.QFormLayout()
        self.filters.setObjectName("filters")

        self.entity_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.entity_label.setText("Entity Type:")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.entity_label.setFont(font)
        self.entity_label.setToolTipDuration(1)
        self.entity_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.entity_label.setObjectName("entity_label")
        self.filters.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.entity_label)
█
███████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████
██████████████████████████████████████
███████████████████████████████████████████
████████████████████████████████████████████████████████████████████████████████████

        self.task_label = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.task_label.setText("Task")
        self.task_label.setFont(font)
        self.task_label.setToolTipDuration(1)
        self.task_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.task_label.setObjectName("task_label")
        self.filters.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.task_label)

        self.task_box = QtWidgets.QComboBox(self.verticalLayoutWidget_5)
        self.task_box.setObjectName("task_box")
        self.task_box.setFont(font)
        self.task_box.addItems(['', 'art', 'edit', 'model', 'rig', 'surfacing', 'groom', 'cloth',
                                       'layout', 'blocking', 'animation', 'finaling', 'lighting',
                                       'comp', 'fx'])
        self.task_box.setCurrentIndex(12)
        self.filters.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.task_box)

        self.column_left.addLayout(self.filters)

        #Shot/Asset List
        self.entity_list = QtWidgets.QTreeWidget(self.verticalLayoutWidget_5)
        self.entity_list.headerItem().setText(0, "Shots")
        font = QtGui.QFont()
        font.setPointSize(12)
███████████████████████████████████████
██████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████████████████████████
█
███████████████████████████████████████████████████████████████████████████
█
█████████████████████████████████████████████████████
█
        #Column Middle
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.column_middle = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.column_middle.setContentsMargins(0, 0, 0, 0)
        self.column_middle.setObjectName("column_middle")
        self.column_middle_top = QtWidgets.QHBoxLayout()
        self.column_middle_top.setContentsMargins(0, -1, 0, -1)
        self.column_middle_top.setObjectName("column_middle_top")

        self.add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.add.setText("ADD")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icons/sg/nav_icon_plus_light.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add.setIcon(icon)
        self.add.setObjectName("add")
        self.column_middle_top.addWidget(self.add)

        self.save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.save.setText("SAVE")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/icons/sg/icon_save.png"),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
█████████████████████████████████
████████████████████████████████████████
████████████████████████████████████████████████████
█
        self.clear = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clear.setText("CLEAR")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap("ui/icons/sg/review_app_overlay_close.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear.setIcon(icon2)
        self.clear.setObjectName("clear")
        self.column_middle_top.addWidget(self.clear)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.column_middle_top.addItem(spacerItem1)

        self.column_middle.addLayout(self.column_middle_top)
        self.batch_layout = QtWidgets.QGridLayout()

        self.batch_layout.setObjectName("batch_layout")

        self.batch_name_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.batch_name_line.setObjectName("batch_name_line")
        self.batch_layout.addWidget(self.batch_name_line, 1, 1, 1, 1)

        self.batch_name_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.batch_name_label.setText("BATCH NAME:")
        self.batch_name_label.setObjectName("batch_name_label")
███████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████████
█
        #This is where the jobs should go
        self.job = JobWidget(self.column_middle)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)

        self.column_middle.addItem(spacerItem2)

        #Right Column
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")

        self.column_right = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.column_right.setContentsMargins(5, 0, 5, 0)
        self.column_right.setObjectName("column_right")

        self.deadline_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.deadline_label.setText("DEADLINE SUBMISSION")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.deadline_label.setFont(font)
        self.deadline_label.setObjectName("deadline_label")
█████████████████████████████████████████████████████████
█
████████████████████████████████████████████████████████████████████████
████████████████████████████████████████
        font = QtGui.QFont()
        font.setPointSize(10)
        self.site_label.setFont(font)
        self.site_label.setObjectName("site_label")
        self.column_right.addWidget(self.site_label)

        self.site_box = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.site_box.setObjectName("site_box")
        self.site_box.addItem("TOR")
        self.site_box.addItem("TLV")
        self.site_box.addItem("PFX")
        self.column_right.addWidget(self.site_box)

        self.priority_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.priority_label.setText("PRIORITY")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.priority_label.setFont(font)
        self.priority_label.setObjectName("priority_label")
        self.column_right.addWidget(self.priority_label)

        self.priority_spinner = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.priority_spinner.setObjectName("priority_spinner")
        self.priority_spinner.setValue(50)
        self.column_right.addWidget(self.priority_spinner)
█
████████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████
█████████████████████████████
██████████████████████████████
        self.machines_label.setFont(font)
        self.machines_label.setObjectName("machines_label")
        self.column_right.addWidget(self.machines_label)

        self.machines_spinner = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.machines_spinner.setObjectName("machines_spinner")
        self.priority_spinner.setValue(1)
        self.column_right.addWidget(self.machines_spinner)

        self.timeout_label = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.timeout_label.setText("TIMEOUT")
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeout_label.setFont(font)
        self.timeout_label.setObjectName("timeout_label")
        self.column_right.addWidget(self.timeout_label)

        self.timeout_spinner = QtWidgets.QSpinBox(self.verticalLayoutWidget_3)
        self.timeout_spinner.setValue(60)
        self.timeout_spinner.setObjectName("timeout_spinner")
        self.column_right.addWidget(self.timeout_spinner)
█
█████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████
        font = QtGui.QFont()
        font.setPointSize(10)
        self.batch_label.setFont(font)
        self.batch_label.setObjectName("batch_label")
        self.column_right.addWidget(self.batch_label)

        self.batch_box = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.batch_box.setObjectName("batch_box")
        self.batch_box.addItem("Single")
        self.batch_box.addItem("All")
        self.column_right.addWidget(self.batch_box)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                            QtWidgets.QSizePolicy.Expanding)
        self.column_right.addItem(spacerItem3)

        #Submit and Log Buttons
        self.submit_button = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.submit_button.setText("SUBMIT")

        font = QtGui.QFont()
        font.setPointSize(16)
        self.submit_button.setFont(font)
        self.submit_button.setObjectName("submit_button")
████████████████████████████████████████████████████████
████████████████████████████████████████████████████████
█
██████████████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████
█████████████████████████████
        font.setPointSize(12)
        self.logs_button.setFont(font)
        self.logs_button.setObjectName("logs_button")
        self.column_right.addWidget(self.logs_button)
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def populate_entities(self):
        print("delete entities")
        QtWidgets.QTreeWidget.clear(self.entity_list)
        print("populate entities")
        episode_list = self.get_episodes(str(self.show_box.currentText()))
        if episode_list != None:
            for episode in episode_list:
                item_0 = QtWidgets.QTreeWidgetItem(self.entity_list, [episode])

                shot_list = self.get_shots('nm01', episode)
                if shot_list != None:
                    for shot in self.get_shots('nm01', episode):
                        item_1 = QtWidgets.QTreeWidgetItem(item_0, [shot])
█
█
███████████████████████████████████████
█
        api = os.getenv('██████', '████████████████████████████')

        episodes_info = requests.get('████████████████████████████/episodes?show={}'.format(show_code)).json()

        episode_list = []

        for episode in episodes_info:
            episode_list.append(episode['name'])

        episode_list.sort()

        return episode_list

    def get_shots(self, show_code, episode):

#        for episode in episode_list:
#            self.get_shots(show_code, episode)

        if " " not in episode:
            response = requests.get('████████████████████████████/shots?show={}&episode={}'.format(show_code, episode))

            if response.status_code == 200:
                shots_info = response.json()

                shot_list = []
█
████████████████████████████████████████
███████████████████████████████████████████████████

                shot_list.sort()

                return shot_list

    def submit(self):
        print("submit")

        shots = self.entity_list.selectedItems()
        shot_list = []

        for shot in shots:
            shot_list.append(shot.text(0))

        show = self.show_box.currentText()
        entity = self.entity_box.currentText()
        task = self.task_box.currentText()
        script = self.job.filename.text()
        site = self.site_box.currentText()
        priority = self.priority_spinner.value()
        machines = self.machines_spinner.value()
        timeout = self.timeout_spinner.value()
█
█
████████████████████
██████████████████████
████████████████████
█████████████████████████
██████████████████████
████████████████████
        print(priority)
        print(machines)
        print(timeout)
        print()


class JobWidget(QtWidgets.QWidget):

    def __init__(self, layout):
        super().__init__()
        self.initUI(layout)

    def initUI(self, layout):
        self.job_item = QtWidgets.QFrame()
        self.job_item.setStyleSheet("border: 2px solid rgb(75,75,75)")
        layout.addWidget(self.job_item)

        self.verticalLayoutWidget = QtWidgets.QWidget(self.job_item)
        self.verticalLayoutWidget.setStyleSheet("border: none")

        self.render_verticalLayout = QtWidgets.QVBoxLayout(self.job_item)
        self.render_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.render_verticalLayout.setObjectName("render_verticalLayout")
        layout.addLayout(self.render_verticalLayout)

███████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████████████████
██████████████████████████████████████████████████████████████████████████████
█
████████████████████████████████████████████████████████████████████████
████████████████████████████████████████████████████████
████████████████████████████████████████████
█████████████████████████████████████████████████████
        self.render_label.setStyleSheet('border: none')
        self.render_horizontalLayout.addWidget(self.render_label)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.render_horizontalLayout.addItem(spacerItem)

        self.clear_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.clear_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/icons/sg/review_app_overlay_close.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_button.setIcon(icon)
        self.clear_button.setObjectName("clear_button")
        self.render_horizontalLayout.addWidget(self.clear_button)
        self.render_verticalLayout.addLayout(self.render_horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.file_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.file_button.setText("")

        self.file_button.clicked.connect(self.fileDialog)
█
██████████████████████████████
██████████████████████████████████████████████████████████████████████████████████
█████████████████████████████████████████████████████████████
████████████████████████████████████████
██████████████████████████████████████████████████████
████████████████████████████████████████████████████████████
█
        self.filename = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.filename.setObjectName("filepath")
        self.horizontalLayout_2.addWidget(self.filename)
        self.render_verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.arg_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.arg_label.setObjectName("label_2")
        self.arg_label.setText("ARGUMENTS")
        self.arg_label.setProperty('style', 'h6')
        self.arg_label.setStyleSheet('border: none')
        self.horizontalLayout_3.addWidget(self.arg_label)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.render_verticalLayout.addLayout(self.horizontalLayout_3)

    def fileDialog(self):
        print("clicked")
        #option = self.filepath()
█████████████████████████████████████████████████████
███████████████████████████████████████████
█
█
███████████████████████████

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
