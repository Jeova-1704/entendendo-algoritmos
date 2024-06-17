public class Fatorial {
    public static void main(String[] args) {
        System.out.println(fatorial(5));
        System.out.println(fatorialRecursivo(5));
    }

    public static int fatorial(int n) {
        int fact = 1; // O(1)
        for (int i=1; i<=n; i++) { // O(n + 1)
            fact *= i; // O(n)
        }
        return fact; // O(1)
    }

    public static int fatorialRecursivo(int n) {
        if (n == 0) {
            return 1;
        }
        return n * fatorial(n-1);
    }

}
// analise em forma de equação de recorrencia
// T(1) = 1
// T(n) = 1 + T(n-1)
