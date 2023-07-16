#Una lista bidimensionale/matrice ha come elementi altre liste

matrice=[[0,1,2,3,4],
        [5,6,7,8,9],
        [10,11,12,13,14],
        [15,16,17,18,19]]
print(matrice)

RIGHE=4
COLONNE=5
#SCORRERE UNA MATRICE
for i in range (RIGHE):
    for j in range (COLONNE):
        print(matrice[i][j] , end=' ')
