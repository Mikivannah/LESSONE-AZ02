#ВЫБРОСЫ

import pandas as pd
import matplotlib.pyplot as plt
data = {'value':[1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}

df = pd.DataFrame(data)
print(df)
# создадим график
df['value'].hist()
plt.show()

# создадим гистограмму
df['value'].plot(kind='hist')
plt.show()

# Другой вариант визуализации данных Раскомментируем график boxplot, который отображает основные
# статистические характеристики набора данных:
df.boxplot(column='value')
plt.show()

print(df.describe())

#2. Далее определим первый (Q1) и третий (Q3) квартили, используя функцию quantile():
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)

#3. Теперь рассчитаем межквартальный размах (IQR), для этого пропишем:
IQR = Q3 - Q1

#4. Теперь рассчитаем верхнюю и нижнюю границы интервала:
downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

#5  А теперь необходимо удалить выбросы, которые не входят в очерченный диапазон. Создадим новый датафрейм:
df = df[(df['value'] >= downside) & (df['value'] <= upside)]

#6 для визуальной оценки нового набора данных создадим график boxplot:
df.boxplot(column='value')
plt.show()




