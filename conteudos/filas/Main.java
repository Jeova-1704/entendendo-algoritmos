public class Main {
    public static void main(String[] args) {
        testAdicionaERemove();
        testIsEmpty();
        testTamanho();
        testPrimeiroElemento();
        testVerificaPresenca();
        testCopia();
        testClear();
        System.out.println("Passou em tudo");
    }

    public static void testAdicionaERemove() {
        Fila fila = new Fila();
        fila.adiciona(1);
        fila.adiciona(2);
        fila.adiciona(3);
        
        assert fila.remove().equals(1);
        assert fila.remove().equals(2);
        assert fila.remove().equals(3);
    }

    public static void testIsEmpty() {
        Fila fila = new Fila();
        assert fila.isEmpty();

        fila.adiciona(1);
        assert !fila.isEmpty();
    }

    public static void testTamanho() {
        Fila fila = new Fila();
        assert fila.tamanho() == 0;

        fila.adiciona(1);
        fila.adiciona(2);
        fila.adiciona(3);
        assert fila.tamanho() == 3;
    }

    public static void testPrimeiroElemento() {
        Fila fila = new Fila();
        fila.adiciona(1);
        fila.adiciona(2);
        fila.adiciona(3);

        assert fila.primeiroElemento().equals(1);
    }

    public static void testVerificaPresenca() {
        Fila fila = new Fila();
        fila.adiciona(1);
        fila.adiciona(2);
        fila.adiciona(3);

        assert fila.verificaPresenca(2);
        assert !fila.verificaPresenca(4);
    }

    public static void testCopia() {
        Fila fila = new Fila();
        fila.adiciona(1);
        fila.adiciona(2);
        fila.adiciona(3);

        Fila copiaFila = new Fila();
        copiaFila.adiciona(1);
        copiaFila.adiciona(2);
        copiaFila.adiciona(3);

        assert fila.copia().equals(copiaFila.copia());
    }

    public static void testClear() {
        Fila fila = new Fila();
        fila.adiciona(1);
        fila.adiciona(2);
        fila.adiciona(3);

        fila.clear();
        assert fila.isEmpty();
    }
}
