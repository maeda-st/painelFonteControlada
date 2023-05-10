from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from Forms.main_form import Ui_MainForm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()