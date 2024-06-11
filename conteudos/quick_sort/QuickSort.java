package quick_sort;

public class QuickSort {
    public static void main(String[] args) {
        int[] numeros = {8, 5, 9, 1, 3 ,2, 7, 4, 6, 0};
        System.out.print("Array desordenado: ");
        printArray(numeros);
        sortedQuick(numeros, 0, numeros.length - 1);
        System.out.print("Array ordenado: ");
        printArray(numeros);
    }

    private static void printArray(int[] arr) {
        for (int i : arr) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    private static int particionar(int[] numeros, int posicaoI, int posicaoF) {
        int pivo = numeros[posicaoF];
        int i = (posicaoI - 1);
        
        for(int j=posicaoI; j<=posicaoF; j++) {
            if(numeros[j] < pivo) {
                i ++;
                int temp = numeros[i];
                numeros[i] = numeros[j];
                numeros[j] = temp;
            }
        }
        int temp = numeros[i+1];
        numeros[i+1] = numeros[posicaoF];
        numeros[posicaoF] = temp;
        return (i+1);
    }

    private static void sortedQuick(int[] numeros, int posicaoI, int posicaoF) {
        if (posicaoI < posicaoF) {
            int posicaoPivot = particionar(numeros, posicaoI, posicaoF);
            sortedQuick(numeros, posicaoI, posicaoPivot - 1);
            sortedQuick(numeros, posicaoPivot + 1, posicaoF);
        }
    }
}