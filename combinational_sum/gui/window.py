import json
import math

from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow, QPushButton
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QDoubleValidator

from combinational_sum.solver.problem import CombinationalSumProblem
from combinational_sum.solver.solver import CombinationalSumSolver


WINDOW_DIMENSIONS = (400, 400)
WINDOW_START_LOCATION = (50, 50)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(*WINDOW_DIMENSIONS))
        self.setWindowTitle("Combinational Sum Solver")

        target_value_line_label = QLabel(self)
        target_value_line_label.setText("Target value:")
        self.target_value_line = QLineEdit(self)
        self.target_value_line.setValidator(QDoubleValidator(-math.inf, math.inf, 2))
        self.target_value_line.move(120, 20)
        target_value_line_label.move(20, 20)

        available_values_line_label = QLabel(self)
        available_values_line_label.setText("Available values:")
        self.available_values_line = QLineEdit(self)
        self.available_values_line.setValidator(QDoubleValidator(-math.inf, math.inf, 2))
        self.available_values_line.move(120, 60)
        available_values_line_label.move(20, 60)

        calculate_button = QPushButton("Calculate", self)
        calculate_button.clicked.connect(self.on_click)
        calculate_button.resize(200, 32)
        calculate_button.move(80, 100)

        self.output_text = QLabel(self)
        self.output_text.setText("Enter target and available numbers, then click \"Calculate\"")
        self.output_text.resize(300, 250)
        self.output_text.setWordWrap(True)
        self.output_text.move(20, 140)

    def on_click(self):
        self.output_text.setText(
            f"Target value: {self.target_value_line.text()}\nAvailable values: {self.available_values_line.text()}"
        )
        try:
            problem = CombinationalSumProblem.from_strings(
                self.target_value_line.text(), self.available_values_line.text(),
            )
            self.output_text.setText("Solving...")
            solver = CombinationalSumSolver(problem)
            solution = solver.solve()
            self.output_text.setText(json.dumps(solution))
        except NotImplementedError:
            self.output_text.setText("Something wasn't implemented...")
        except ValueError:
            self.output_text.setText("Failed to parse the input...")

    def run(self):
        self.widget.show()
        self.app.exec_()
