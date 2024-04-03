package listas;

public class Main {
    public static void main(String[] args) {
        Vetor<String> vetor = new Vetor<>();
        System.out.println(vetor);

        vetor.adicionar("A");
        vetor.adicionar("C");
        vetor.adicionar("D");
        vetor.adicionar("E");
        vetor.adicionar("A");
        System.out.println(vetor);
        vetor.adicionar(1, "B");
        System.out.println(vetor);
        System.out.println(vetor.contem("A"));
        System.out.println(vetor.contem("J"));
        System.out.println(vetor.ultimoIndex("A"));


    }
}
