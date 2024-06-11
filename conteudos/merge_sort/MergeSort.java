package merge_sort;

import java.util.ArrayList;
import java.util.Arrays;

public class MergeSort {
    public static void main(String[] args) {
        Integer[] numerosArray = {5, 3, 8, 6, 2, 7};
        ArrayList<Integer> numeros = new ArrayList<>(Arrays.asList(numerosArray));

        sorted(numeros, 0, numeros.size());

        System.out.println(numeros.toString());
    }

    private static void sorted(ArrayList<Integer> numeros, int p, int r) {
        if (p >= r) {
        
        } else {
            int q = (p + r) / 2;
            sorted(numeros, p, q);
            sorted(numeros, q+1, r);
            merge(numeros, p, q, r);
        }
    }

    private static void merge(ArrayList<Integer> numeros, int p, int q, int r) {
        int nE = q - p;
        int nD = r - q;
        Integer[] esquerda = new Integer[nE];
        Integer[] direita = new Integer[nD];


        for (int i = 0; i < nE; i++) {
            esquerda[i] = numeros.get(p + i);
        }

        for (int j = 0; j < nD; j++) {
            direita[j] = numeros.get(q + j);
        }

        int i = 0, j = 0, k = p;

        while (i < nE && j < nD) {
            if (esquerda[i] <= direita[j]) {
                numeros.set(k, esquerda[i]);
                i++;
            } else {
                numeros.set(k, direita[j]);
                j++;
            }
            k++;
        }

        while (i < nE) {
            numeros.set(k, esquerda[i]);
            i++;
            k++;
        }

        while (j < nD) {
            numeros.set(k, direita[j]);
            j++;
            k++;
        }
    }
}
