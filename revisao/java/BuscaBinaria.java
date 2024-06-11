public class BuscaBinaria {
    public static void main(String[] args) {
        int[] numeros = new int[5];
        numeros[0] = 1; 
        numeros[1] = 2; 
        numeros[2] = 3; 
        numeros[3] = 4; 
        numeros[4] = 5; 
        System.out.println(buscaBinaria(numeros, 3));
    }

    public static int buscaBinaria(int[] arr, int n) {
        int inferior = 0;
        int superior = arr.length - 1;

        while (inferior <= superior) {
            int meio = (superior + inferior) / 2;
            int chute = arr[meio];

            if (chute == n) {
                return meio;
            }
            if (chute < n) {
                inferior = meio + 1;
            }
            if (chute > n) {
                superior = meio - 1;
            }
        }
        return -1;
    }

}
