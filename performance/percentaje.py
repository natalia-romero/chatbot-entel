import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'serif'
options = ['Correctas', 'Malas']
values = [65.5, 34.5] 
colors = ['cornflowerblue', 'thistle']
plt.pie(values, labels=options, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title('Porcentaje de Respuestas Correctas')
plt.axis('equal')
plt.show()