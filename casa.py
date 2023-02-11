#importação de pacotes
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

#criação de figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Coordenadas da casa
x=[0,0,0,0,3,3,3,3]
y=[0,0,3,3,3,3,0,0]
z=[0,3,3,0,0,3,3,0]

#Desenhando a casa
ax.plot(x,y,z, color='yellow', marker='o', linestyle='dashed')

#Configurando a visualização
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

#Mostrando a figura
plt.show()