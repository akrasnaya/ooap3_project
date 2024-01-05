from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QLabel, QLineEdit, QVBoxLayout, QWidget, QRadioButton

from kinematics import Robot, InverseKinematics
from warning import WarningNotification

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.target_pose = [000.000] * 6

        self.setWindowTitle("Inverse Kinematics Calculation App")

        self.robot_label = QLabel("Выберите Модель Робота")

        self.robot_choice_puma = QRadioButton("Puma")
        self.robot_choice_ur5 = QRadioButton("UR5")
        self.robot_choice_ur10 = QRadioButton("UR10")

        self.position_label = QLabel("Введите желаемое положение конца стрелы: ")

        self.input_x = QLineEdit('000.000')
        self.input_x.textChanged.connect(self.set_x)
        self.input_y = QLineEdit('000.000')
        self.input_y.textChanged.connect(self.set_y)
        self.input_z = QLineEdit('000.000')
        self.input_z.textChanged.connect(self.set_z)
        self.input_r = QLineEdit('000.000')
        self.input_r.textChanged.connect(self.set_r)
        self.input_p = QLineEdit('000.000')
        self.input_p.textChanged.connect(self.set_p)
        self.input_yaw = QLineEdit('000.000')
        self.input_yaw.textChanged.connect(self.set_yaw)

        self.result_label = QLabel('RESULT')
        self.error_label = QLabel('ERRORS')

        layout = QVBoxLayout()
        layout.addWidget(self.robot_label)
        layout.addWidget(self.robot_choice_puma)
        layout.addWidget(self.robot_choice_ur5)
        layout.addWidget(self.robot_choice_ur10)
        layout.addWidget(self.position_label)
        layout.addWidget(QLabel('x position'))
        layout.addWidget(self.input_x)
        layout.addWidget(QLabel('y position'))
        layout.addWidget(self.input_y)
        layout.addWidget(QLabel('z position'))
        layout.addWidget(self.input_z)
        layout.addWidget(QLabel('roll position'))
        layout.addWidget(self.input_r)
        layout.addWidget(QLabel('pitch position'))
        layout.addWidget(self.input_p)
        layout.addWidget(QLabel('yaw position'))
        layout.addWidget(self.input_yaw)
        layout.addWidget(self.error_label)
        layout.addWidget(self.result_label)

        container = QWidget()
        container.setLayout(layout)

        # Устанавливаем центральный виджет Window.
        self.setCentralWidget(container)

    def set_x(self):
        try:
            x_pos = float(self.input_x.text())
        except ValueError:
            self.error_label.setText('x position invalid, please enter float number')
        self.target_pose[0] = x_pos

    def set_y(self):
        try:
            y_pos = float(self.input_y.text())
        except ValueError:
            self.error_label.setText('y position invalid, please enter float number')
        self.target_pose[1] = y_pos

    def set_z(self):
        try:
            z_pos = float(self.input_z.text())
        except ValueError:
            self.error_label.setText('z position invalid, please enter float number')
        self.target_pose[2] = z_pos

    def set_r(self):
        try:
            r_pos = float(self.input_r.text())
        except ValueError:
            self.error_label.setText('r position invalid, please enter float number')
        self.target_pose[3] = r_pos

    def set_p(self):
        try:
            p_pos = float(self.input_p.text())
        except ValueError:
            self.error_label.setText('p position invalid, please enter float number')
        self.target_pose[4] = p_pos

    def set_yaw(self):
        try:
            yaw_pos = float(self.input_yaw.text())
        except ValueError:
            self.error_label.setText('yaw position invalid, please enter float number')
        self.target_pose[5] = yaw_pos



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()