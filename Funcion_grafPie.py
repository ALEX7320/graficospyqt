# modulos de PySide2
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter, QColor, QFont
from PySide2.QtCore import Qt

# random para ejemplos
from random import randint

class Clase_GraficoPie():

    def __init__(self, parentgrid, theme=1):
        '''parentgrid: grid para ubicar el grafico | teme 1: predeterminado, teme 2: personalizado'''

        # 0. DATOS A REGISTRAR *-*-*-*-*-*-*-*-*-*-* 
        dato_titulo = "Ejemplo"
        dato_nombres = ["Uno", "Dos", "Tres", "Cuatro"]
        dato_colores = ["#e3722d", "#f0b904", "#6caa3f", "#42A5F8"]
        dato_datos = [
                # ---"Uno" ------ "Dos" --------- "Tres" --------- "Cuatro" ---
                randint(80,800), randint(80,800), randint(80,800), randint(80,800)
                ]        

        # 1. PIESLICE *-*-*-*-*-*-*-*-*-*-*
        listapieslice = self.creador_pieslice(valores = dato_datos, colores = dato_colores)

        # 2. PIESERIES *-*-*-*-*-*-*-*-*-*-*
        pieSeries = self.creador_pieseries(lista_pieslice = listapieslice, marcaindice=[1])

        # 3. PIESLICE LABELS *-*-*-*-*-*-*-*-*-*-*
        self.creador_pieslicelabels(
                                lista_pieslice = listapieslice,
                                valores = dato_datos,
                                nombres = dato_nombres,
                                decimales = 1)

        # 4. CHART *-*-*-*-*-*-*-*-*-*-*
        chart = self.creador_chart(pieseries = pieSeries, titulo = dato_titulo, theme=theme)

        # 5. CHARTVIEW *-*-*-*-*-*-*-*-*-*-*
        chartView = QtCharts.QChartView(chart)
        chartView.setRenderHint(QPainter.Antialiasing)

        if(theme==1):
                # TEMA PREDETERMINADO *-*-*-*-*-*-*-*-*-*-*

                # temas disponibles /-/-/-/
                'ChartThemeLight | ChartThemeBlueCerulean | ChartThemeDark | ChartThemeBrownSand'
                'ChartThemeBlueNcs | ChartThemeHighContrast | ChartThemeBlueIcy | ChartThemeQt'
                chart.setTheme(QtCharts.QChart.ChartThemeDark)
        else:
            # TEMA PERSONALIZADO *-*-*-*-*-*-*-*-*-*-*

            # definir color de letras /-/-/-/
            chartView.chart().setTitleBrush(QColor("white")) # titulo
            chartView.chart().legend().setLabelColor(QColor("white")) # etiquetas

            # personalizacion de fondo /-/-/-/
            chartView.chart().setBackgroundVisible(False) # quitar color
            chartView.setBackgroundBrush(QColor("#141f24")) # asignar color

        # 6. CONFIGURACIONES *-*-*-*-*-*-*-*-*-*-*

        # leyenda /-/-/-/
        'MarkerShapeDefault | MarkerShapeRectangle | MarkerShapeCircle | MarkerShapeFromSeries'
        chartView.chart().legend().setMarkerShape(QtCharts.QLegend.MarkerShapeCircle)

        # tamaño de letra /-/-/-/
        chartView.chart().setTitleFont(self.font_size(25)) # tamaño de titulo
        chartView.chart().legend().setFont(self.font_size(12))

        # fondo /-/-/-/
        chartView.chart().layout().setContentsMargins(0, 0, 0, 0) # quitar margenes
        chartView.chart().setBackgroundRoundness(0) # quitar bordes

        # font sub titulos /-/-/-/
        for sli in pieSeries.slices():
            sli.setLabelFont(self.font_size(14))

        # 7. RESTABLECER WIDGETS *-*-*-*-*-*-*-*-*-*-*
        'limpiar todos los elementos del widget'
        for i in reversed(range(parentgrid.count())): 
            parentgrid.itemAt(i).widget().deleteLater()
  
        # 8. INSERTAR GRAFICO *-*-*-*-*-*-*-*-*-*-*
        parentgrid.addWidget(chartView, 0, 0)


    def font_size(self, size):
        """cambiar tamaño de letra"""
        font = QFont()
        font.setPointSize(size)

        return font
   
    # 1. PIESLICE +-+-+
    def creador_pieslice(self, valores, colores):
        '''theme 1: predeterminado, theme 2: personalizado'''

        lista_pieslice = [] # almacena QPieSlice
        for dato,color in zip(valores, colores):
            pieSlice = QtCharts.QPieSlice()
            pieSlice.setValue(dato) # dato
            pieSlice.setColor(color) # color leyenda
            pieSlice.setLabelColor("white") # color valor

            # ubicacion de la señalizacion /-/-/-/
            'LabelOutside | LabelInsideHorizontal | LabelInsideTangential | LabelInsideNormal'
            pieSlice.setLabelPosition(QtCharts.QPieSlice.LabelOutside)

            lista_pieslice.append(pieSlice)

        return lista_pieslice
   
    # 2. PIESERIES +-+-+
    def creador_pieseries(self, lista_pieslice,marcaindice=[]):

        pieSeries = QtCharts.QPieSeries()

        for indice, sli in enumerate(lista_pieslice):
            if(indice in marcaindice):
                sli.setExploded(True)# resalta por indice

            pieSeries.append(sli)

        pieSeries.setHoleSize(0.0) # agujero tamaño
        pieSeries.setPieSize(0.6) # pie tamaño
        pieSeries.setLabelsVisible(True)
 
        return pieSeries

    # 3. PIESLICE LABELS +-+-+
    def creador_pieslicelabels(self, lista_pieslice, valores, nombres, decimales=2):
        """titulo a mostrar (con valor y porcentaje)"""
        for sli,valor,nombre in zip(lista_pieslice, valores, nombres):
            sli.setLabel(f"{nombre}: {valor} ({round(sli.percentage()*100,decimales)}%)")
    
    # 4. CHART +-+-+    
    def creador_chart(self, pieseries, titulo, theme):
        '''theme 1: predeterminado, theme 2: personalizado'''

        chart = QtCharts.QChart()
        chart.setTitle(titulo)
        chart.addSeries(pieseries)
        chart.legend().setVisible(True)

        # Alieamiento de las etiquetas /-/-/-/
        'AlignTop | AlignBottom | AlignLeft | AlignRight'
        chart.legend().setAlignment(Qt.AlignTop)

        # animaciones /-/-/-/
        'NoAnimation | SeriesAnimations | AllAnimations | GridAxisAnimations'
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        return chart
