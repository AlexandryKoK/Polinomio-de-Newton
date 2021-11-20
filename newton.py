import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

n=5

#Lendo os dados do arquivo de entrada
X, Y = [], []
for line in open('entrada.dat', 'r'):
  values = [float(s) for s in line.split()]
  X.append(values[0])
  Y.append(values[1])

#criando uma matriz de zeros
a = np.zeros((n+1, n+1))


#Gravando na primeira(0 no python) linha de a, os dados de X e na segunda(1 no python) linha os dados de Y
for i in range(0,n): 
    a[0][i] = X[i]
for i in range(0,n):
    a[1][i] = Y[i]

#Na terceira(2) linha de a, todos os elementos seguem o algoritmo a seguir:
for i in range(0,n-1): 
    a[2][i] = (a[1][i+1] - a[1][i])/(a[0][i+1] - a[0][i])
    
#Da quarta(3) em diante, o algoritmo se modifica para o seguinte,
#onde temos que ter (4-j+2) para que a quantidade de elementos va diminuindo conforme formos avancando
#no calculo e temos que considerar que estamos comecando de 3.
for j in range(3,n+1):
    for i in range(0,4-j+2):
        a[j][i] = (a[j-1][i+1] - a[j-1][i])/(a[0][j+i-1] - a[0][i])
        
#Imprimindo os valores dos coeficientes da funcao:
for i in range(1,n+1):        
    print('a_%g = %g' % (i,a[i][0]))
print('f(x) = 0.977736 + 0.0733913*x - 0.343047*x**2 + 0.0552928*x**3 + 0.0018251*x**4')

#Criando uma funcao para melhor visualizar e plotar.
def polinomio(x):
    soma = 0
    for j in range(0,n):
        produto = 1
        for i in range(0,j):
            produto = produto * (x-a[0][i])
        soma = soma + a[j+1][0]*produto
        #print(soma)
    return soma

#Salvando em um arquvio de texto os dados encontrados.
#Onde a funcao e determinada por f(x) = a_1 + a_2(x-x_1) + a_3(x-x_1)(x-x_2) + ...,
#e so entao depois desse produto que encontramos uma funcao apresentavel como a que se imprime a seguir.
text_file = open("saida.dat", "w")
for i in range(1,n+1):        
    text_file.write('a_%g = %g\n' % (i,a[i][0]))
text_file.write('f(x) = 0.977736 + 0.0733913*x - 0.343047*x**2 + 0.0552928*x**3 + 0.0018251*x**4')
text_file.close()
print("Dados salvos em 'saida.dat' ")

#Plotando os dados de entrada.
plt.plot(X, Y, 'ro', label='Dados')
x = np.arange(-200., 100., 0.2)
plt.axis([0, 3, -3, 3])
plt.title('Dados de Entrada.')
plt.legend()
plt.show()

#Plotando a funcao encontrada.
x = np.arange(-200., 100., 0.2)
plt.plot(x, polinomio(x),label='Funcao de ajuste')
#se necessario conferir a funcao encontrada:
#plt.plot(x,0.977736 + 0.0733913*x - 0.343047*x**2 + 0.0552928*x**3 + 0.0018251*x**4)
plt.axis([-200, 200, -500, 510])
plt.title('Funcao de Ajuste encontrada.')
plt.legend()
plt.show()

#Plotando a comparacao entre os dois
fig, ax = plt.subplots()
ax.plot(X, Y, 'ro', label='Dados')
x = np.arange(-200., 100., 0.2)
ax.plot(x, polinomio(x),label='Funcao de Ajuste')
plt.axis([-4, 7, -4, 7])
plt.legend()
plt.title('Comparacao - Dados x Funcao de ajuste.')
fig.savefig("comparacao.png")
plt.show()
