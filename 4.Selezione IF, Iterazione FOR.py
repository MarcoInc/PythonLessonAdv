#SELEZIONE
num=int(input("inserisci un numero\n"))
if num==5:
    print("uguale a 5")
elif num!=5:
    print("diverso da 5")
    if 5<num: 
        print("più grande di 5")

    elif num==0:
        print("uguale a 0")
    else: 
        print("più piccolo di 0")
if(num<5 or num>10):
    print('il numero non è compreso tra 5 e 10')
else:
    print('il numero è compreso tra 5 e 10')
print("")

#ITERAZIONE

print("while")
count=1
while(count<=num): #pre-test loop
    print(count)
    count+=1
print("for in")
for numero in [10,50,2]: #scorre un elemento numerabile
    print(numero) #stampa il singolo elemento
print("for in range")
for i in range(50): #conta i viene incrementatato da 0 a 50)
    print(i)

print("for in rage 3 argomenti")
for j in range(1,10,2): #da 1 a 10 ad incrementi di 2
    print(j)
print('oppure')
for j in range(1,100,5): #da 1 a 100 ad incrementi di 5
    print(j) #stampa 20 numeri
print("for in rage 3 argomenti decremento")
for m in range(1,-10,-1): #da 1 a -10 ad decrementi di 1
    print(m)


    
