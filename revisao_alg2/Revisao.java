public class Revisao {

    public static void main(String[] args) {
        System.out.println(fatorial(0));
        System.out.println(fatorial(1));
        System.out.println(fatorial(2));
        System.out.println(fatorial(3));
        System.out.println(fatorial(4));
        System.out.println(fatorial(5));
    }

    public static int fatorial(int n) {
        if (n == 0) {
            return 1;
        }
        return n * fatorial(n -1);
    }
}
