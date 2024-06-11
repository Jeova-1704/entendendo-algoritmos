package heap_sort;

import java.util.ArrayList;
import java.util.Arrays;

public class HeapSort {
    public static void main(String[] args) {
        ArrayList<Integer> numeros = new ArrayList<>();
        numeros.addAll(Arrays.asList(8, 5, 9, 1, 3 ,2, 7, 4, 6, 0));
        System.out.println("Array desordenado: " + numeros);
        sortedHeap(numeros);
        System.out.println("Array ordenado: " + numeros);
    }

    private static void sortedHeap(ArrayList<Integer> numeros) {
        int tam = numeros.size();

        for (int i = tam / 2 - 1; i >= 0; i--) {
            heapify(numeros, tam, i);
        }

        for(int i=tam-1; i>0; i--) {
            int temp = numeros.get(0);
            numeros.set(0, numeros.get(i));
            numeros.set(i, temp);
            heapify(numeros, i, 0);
        }
    }

    private static void heapify(ArrayList<Integer> numeros, int tam, int i) {
        int largest = i;
        int l = 2 * i + 1;
        int r = 2 * i + 2;

        if(l < tam && numeros.get(i) < numeros.get(l)) {
            largest = l;
        }

        if(r < tam && numeros.get(largest) < numeros.get(r)) {
            largest = r;
        }

        if(largest != i) {
            int temp = numeros.get(i);
            numeros.set(i, numeros.get(largest));
            numeros.set(largest, temp);
            heapify(numeros, tam, largest);
        }
    }

}
