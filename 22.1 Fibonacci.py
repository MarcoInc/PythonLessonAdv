# Fib(0)=1
# Fib(1)=1
# Fib(n)=Fib(n-1)+Fib(n-2)

[0 , 1 , 1 , 2 , 3 , 5 , 8 , 13]
def main():
    n=0
    while n<2:
        n = int(input("Inserire il valore di n per la formula di Fibonacci: (n>=2) "))
    fib = [0]*(n+1)
    fib[1] = 1

    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    
    print(fib)
    #[0 , 1 , 1 , 2 , 3 , 5 , 8 , 13.....]

main()