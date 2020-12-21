import heapq
contador = 6
n, m = input().split()  # Pedir ao usuario o numero de vertices e arestas
n = int(n)
m = int(m)
n_out = [[] * n for i in range(n)]  # inicializar as listas de adjecencia
custo = []  # inicializar a matriz de pesos(custo de transitação entre um vertice e outro)

# Começar a preencher a matriz, inicialmente só é utilizado -1 e 0 pois ainda não foi computado os pesos entre os vertices

for i in range(n):
    linha = []
    for j in range(n):
        if i == j:
            linha.append(0)
        else:
            linha.append(-1)
    custo.append(linha)

print(
    "Preenchimento da Matriz com valores inicias de 0, quando estiver na diagonal principal e -1 para todos os outros, já que não temos o peso verdadeiro.")
print("")
print(" V0  V1  V2  V3  V4  V5")
for espaço in custo:
    print(espaço)
print("")

# Preenche a matriz de custo com os valores verdadeiros e completa a matriz de adjacencia

infty = 1
for j in range(m):  # Ler todas as arestas do grafo
    a, b, c = input().split()  # Ler o peso C do vertice A ao vertice B
    a = int(a)
    b = int(b)
    c = int(c)
    n_out[a].append(b)  # B vai ser vizinho de A, já que ele possui uma conexão
    custo[a][b] = c
    infty = infty + c

print("")
print("Matriz de Pesos com os dados atualizados, onde tem -1 significa que o caminho é inviavel")
print("")

for espaço in custo:
    print(espaço)
print("")

# No algoritmo de Dijkastra é necessario que os vertices sejam marcados, precisa da escolha de uma raiz em que o tamanho até ela seja 0 e para todas as outras é necessario que seja infinito, as linhas de codigo abaixo servem para isso

marca = n * [0]  # Deixa todos os vertices desmarcados
L = n * [infty]  # Atribui para todos os vertices o valor de distancia "infinito"
L[0] = 0  # Para o vertice raiz é dado a distancia como 0 para poder inicializar o algoritmo
D = [(0, 0)]  # A raiz entra na nossa fila de prioridade
for w in range(1, n):  # Guardar todas as posições em nossa fila de prioridade
    heapq.heappush(D, (L[w], w))
pai = n * [-1]  # Assim como no algoritmo de Dijkastra, em codigo, inicialmente, todos os pais serão indefinidos em -1

print("")
print(
    "Assim como no algoritmo mostrado nos slides, inicialmente todos os vertices, com excessão da raiz, terão um peso infinito")
print("")
print(D)
print("")

# Essa parte daqui é um pouco parecida com o proprio pseudocódigo do Dijkastra
print('''Mostra a cada loop os itens da matriz que estão sendo marcadas, bem como, as mudanças de custo que estão tendo para chegar em determinado vertice, no final, vamos ter encontrado o menor caminho para cada situação e todos os vertices estarão marcados'
perceba que a lista de prioridade também está mudando
''')
print("")
print(L)
print("")
while D != []:

    Lmin, v = heapq.heappop(D)  #Retiro o menor valor da fila de prioridade, pego a sua distancia e o vertice no qual está associado
    marca[v] = 1                # Marca o vertice o qual foi pego na linha anterior
    print("V0 V1 V2 V3 V4 V5")
    print(marca)
    print(D)


    for w in n_out[v]:                        #Agora que o vertice foi marcado, devo pegar as adjacências dele
        if marca[w] == 0:                     #Obviamente que só devo fazer isso, caso ele não esteja marcado
            if L[v] + custo[v][w] < L[w]:     #Agora eu preciso saber se o custo do vertice + o custo do trajeto de V para o adjacencia é menor do o custo atual dele
                for i in range(len(D)):
                    if D[i] == (L[w], w):
                        pos = i
                        break
                L[w] = L[v] + custo[v][w]    #Se for menor, vou atualizar o custo atual dele
                D[pos] = (L[w], w)
                heapq._siftdown(D, 0, pos)   #atualizar a lista de prioridade
                pai[w] = v
    print(L)
    print("")


print("")