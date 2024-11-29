from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QComboBox
from PyQt5.QtGui import QFont
import math

class GeometryCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        # Titlu
        self.geometry_label = QLabel('Selectează Calculul Geometric:')
        layout.addWidget(self.geometry_label, 0, 0, 1, 2)

        # Combobox pentru selecția calculelor
        self.geometry_combo = QComboBox()
        self.geometry_combo.addItems([
            'Aria Cercului',
            'Aria Dreptunghiului',
            'Aria Triunghiului',
            'Volumul Cubului',
            'Volumul Sferei',
            'Volumul Cilindrului'
        ])
        layout.addWidget(self.geometry_combo, 0, 2, 1, 2)

        # Inputuri
        self.geometry_input1 = QLineEdit()
        self.geometry_input1.setPlaceholderText('Input 1')
        layout.addWidget(self.geometry_input1, 1, 0, 1, 2)

        self.geometry_input2 = QLineEdit()
        self.geometry_input2.setPlaceholderText('Input 2 (dacă este necesar)')
        layout.addWidget(self.geometry_input2, 1, 2, 1, 2)

        self.geometry_input3 = QLineEdit()
        self.geometry_input3.setPlaceholderText('Input 3 (dacă este necesar)')
        layout.addWidget(self.geometry_input3, 2, 0, 1, 2)

        # Buton pentru calcul
        self.geometry_calculate_button = QPushButton('Calculează')
        self.geometry_calculate_button.clicked.connect(self.calculate_geometry)
        layout.addWidget(self.geometry_calculate_button, 2, 2, 1, 2)

        # Rezultat
        self.geometry_result = QLineEdit()
        self.geometry_result.setReadOnly(True)
        self.geometry_result.setPlaceholderText('Rezultat')
        layout.addWidget(self.geometry_result, 3, 0, 1, 4)

        # Afișaj pentru explicații
        self.explanation = QTextEdit()
        self.explanation.setReadOnly(True)
        self.explanation.setFixedHeight(200)
        layout.addWidget(self.explanation, 4, 0, 1, 4)

    def calculate_geometry(self):
        calculation = self.geometry_combo.currentText()
        input1 = self.geometry_input1.text()
        input2 = self.geometry_input2.text()
        input3 = self.geometry_input3.text()
        result = ''
        explanation = ''
        try:
            if calculation == 'Aria Cercului':
                raza = float(input1)
                aria = math.pi * raza **2
                result = str(aria)
                explanation = f'Aria = π × r² = π × {raza}² = {aria}'
            elif calculation == 'Aria Dreptunghiului':
                lungime = float(input1)
                latime = float(input2)
                aria = lungime * latime
                result = str(aria)
                explanation = f'Aria = Lungime × Lățime = {lungime} × {latime} = {aria}'
            elif calculation == 'Aria Triunghiului':
                baza = float(input1)
                inaltime = float(input2)
                aria = 0.5 * baza * inaltime
                result = str(aria)
                explanation = f'Aria = ½ × Bază × Înălțime = ½ × {baza} × {inaltime} = {aria}'
            elif calculation == 'Volumul Cubului':
                latura = float(input1)
                volum = latura ** 3
                result = str(volum)
                explanation = f'Volumul = Latura³ = {latura}³ = {volum}'
            elif calculation == 'Volumul Sferei':
                raza = float(input1)
                volum = (4/3) * math.pi * raza ** 3
                result = str(volum)
                explanation = f'Volumul = (4/3) × π × r³ = (4/3) × π × {raza}³ = {volum}'
            elif calculation == 'Volumul Cilindrului':
                raza = float(input1)
                inaltime = float(input2)
                volum = math.pi * raza ** 2 * inaltime
                result = str(volum)
                explanation = f'Volumul = π × r² × h = π × {raza}² × {inaltime} = {volum}'
            self.geometry_result.setText(result)
            self.explanation.append(explanation)
        except Exception as e:
            self.geometry_result.setText('Eroare')
