import java.util.List;

public class BuscaBinaria {
    public static void main(String[] args) {
        List<Integer> listaNumeros = List.of(1, 3, 5, 7, 9, 11, 13, 15, 17, 19);
        Integer item = 12;
        Integer resultado = buscaBinaria(listaNumeros, item);

        if (resultado != null) {
            System.out.println("Elemento encontrado no índice: " + resultado);
        } else {
            System.out.println("Elemento não encontrado na lista.");
        }
    }


    public static Integer buscaBinaria(List<Integer> listaNumeros, Integer item) {
        int baixo = 0;
        int alto = listaNumeros.size() - 1;

        while (baixo <= alto) {
            int meio = (baixo + alto) / 2;
            int chute = listaNumeros.get(meio);

            if (chute == item) {
                return meio;
            }

            if (chute > item) {
                alto = meio -1;
            }
            else {
            baixo = meio + 1;
            }
        }
        return null;
    }
}
