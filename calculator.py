from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QComboBox, QTabWidget, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from geometry import GeometryCalculator
import math
import styles

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator Complex')
        self.setGeometry(100, 100, 500, 700)

        # Layout principal
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Taburi
        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        # Tab Calculator Standard
        self.standard_tab = QWidget()
        self.tabs.addTab(self.standard_tab, 'Standard')

        # Tab Calculator Științific
        self.scientific_tab = QWidget()
        self.tabs.addTab(self.scientific_tab, 'Științific')

        # Tab Calculator Geometric
        self.geometry_tab = GeometryCalculator()
        self.tabs.addTab(self.geometry_tab, 'Geometrie')

        # Inițializare taburi
        self.initStandardTab()
        self.initScientificTab()

        # Stilizare interfață
        self.setStyleSheet(styles.stylesheet)

    def initStandardTab(self):
        layout = QGridLayout()
        self.standard_tab.setLayout(layout)

        # Afișaj principal
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)
        self.display.setFont(QFont('Arial', 16))
        layout.addWidget(self.display, 0, 0, 1, 4)

        # Butoane pentru operații aritmetice
        buttons = [
            'C', 'CE', '', '',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        positions = [(i+1, j) for i in range(5) for j in range(4)]

        for position, button_text in zip(positions, buttons):
            if button_text:
                button = QPushButton(button_text)
                button.setFont(QFont('Arial', 14))
                button.clicked.connect(self.on_standard_button_clicked)
                layout.addWidget(button, *position)

        # Afișaj pentru explicații
        self.explanation = QTextEdit()
        self.explanation.setReadOnly(True)
        self.explanation.setFixedHeight(100)
        layout.addWidget(self.explanation, 6, 0, 1, 4)

    def initScientificTab(self):
        layout = QGridLayout()
        self.scientific_tab.setLayout(layout)

        # Afișaj principal
        self.scientific_display = QLineEdit()
        self.scientific_display.setReadOnly(True)
        self.scientific_display.setAlignment(Qt.AlignRight)
        self.scientific_display.setFixedHeight(50)
        self.scientific_display.setFont(QFont('Arial', 16))
        layout.addWidget(self.scientific_display, 0, 0, 1, 6)

        # Butoane pentru operații științifice
        buttons = [
            'C', 'CE', '(', ')', 'π', 'e',
            'sin', 'cos', 'tan', 'log', 'ln', '√',
            '7', '8', '9', '/', '^', '%',
            '4', '5', '6', '*', '', '',
            '1', '2', '3', '-', '', '',
            '0', '.', '=', '+', '', ''
        ]

        positions = [(i+1, j) for i in range(6) for j in range(6)]

        for position, button_text in zip(positions, buttons):
            if button_text:
                button = QPushButton(button_text)
                button.setFont(QFont('Arial', 12))
                button.clicked.connect(self.on_scientific_button_clicked)
                layout.addWidget(button, *position)

        # Afișaj pentru explicații
        self.scientific_explanation = QTextEdit()
        self.scientific_explanation.setReadOnly(True)
        self.scientific_explanation.setFixedHeight(100)
        layout.addWidget(self.scientific_explanation, 7, 0, 1, 6)

    def on_standard_button_clicked(self):
        sender = self.sender()
        text = sender.text()
        if text == '=':
            try:
                expression = self.display.text()
                result = str(eval(expression))
                self.display.setText(result)
                self.explanation.append(f'{expression} = {result}')
            except Exception as e:
                self.display.setText('Eroare')
        elif text == 'C':
            self.display.clear()
        elif text == 'CE':
            self.display.setText(self.display.text()[:-1])
        else:
            self.display.setText(self.display.text() + text)

    def on_scientific_button_clicked(self):
        sender = self.sender()
        text = sender.text()
        if text == '=':
            try:
                expression = self.scientific_display.text()
                expression = self.parse_expression(expression)
                result = str(eval(expression))
                self.scientific_display.setText(result)
                self.scientific_explanation.append(f'{expression} = {result}')
            except Exception as e:
                self.scientific_display.setText('Eroare')
        elif text == 'C':
            self.scientific_display.clear()
        elif text == 'CE':
            self.scientific_display.setText(self.scientific_display.text()[:-1])
        else:
            self.scientific_display.setText(self.scientific_display.text() + text)

    def parse_expression(self, expression):
        # Înlocuiește funcțiile matematice cu cele din modulul math
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        expression = expression.replace('log', 'math.log10')
        expression = expression.replace('ln', 'math.log')
        expression = expression.replace('√', 'math.sqrt')
        expression = expression.replace('π', str(math.pi))
        expression = expression.replace('e', str(math.e))
        expression = expression.replace('^', '**')
        expression = expression.replace('%', '/100')
        return expression
