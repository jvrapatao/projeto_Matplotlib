from matplotlib import pylab as plt

x = ['Python', 'C#', 'Java', 'C++', 'JavaScript']
y = [10, 2, 3, 4, 5]

plt.bar(x, y, align='center', alpha=0.5)
plt.title('Bar Chart', fontdict={
          'family': 'monospace', 'color': 'red',
          'weight': 'bold', 'size': '16'}, loc='center')

plt.xlabel('Linguagens de programação', labelpad=5)
plt.ylabel('Pontuações', labelpad=5)

plt.show()
