import math

from PyQt5.QtWidgets import QLabel, QLineEdit, QMainWindow, QPushButton, QPlainTextEdit
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QDoubleValidator

from combinational_sum.solver.problem import CombinationalSumProblem
from combinational_sum.solver.solver import CombinationalSumSolver


WINDOW_DIMENSIONS = (400, 400)
WINDOW_START_LOCATION = (50, 50)


class MainWindow(QMainWindow):

    INSTRUCTIONS_TEXT = "Enter target and available numbers, then click \"Calculate\""

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

        calculate_button = QPushButton("Calculate", self)
        calculate_button.clicked.connect(self.on_click)
        calculate_button.resize(100, 32)
        calculate_button.move(240, 20)

        available_values_box_label = QLabel(self)
        available_values_box_label.setText("Available values:")
        self.available_values_box = QPlainTextEdit(self)
        self.available_values_box.resize(80, 200)
        self.available_values_box.move(40, 90)
        available_values_box_label.move(40, 60)

        solution_box_label = QLabel(self)
        solution_box_label.setText("Solution:")
        self.solution_box = QPlainTextEdit(self)
        self.solution_box.resize(80, 200)
        self.solution_box.move(220, 90)
        solution_box_label.move(220, 60)

        self.status_text = QLabel(self)
        self.status_text.setText(self.INSTRUCTIONS_TEXT)
        self.status_text.resize(300, 250)
        self.status_text.setWordWrap(True)
        self.status_text.move(20, 220)

    def on_click(self):
        try:
            self.solution_box.setPlainText("")
            problem = CombinationalSumProblem.from_strings(
                self.target_value_line.text(), self.available_values_box.toPlainText(),
            )
            self.status_text.setText("Solving...")
            solver = CombinationalSumSolver(problem)
            solution = solver.solve()
            if not solution.values:
                raise NoSolutionFoundError()
            self.solution_box.setPlainText(
                "\n".join([
                    f"{key.split(' ')[1]}: {value}" for key, value in solution.values.items()
                ])
            )
            self.status_text.setText(self.INSTRUCTIONS_TEXT)
        except NotImplementedError:
            self.status_text.setText("Error: Something wasn't implemented...")
        except ValueError:
            self.status_text.setText("Error: Failed to parse the input...")
        except NoSolutionFoundError:
            self.status_text.setText("No solution found")

    def run(self):
        self.widget.show()
        self.app.exec_()


class NoSolutionFoundError(Exception):
    pass
