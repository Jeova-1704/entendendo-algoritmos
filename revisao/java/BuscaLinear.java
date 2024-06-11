import java.util.ArrayList;
import java.util.List;

public class BuscaLinear {
    public static void main(String[] args) {
        List<Integer> numeros = new ArrayList<>();
        numeros.add(1);
        numeros.add(2);
        numeros.add(3);
        numeros.add(4);
        numeros.add(5);
        System.out.println(buscaLinear(numeros, 5));
    }

    public static int buscaLinear(List<Integer> numeros, Integer n) {
        int a = numeros.size() - 1;
        for (int i = 0; i <= a; i++) {
            if (numeros.get(i).equals(n)) {
                return i;
            }
        }
        return -1;
    }
}
