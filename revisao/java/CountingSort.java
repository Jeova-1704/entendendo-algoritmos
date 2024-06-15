import java.util.Arrays;

public class CountingSort {
    public static void main(String[] args) {
        int[] vetor = new int[]{1, 5, 2, 76, 4, 7, 23, 0, 9, 2, 3, 5, 5};
        int[] ordenado = countingsort(vetor);
        for (int i : ordenado) {
            System.out.println(i);
        }
    }

    public static int[] countingsort(int[] entrada) {
        int tamanho = entrada.length;
        int maiorElemento = Arrays.stream(entrada).max().getAsInt();
        int[] ordenado = new int[tamanho];
        int[] contagem = new int[maiorElemento + 1];

        for (int i = 0; i < tamanho; i++) {
            contagem[entrada[i]]++;
        }

        for (int i = 1; i <= maiorElemento; i++) {
            contagem[i] += contagem[i - 1];
        }

        for (int j = tamanho - 1; j >= 0; j--) {
            ordenado[contagem[entrada[j]] - 1] = entrada[j];
            contagem[entrada[j]]--;
        }

        return ordenado;
    }
}
