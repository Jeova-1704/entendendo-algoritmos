def fiboR(valor):
    if valor <= 0:
        return 0
    if valor == 1:
        return 1
    else:
        return (fiboR(valor - 1) + fiboR(valor - 2))
    
    
def fibo(valor):
    if valor <= 0:
        return 0
    if valor == 1:
        return 1
    else:
        t1 = 0 
        t2 = 1 
        for x in range(1, valor):
            t3 = t1 + t2
            
            t1 = t2
            t2 = t3
        return t3

#  0 1 1 2 3 5 8 13 21 34 55

print (fiboR(6))

print (fibo(3)) 