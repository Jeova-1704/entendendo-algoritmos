package pilhas;

import java.util.ArrayList;

public class Pilha<E> {
    private ArrayList<E> pilha;

    public Pilha() {
        this.pilha = new ArrayList<>();
    }

    public void adicionar(E item) {
        this.pilha.add(item);
    }

    public E pop(){
        if (this.isEmpty()) {
            throw new IllegalStateException("A pilha está vazia.");
        }
        int ultimoIndex = getUltimoIndex();
        return this.pilha.remove(ultimoIndex);
    }

    public E peek(){
        if (this.isEmpty()) {
            throw new IllegalStateException("A pilha está vazia.");
        }
        int ultimoIndex = getUltimoIndex();
        return this.pilha.get(ultimoIndex);
    }

    public boolean isEmpty(){
        if (this.pilha.isEmpty()) {
            return true;
        }
        return false;
    }

    public int size(){
        return this.pilha.size();
    }

    public void clear(){
        this.pilha = new ArrayList<>();
    }

    private int getUltimoIndex(){
        return this.pilha.size() - 1;
    }

    @Override
    public String toString(){
        return this.pilha.toString();
    }
}
