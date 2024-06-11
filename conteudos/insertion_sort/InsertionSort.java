package insertion_sort;

import java.util.ArrayList;
import java.util.Arrays;

public class InsertionSort {
    public static void main(String[] args) {    
        Integer[] numerosArray = {5, 3, 8, 6, 2, 7};
        ArrayList<Integer> numeros = new ArrayList<>(Arrays.asList(numerosArray));

        sorted(numeros);

        System.out.println(numeros.toString());

    }

    private static void sorted(ArrayList<Integer> numeros) {
        int tamanho = numeros.size();

        for(int i=0; i<tamanho; i++) {
            int chave = numeros.get(i);
            int j = i -1;

            while (j >= 0 && numeros.get(j) > chave) {
                numeros.set(j+1, numeros.get(j));
                j--;
            }
            numeros.set(j+1, chave);
        }
    }
}
