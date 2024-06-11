public class BuscaBinaria2 {
    public static void main(String[] args) {
        int[] vetor = {1, 2, 3, 4, 5, 6, 7, 8, 9};
        int chave = 5;
        int posicao = buscabinaria(vetor, chave);
        if (posicao != -1) {
            System.out.println("Elemento encontrado na posição: " + posicao);
        } else {
            System.out.println("Elemento não encontrado");
        }
    }

    public static int buscabinaria(int[] vetor, int chave) {
        int inicio = 0;
        int fim = vetor.length - 1;
        int meio = 0;
        while (inicio <= fim) {
            meio = (inicio + fim) / 2;
            if (vetor[meio] == chave) {
                return meio;
            } else if (vetor[meio] < chave) {
                inicio = meio + 1;
            } else {
                fim = meio - 1;
            }
        }
        return -1;
    }
}
