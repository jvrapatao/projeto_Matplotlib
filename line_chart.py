from matplotlib import pyplot as plt


x = [1, 2, 3]
y = [1, 2, 3]

plt.title('Título esquerda', fontdict={
          'family': 'serif', 'color': 'darkblue',
          'weight': 'bold', 'size': '16'}, loc='left')

plt.title('Título central', fontdict={
          'family': 'monospace', 'color': 'red',
          'weight': 'bold', 'size': '16'}, loc='center')

plt.title('Título direita', fontdict={
          'family': 'fantasy', 'color': 'black',
          'weight': 'bold', 'size': '16'}, loc='right')

plt.xlabel('Valores do eixo X', family='serif',
           color='c', weight='normal', size=13, labelpad=6)
plt.ylabel('Valores do eixo Y', family='serif',
           color='c', weight='normal', size=13, labelpad=6)

# Alterando a cor e modeo da linha do grafíco
plt.plot(x, y, ':', color='g', lw=2)
# plt.title('Gráfico em python')


plt.show()
