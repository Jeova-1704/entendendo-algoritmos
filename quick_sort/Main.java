package quick_sort;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> listaNumeros = new ArrayList<>();
        listaNumeros.add(3);
        listaNumeros.add(5);
        listaNumeros.add(2);
        listaNumeros.add(1);
        listaNumeros.add(0);
        listaNumeros.add(4);
        listaNumeros.add(7);
        listaNumeros.add(9);
        listaNumeros.add(8);
        listaNumeros.add(6);

        System.out.println(ordenar(listaNumeros));
        
    }

    public static ArrayList<Integer> ordenar(ArrayList<Integer> arr) {
        if (arr.size() < 2) {
            return arr;
        } else {
            int meio = arr.size() / 2;
            int pivo = arr.get(meio);
            ArrayList<Integer> menores = new ArrayList<>();
            ArrayList<Integer> iguais = new ArrayList<>();
            ArrayList<Integer> maiores = new ArrayList<>();

            for (Integer i : arr) {
                if (i < pivo) {
                    menores.add(i);
                } else if (i == pivo) {
                    iguais.add(i);
                } else {
                    maiores.add(i);
                }
            }

            ArrayList<Integer> resultados = new ArrayList<>();
            resultados.addAll(ordenar(menores));
            resultados.addAll(iguais);
            resultados.addAll(ordenar(maiores));

            return resultados;
        }
    }
}
