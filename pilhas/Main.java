package pilhas;

public class Main {
    public static void main(String[] args) {
        testAdicionar();
        testPop();
        testPeek();
        testIsEmpty();
        testSize();
    }

    public static void testAdicionar() {
        System.out.println("Testando adicionar elementos à pilha:");

        Pilha<Integer> pilha = new Pilha<>();
        pilha.adicionar(10);
        pilha.adicionar(20);
        pilha.adicionar(30);

        System.out.println("Pilha após adicionar elementos: " + pilha);
        System.out.println();
    }

    public static void testPop() {
        System.out.println("Testando remover elementos da pilha:");

        Pilha<Integer> pilha = new Pilha<>();
        pilha.adicionar(10);
        pilha.adicionar(20);
        pilha.adicionar(30);

        System.out.println(pilha);

        pilha.pop();

        System.out.println("Pilha após remover elemento do topo: " + pilha);
        System.out.println();
    }

    public static void testPeek() {
        System.out.println("Testando peek() para visualizar o topo da pilha:");

        Pilha<Integer> pilha = new Pilha<>();
        pilha.adicionar(10);
        pilha.adicionar(20);
        pilha.adicionar(30);

        System.out.println("Elemento no topo da pilha: " + pilha.peek());
        System.out.println("Pilha após peek(): " + pilha);
        System.out.println();
    }

    public static void testIsEmpty() {
        System.out.println("Testando isEmpty() para verificar se a pilha está vazia:");

        Pilha<Integer> pilha = new Pilha<>();
        System.out.println("A pilha está vazia? " + pilha.isEmpty());

        pilha.adicionar(10);
        pilha.adicionar(20);

        System.out.println("A pilha está vazia? " + pilha.isEmpty());
        System.out.println();
    }

    public static void testSize() {
        System.out.println("Testando size() para verificar o tamanho da pilha:");

        Pilha<Integer> pilha = new Pilha<>();
        System.out.println("Tamanho da pilha: " + pilha.size());

        pilha.adicionar(10);
        pilha.adicionar(20);
        pilha.adicionar(30);

        System.out.println("Tamanho da pilha após adicionar elementos: " + pilha.size());
        System.out.println();
    }
}
