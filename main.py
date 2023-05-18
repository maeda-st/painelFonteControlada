import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt
from Forms.main_form import Ui_MainForm
from Forms.form_teste_saida import Ui_FormTesteSaida

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.janela_teste_saida = None

        # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Obter o tamanho do monitor primário
        screen = QApplication.primaryScreen()
        mainScreenRect = screen.availableGeometry()

        # Definir a posição da janela no canto superior esquerdo
        self.move(mainScreenRect.topLeft())

        self.ui.btTestes.clicked.connect(self.mudaJanela)

    def mudaJanela(self):
        self.janela_teste_saida = MainTesteSaida()
        #self.janela2.showMaximized()
        self.janela_teste_saida.show()
        # self.hide()
        self.close()

class MainTesteSaida(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuração da interface do usuário gerada pelo Qt Designer
        self.ui = Ui_FormTesteSaida()
        self.ui.setupUi(self)

        # Remover a barra de título e ocultar os botões de maximizar e minimizar
        # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        # Obter o tamanho do monitor primário
        screen = QApplication.primaryScreen()
        mainScreenRect = screen.availableGeometry()

        # Definir a posição da janela no canto superior esquerdo
        self.move(mainScreenRect.topLeft())

        self.ui.btVoltar.clicked.connect(self.voltar)

    def voltar(self):
        self.close()# Chama o evento closedEvent

    def closeEvent(self, event):
        self.origem = MainWindow()
        #self.origem.showMaximized()
        self.origem.show()
        event.accept()# esse método aceita o pedido de fechamento....

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
