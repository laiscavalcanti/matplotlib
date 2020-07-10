import pandas as pd
import matplotlib.pyplot as plt
import datetime

df = pd.read_csv('monitoramento_tempo.csv')
df['data'] = pd.to_datetime(df['data'])
# print(df)

fig, main_ax = plt.subplots()
main_ax.plot(df['data'], df['temperatura'], color='steelblue')
main_ax.set_xlim(datetime.datetime(2014, 5, 1), datetime.datetime(2014, 6, 1))
main_ax.set_ylim(270, 320)
main_ax.set_xlabel('Data')
plt.xticks(rotation=45)
main_ax.set_ylabel('Temperatura')
main_ax.set_title('Temperatura em maio/2014', pad=20)
main_ax.legend(['Temperatura'], loc='lower right', fontsize=15)

# fig = plt.figure(figsize=(11, 8))

# eixo = fig.add_axes([0, 0, 1, 1])
eixo2 = fig.add_axes([0.7, 0.60, 0.2, 0.2])

# eixo.plot(df['data'], df['temperatura'], color='steelblue')
# eixo.set_xlim(datetime.datetime(2014, 5, 1), datetime.datetime(2014, 6, 1))
# eixo.set_ylim(270, 320)
# eixo.set_title('Temperatura em maio/2014', fontsize=25, pad=20)
# eixo.set_ylabel('Temperatura', fontsize=20)
# eixo.set_xlabel('Data', fontsize=20)
# eixo.legend(['Temperatura'], loc='lower right', fontsize=15)
# eixo.grid(True)

filtro_esquerda = df['data'] < datetime.datetime(2014, 5, 1)
filtro_direita = df['data'] > datetime.datetime(2014, 6, 1)

eixo2.plot(df['data'], df['temperatura'], color='steelblue')
eixo2.plot(df[filtro_esquerda]['data'], df[filtro_esquerda]['temperatura'], color='purple')
eixo2.plot(df[filtro_direita]['data'], df[filtro_direita]['temperatura'], color='purple')
eixo2.set_xlim(datetime.datetime(2014, 1, 1), datetime.datetime(2015, 1, 1))
eixo2.set_title('Temperatura em 2014', fontsize=5, pad=5)
eixo2.set_ylabel('Temperatura', fontsize=5)
eixo2.set_xlabel('Data', fontsize=10)
plt.xticks(rotation=45)
eixo2.legend(['Temperatura'], loc='best', fontsize=5)
eixo2.grid(True)

plt.show()

