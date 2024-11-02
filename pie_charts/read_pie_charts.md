# Вы находитесь в директории содержащей 3 модуля для построения Круговых диаграмм с использованием библиотек Matplotlib, Seaborn и Plotly
## Для построения круговых диаграмм использован файл data_mun_demography_123_v20240612.csv.csv содержащий общие сведения о численности населения РФ, показателях рождаемости, смертности и миграции:
![image](https://github.com/user-attachments/assets/9ea41871-c46b-443c-85fe-197fce78ff95)
## для всех графиков создан датафрейм df = pd.read_csv('data_mun_demography_123_v20240612.csv', sep=';', )
## и переменные со значениями столбцов, - a = df['year'], b = df['population'], c = df['deaths'], d = df['births'], e = df['migration']
## Для фиксации времени задействован модуль time
# Matplotlib
### импортированы библиотеки matplotlib.pyplot, pandas, time. 
### Создание каркаса фигуры plt.subplots(figsize=(8, 5.5), )
### для построения диаграммы использована функция df[df.columns[1:]].sum().plot.pie () с параметрами сдвигов, цветов, значений
## [посмотреть код Matplotlib](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/pie_charts/pie_chart_PLT.py)____>>>>____[посмотреть реузльтат](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/graphics/Круговая%20диаграмма%20PLT.png)

___________________________________________________________________________________________________________________________________________________________________________________________________________
# Seaborn
### импортированы библиотеки matplotlib.pyplot, pandas, seaborn, time. 
### график создается с использованием функции plt.pie () с параметрами, в качестве основного аргумента data
## [посмотреть код Seaborn](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/pie_charts/pie_chart_SNS.py)____>>>>____[посмотреть реузльтат](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/graphics/Круговая%20диаграмма%20SNS.png)

___________________________________________________________________________________________________________________________________________________________________________________________________________
# Plotly
### импортированы библиотеки plotly.graph_objs, pandas, time. 
### Создание фигуры с использованием функции fig = go.Figure()
### для установки параметров fig.add_trace(go.Pie())
## [посмотреть код Plotly](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/pie_charts/pie_chart_PX.py)____>>>>____[посмотреть реузльтат](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/graphics/Кольцевая%20диаграмма%20РХ.png)




