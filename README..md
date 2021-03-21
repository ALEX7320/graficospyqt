# Gráficos de Barras y Pie PySide2 [PyQt]

**Indice**

  * [Recursos utilizados](#recursos-utilizados)
  * [Estructura](#estructura)
	* [Gráfico de Barras](#gráfico-de-barras)
	* [Gráfico Pie](#gráfico-pie)
  * [Parámetros](#parámetros)
  * [Personalización](#fuentes)
 	* [Metodos](#metodos)
 	* [Muestra](#muestra)
  * [Estilos](#fuentes)
 	* [Gráfico - En general](#gráfico---En-general)
 	* [Gráfico - Barras](#gráfico---barras)
 	* [Gráficos - Pie](#gráficos---pie)
  * [Agregar gráfico](#agregar-gráfico)
  * [Optimización](#optimización)
  * [Otros gráficos](#otros-gráficos)
  * [Fuentes](#fuentes)
  * [Previzualización](#previzualización)

# Recursos utilizados

`pip install PySide2`

# Estructura

### Gráfico de Barras

Estructura de creación:

1. QBarSet
2. QBarSeries
3. QBarCategoryAxis
4. QValueAxis
5. QChart
6. QChartView

### Gráfico Pie

Estructura de creación:

1. QPieSlice
2. QPieSeries
3. QChart
4. QChartView

# Parámetros

 * Parentgrid: QGridLayout para ubicar el el gráfico generado
 * teme 1: predeterminado | teme 2: personalizado

```python
def __init__(self, parentgrid, theme=1):
```

# Personalización

### Metodos

En todos estos parametros es en donde se customiza el grafico.

- setTitleBrush
- setLabelColor
- setGridLineColor
- setGridLineVisible
- setBackgroundVisible
- setMarkerShape
- setTitleFont
- setFont
- setContentsMargins
- setBackgroundRoundness

### Muestra

Estos se encuentra de manera directa en el `else` de Personalizado, en aqui podras realizar dichos cambios.

**Grafico de Barras**

```python
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

```

**Grafico Pie**

```python
# definir color de letras /-/-/-/
chartView.chart().setTitleBrush(QColor("white")) # titulo
chartView.chart().legend().setLabelColor(QColor("white")) # etiquetas

# personalizacion de fondo /-/-/-/
chartView.chart().setBackgroundVisible(False) # quitar color
chartView.setBackgroundBrush(QColor("#141f24")) # asignar color
```

# Estilos

### Gráfico - En general

| Temas - Gráficos |
| :------------ |
|QtCharts.QChart.ChartThemeLight|
|QtCharts.QChart.ChartThemeBlueCerulean|
|QtCharts.QChart.ChartThemeDark|
|QtCharts.QChart.ChartThemeBrownSand|
|QtCharts.QChart.ChartThemeBlueNcs|
|QtCharts.QChart.ChartThemeHighContrast|
|QtCharts.QChart.ChartThemeBlueIcy|
|QtCharts.QChart.ChartThemeQt|

| Temas - Leyenda |
| :------------ |
|QtCharts.QLegend.MarkerShapeDefault|
|QtCharts.QLegend.MarkerShapeRectangle|
|QtCharts.QLegend.MarkerShapeCircle|
|QtCharts.QLegend.MarkerShapeFromSeries|

| Animaciones - Gráficos |
| :------------ |
|QtCharts.QChart.NoAnimation|
|QtCharts.QChart.SeriesAnimations|
|QtCharts.QChart.AllAnimations|
|QtCharts.QChart.GridAxisAnimations|


###  Gráfico - Barras

| Ubicación - Etiquetas |
| :------------ |
|QtCharts.QAbstractBarSeries.LabelsCenter|
|QtCharts.QAbstractBarSeries.LabelsOutsideEnd|
|QtCharts.QAbstractBarSeries.LabelsInsideEnd|
|QtCharts.QAbstractBarSeries.LabelsInsideBase|

### Gráficos - Pie

| Ubicación - Etiquetas |
| :------------ |
|QtCharts.QPieSlice.LabelOutside|
|QtCharts.QPieSlice.LabelInsideHorizontal|
|QtCharts.QPieSlice.LabelInsideTangential|
|QtCharts.QPieSlice.LabelInsideNormal|

# Agregar gráfico

Simplemente lo agregamos el `chartView` a nuesto `QGridLayout`

```python
parentgrid.addWidget(chartView, 0, 0)
```

# Optimización

Para ello debemos tener en cuenta que cada vez que se agrega un widget, este se posiciona encima del otro. 

Para evitar ese caso, debemos remover todos los widgets que se encuentren en el `QGridLayout` y posteriormente agregarlo (esto ya viene integrado en el script).

```python
# 7. RESTABLECER WIDGETS *-*-*-*-*-*-*-*-*-*-*
for i in reversed(range(parentgrid.count())): 
    parentgrid.itemAt(i).widget().deleteLater()
```

# Otros gráficos

No solo existen unicamenten estos dos gráficos; sin embargo son los más usados, pero si deseas adentrarte mas en este tema en [Qter](https://www.qter.org/portal.php?mod=view&aid=6802 "Qter") podras ver otros tipos con su respectivo script.

# Fuentes

- [AndresNiño (Bar Chart)](https://github.com/andresnino/PyQt5/tree/master/Grafico%20de%20barras%20-%20Bar%20Chart "AndresNiño (Bar Chart)")
- [AndresNiño (Pie Chart)](https://github.com/andresnino/PyQt5/tree/master/Grafico%20circular%20-%20Pie%20Chart "AndresNiño (Pie Chart)")
- [ProgrammerSought](https://www..com/article/26606027024/ "ProgrammerSought")
- [StackOverflow](https://stackoverflow.com/questions/59884038/how-do-i-get-the-axis-labels-in-qtchart-qlineseries "StackOverflow")
- [SemiColonWorld](https://www.semicolonworld.com/question/58072/clear-all-widgets-in-a-layout-in-pyqt "SemiColonWorld")
- [Qter](https://www.qter.org/portal.php?mod=view&aid=6802 "Qter")


# Previzualización

**Gráfico de Barras**

![](https://1.bp.blogspot.com/-sHgEFQZheg0/YFau8KheFrI/AAAAAAAAAH8/q-qC0lALGM8BycmZqsjgX5T3aiK5JAS1QCLcBGAsYHQ/s1600/32146124.jpg)


**Gráfico Pie**

![](https://1.bp.blogspot.com/-K3dKxqjDifo/YFau8DgCSQI/AAAAAAAAAH4/hc_pD1xuiWI9o64GAnizbFbdWDU-bZGVgCLcBGAsYHQ/s1600/14561421.jpg)