# Вы находитесь в директории содержащей 3 модуля для построения Столбчатых диаграмм с использованием библиотек Matplotlib, Seaborn и Plotly
## Для построения столбчатых диаграмм использован файл data_mun_demography_123_v20240612.csv.csv содержащий общие сведения о численности населения РФ, показателях рождаемости, смертности и миграции:
![image](https://github.com/user-attachments/assets/9ea41871-c46b-443c-85fe-197fce78ff95)
## для всех графиков создан датафрейм df = pd.read_csv('data_mun_demography_123_v20240612.csv', sep=';', )
## и переменные со значениями столбцов, - a = df['year'], b = df['population'], c = df['deaths'], d = df['births'], e = df['migration']
## Для фиксации времени задействован модуль time
# Matplotlib
### импортированы библиотеки matplotlib.pyplot, pandas, time. 
### Создание каркаса фигуры plt.figure(figsize=(8, 5.5), )
### для передачи координат по осям использована функция plt.bar
### Так же добавлены названия осей и графика
## [посмотреть код Matplotlib](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/bar_graphs/bar_graphs_PLT.py)____>>>>____[посмотреть реузльтат](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/graphics/Столбчатая%20диаграмма%20PLT.png)
![image](https://github.com/user-attachments/assets/7e033c56-6990-4add-81d2-906536edcd54)

___________________________________________________________________________________________________________________________________________________________________________________________________________
# Seaborn
### импортированы библиотеки matplotlib.pyplot, pandas, time. 
### Создание каркаса фигуры sb = sns.barplot(data=df, x="year", y="deaths",)
### для передачи координат по осям использована функция sns.barplot
### Так же добавлены названия осей и графика
## [посмотреть код Seaborn](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/bar_graphs/bar_graphs_SNS.py)____>>>>____[посмотреть реузльтат](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/graphics/Столбчатая%20диаграмма%20SNS.png)
![image](https://github.com/user-attachments/assets/1b9e4247-9a69-4e39-82b2-ad6aab93ce2e)

___________________________________________________________________________________________________________________________________________________________________________________________________________
# Plotly
### импортированы библиотеки plotly.express, pandas, time. 
### Создание фигуры с параметрами fig = px.bar(df, x=a, y=[c, d, e], template="simple_white",)
### для передачи Названия графика, названий осей использован метод fig.update_layout
## [посмотреть код Plotly](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/bar_graphs/bar_graphs_PX.py)____>>>>____[посмотреть реузльтат](https://github.com/AlexandrKuznetsov1/DegreeProject/blob/master/graphics/Столбчатая%20диаграмма%20PX.png)
![image](https://github.com/user-attachments/assets/3c0c54ea-0395-4b66-be34-c5140560c20c)
