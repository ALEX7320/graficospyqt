# modulos de PySide2
from PySide2.QtWidgets import QApplication,QMainWindow

# diseño
from view.ui_principal import Ui_Principal

# modulos de graficos
from Funcion_grafBarras import Clase_GraficoBarras
from Funcion_grafPie import Clase_GraficoPie

class Ui_venPrincipal(QMainWindow):
    def __init__(self):
        super(Ui_venPrincipal, self).__init__()

        # clase principal
        self.raiz = Ui_Principal()
        self.raiz.setupUi(self)

        # establecer grafico por defecto
        Clase_GraficoBarras(self.raiz.gridgrafico, theme=1)

        # grafico barras
        self.raiz.btn_prebar.clicked.connect(lambda : Clase_GraficoBarras(self.raiz.gridgrafico, theme=1))
        self.raiz.btn_perbar.clicked.connect(lambda : Clase_GraficoBarras(self.raiz.gridgrafico, theme=2))

        # grafico pie
        self.raiz.btn_prepie.clicked.connect(lambda : Clase_GraficoPie(self.raiz.gridgrafico, theme=1))
        self.raiz.btn_perpie.clicked.connect(lambda : Clase_GraficoPie(self.raiz.gridgrafico, theme=2))


if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    mi_aplicacion = Ui_venPrincipal()
    mi_aplicacion.show()
    sys.exit(app.exec_())
