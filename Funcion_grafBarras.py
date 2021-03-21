# modulos de PySide2
from PySide2.QtCharts import QtCharts
from PySide2.QtCore import Qt, QMargins 
from PySide2.QtGui import QColor, QFont

# random para ejemplos
from random import randint

class Clase_GraficoBarras():

    def __init__(self, parentgrid, theme=1):
        '''parentgrid: grid para ubicar el grafico | teme 1: predeterminado, teme 2: personalizado'''

        # 0. DATOS A REGISTRAR *-*-*-*-*-*-*-*-*-*-* 
        dato_titulo = "Ejemplo"
        dato_titulo_left = "Titulo izquierda" # puede ser None
        dato_titulo_down = "Titulo abajo" # puede ser None

        dato_nombres = ["CASO A", "CASO B", "CASO C"]
        dato_etiquetas = ["TAG 1", "TAG 2", "TAG 3", "TAG 4"]
        dato_colores = ["#e3722d", "#f0b904", "#6caa3f", "#42A5F8"]
        dato_datos = [
                # ---"CASO A" ------- "CASO B" ------- "CASO C" --
                [randint(80,800), randint(80,800), randint(80,800)], # TAG 1
                [randint(80,800), randint(80,800), randint(80,800)], # TAG 2
                [randint(80,800), randint(80,800), randint(80,800)], # TAG 3
                [randint(80,800), randint(80,800), randint(80,800)], # TAG 4

                ]
        # obtener valor maximo /-/-/-/
        valormaximo = max([max(dato) for dato in dato_datos])
        
        # 1. BARSET *-*-*-*-*-*-*-*-*-*-*
        listabarset = []
        for titulo,datos,color in zip(dato_etiquetas,dato_datos,dato_colores):
            barSet = self.creador_barset(titulo = titulo, datos = datos, color = color)
            listabarset.append(barSet)

        # 2. BARSERIES *-*-*-*-*-*-*-*-*-*-*
        barSeries = self.creador_barseries(
                        listaelementos = listabarset, 
                        rotacion = 0, # angulos de rotacion
                        formato = "@value")

        # 3. NAMEAXIS *-*-*-*-*-*-*-*-*-*-*
        nameAxis = self.creador_nameaxis(listanombres = dato_nombres)

        # 4. VALUEAXIS *-*-*-*-*-*-*-*-*-*-*
        valueAxis = self.creador_valueaxis(formato = "%i ", valormax = valormaximo)

        # 5. CHART *-*-*-*-*-*-*-*-*-*-*
        chart = self.creador_chart(bseries = barSeries, nameaxis = nameAxis, valueaxis = valueAxis,
                                   titulo = dato_titulo, titulo_down=dato_titulo_down, titulo_left=dato_titulo_left)

        # 6. CHARTVIEW *-*-*-*-*-*-*-*-*-*-*
        chartView = QtCharts.QChartView(chart)

        'utilizar solo si hay objetos circulares'
        #chartView.setRenderHint(QPainter.Antialiasing)
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
            chartView.chart().axisX().setLabelsBrush(QColor("white")) # valor derecho
            chartView.chart().axisY().setLabelsBrush(QColor("white")) # valor inferior
            chartView.chart().legend().setLabelColor(QColor("white")) # etiquetas

            chartView.chart().axisX().setGridLineColor(QColor("white")) # grid horizontal
            chartView.chart().axisY().setGridLineColor(QColor("white")) # grid vertical

            chartView.chart().axisX().setTitleBrush(QColor("white")) # color titulo down
            chartView.chart().axisY().setTitleBrush(QColor("white")) # color titulo left

            # personalizacion de fondo /-/-/-/
            chartView.chart().setBackgroundVisible(False) # quitar color
            chartView.setBackgroundBrush(QColor("#141f24")) # asignar color



        # 7. CONFIGURACIONES *-*-*-*-*-*-*-*-*-*-*

        # vista grids /-/-/-/
        chartView.chart().axisX().setGridLineVisible(True) # vista grid horizontal
        chartView.chart().axisY().setGridLineVisible(True) # vista grid horizontal

        # leyenda /-/-/-/
        'MarkerShapeDefault | MarkerShapeRectangle | MarkerShapeCircle | MarkerShapeFromSeries'
        chartView.chart().legend().setMarkerShape(QtCharts.QLegend.MarkerShapeRectangle)

        # tamaño de letra /-/-/-/
        chartView.chart().setTitleFont(self.font_size(25)) # titulo
        chartView.chart().axisX().setLabelsFont(self.font_size(12)) # dato down
        chartView.chart().axisY().setLabelsFont(self.font_size(12)) # dato left
        chartView.chart().legend().setFont(self.font_size(12)) # leyenda
        chartView.chart().axisX().setTitleFont(self.font_size(15)) # titulo down
        chartView.chart().axisY().setTitleFont(self.font_size(15)) # titulo left
        
        # fondo /-/-/-/
        chartView.chart().layout().setContentsMargins(0, 0, 0, 0) # quitar margenes
        chartView.chart().setBackgroundRoundness(0) # quitar bordes

        # 8. RESTABLECER WIDGETS *-*-*-*-*-*-*-*-*-*-*
        'limpiar todos los elementos del widget'
        for i in reversed(range(parentgrid.count())): 
            parentgrid.itemAt(i).widget().deleteLater()
        
        # 9. INSERTAR GRAFICO *-*-*-*-*-*-*-*-*-*-*
        parentgrid.addWidget(chartView, 0, 0)

    def font_size(self, size):
        """cambiar tamaño de letra"""
        font = QFont()
        font.setPointSize(size)

        return font

    # 1. BARSET +-+-+
    def creador_barset(self,titulo, datos, color=None):

        barra = QtCharts.QBarSet(titulo) # titulo
        barra.append(datos) # datos
        if not(color is None):
            barra.setColor(color) # color leyenda
            barra.setLabelColor("white") # color valor
            barra.setLabelFont(self.font_size(13)) # tamaño letra 

        return barra

    # 2. BARSERIES +-+-+
    def creador_barseries(self, listaelementos, rotacion=0, formato = "@value"):

        barraseries = QtCharts.QBarSeries()
        for item in listaelementos: # agrega los datos
            barraseries.append(item)
        barraseries.setLabelsVisible(True)
        barraseries.setLabelsFormat(formato)
        barraseries.setLabelsAngle(rotacion)

        # Posicionamiento del "label" valor /-/-/-/
        'LabelsCenter | LabelsOutsideEnd | LabelsInsideEnd | LabelsInsideBase'
        barraseries.setLabelsPosition(QtCharts.QAbstractBarSeries.LabelsOutsideEnd)

        return barraseries

    # 3. NAMEAXIS +-+-+
    def creador_nameaxis(self, listanombres):

        nameAxis = QtCharts.QBarCategoryAxis()
        nameAxis.append(listanombres)

        # cantida de casos a mostrar /-/-/-/
        nameAxis.setRange(listanombres[0], listanombres[-1])

        return nameAxis

    # 4. VALUEAXIS +-+-+
    def creador_valueaxis(self, formato, valormax):

        valueAxis = QtCharts.QValueAxis()
        # formato vista de valor /-/-/-/
        '%.2f (flotante 2 decimales) | %i (entero)'
        valueAxis.setLabelFormat(formato) 

        # uso del valor maximo /-/-/-/
        'al valor maximo por defecto le sumamos 10 esto para que'
        'no este pegado a la parte superior del grafico'
        valueAxis.setRange(0, valormax+50)

        valueAxis.setTickCount(10) # salto en cantidades
        valueAxis.applyNiceNumbers()

        return valueAxis

    # 5. CHART +-+-+
    def creador_chart(self, bseries, nameaxis, valueaxis, titulo, titulo_down=None, titulo_left=None):
        
        chart = QtCharts.QChart()
        chart.setMargins(QMargins(15, 15, 15, 15)) # margenes del graficos
        chart.setTitle(titulo)
        chart.addSeries(bseries)
        chart.setAxisX(nameaxis, bseries)
        chart.setAxisY(valueaxis, bseries)
        chart.legend().setVisible(True)

        # Alieamiento de las etiquetas /-/-/-/
        'AlignTop | AlignBottom | AlignLeft | AlignRight'
        chart.legend().setAlignment(Qt.AlignTop)

        # asignar titulos x y
        chart.axisX().setTitleText(titulo_down)
        chart.axisY().setTitleText(titulo_left)

        # animaciones /-/-/-/
        'NoAnimation | SeriesAnimations | AllAnimations | GridAxisAnimations'
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        return chart


