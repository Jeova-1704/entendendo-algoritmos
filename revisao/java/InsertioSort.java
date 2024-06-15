public class InsertioSort {
    public static void main(String[] args) {
        int[] numeros = new int[5];
        numeros[0] = 5;
        numeros[1] = 4;
        numeros[2] = 3;
        numeros[3] = 2;
        numeros[4] = 1;
        for (int i : numeros) {
            System.out.println(i);
        }
        System.out.println("============");
        insertionSort(numeros);
        System.out.println("============");
        for (int i : numeros) {
            System.out.println(i);
        }
    
    }

    public static void insertionSort(int[] arr) {
        int n = arr.length;
    
        for (int i = 1; i < n; i++) {
            int chave = arr[i];
            int j = i - 1;
    
            while (j >= 0 && chave < arr[j]) {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = chave;
        }
    }

}
