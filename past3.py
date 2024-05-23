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

# Другой вариант визуализации данных
df.boxplot(column='value')
plt.show()

print(df.describe())

