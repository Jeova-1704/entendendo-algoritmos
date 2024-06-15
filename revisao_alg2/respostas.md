##### 1. Considere uma função que resolve o fatorial de um número, como descrito abaixo:
```java
public int fatorial(int n){ 
  int fact=1; // O(1)
  for(int i = 1; i <= n; i++){ // O(n + 1)
      fact = fact * i; // O(n)
  }
  return fact; // O(1)
 }
```
##### Calcule a complexidade do algoritmo apresentado e forneça a sua classificação de acordo com a notação O.
O(1) + O(n+1) + O(n) + o(1) = O(N)


##### 2. Resolva o mesmo problema de forma recursiva (mostre o código) e faça a análise na forma de equação de recorrência. Detalhe seu raciocínio.

```java
public static int fatorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * fatorial(n -1);
}
```
T(1) = 1
T(n) = 1 + T(n-1)
onde:
    n = 0
    n > =

##### 3.Escreva um algoritmo que, dada uma lista ligada, seja capaz de inverter a lista, isto é, fazer com que os ponteiros apontem na direção contrária, e o último elemento da lista seja, ao fim da execução, a cabeça.
``` python
def inverter(self):
    anterior = None
    atual = self.inicio 
    self.fim = self.incio

    while atual is not None:
        proximo = atual.getProximo()
        atual.setProximo(anterior)
        anterior = atual
        atual = proximo

    self.inicio = anterior
```

##### 4.
um pilha pelo erro de memoria





