package listas;

import java.lang.reflect.Array;

public class Vetor<T> {

    private T[] elementos;
    private Integer tamanho;

    @SuppressWarnings("unchecked")
    public Vetor() {
        this.elementos = (T[]) new Object[10];
        this.tamanho = 0;
    }

    @SuppressWarnings("unchecked")
    public Vetor(Class<T> classTipo) {
        this.elementos = (T[]) Array.newInstance(classTipo, 10);
        this.tamanho = 0;
    }

    public void adicionar(T elemento) {
        this.aumentaCapacidade();
        if (this.tamanho < this.elementos.length) {
            this.elementos[this.tamanho] = elemento;
            this.tamanho++;
        }
    }

    @SuppressWarnings("unchecked")
    private void aumentaCapacidade() {
        if (this.tamanho == this.elementos.length) {
            T[] elementosNovos = (T[]) new Object[this.elementos.length * 2];
            for (int i = 0; i < this.elementos.length; i++) {
                elementosNovos[i] = this.elementos[i];
            }
            this.elementos = elementosNovos;
        }
    }

    public void adicionar(int posicao, T elemento) {
        if (!(posicao >= 0 && posicao < tamanho)) {
            throw new IllegalArgumentException("Posição invalida");
        }
        this.aumentaCapacidade();
        for (int i = this.tamanho - 1; i >= posicao; i--) {
            this.elementos[i + 1] = this.elementos[i];
        }
        this.elementos[posicao] = elemento;
        this.tamanho++;
    }

    public Integer tamanho() {
        return this.tamanho;
    }

    @Override
    public String toString() {
        StringBuilder s = new StringBuilder();
        s.append("[ ");

        for (int i = 0; i < this.tamanho - 1; i++) {
            s.append(this.elementos[i]);
            s.append(", ");
        }

        if (this.tamanho > 0) {
            s.append(this.elementos[this.tamanho - 1]);
        }

        s.append(" ]");

        return s.toString();
    }

    public T busca(int posicao) {
        if (!(posicao >= 0 && posicao < tamanho)) {
            throw new IllegalArgumentException("Posição invalida");
        }
        return this.elementos[posicao];
    }

    public T obtem(int posicao) {
        return busca(posicao);
    }

    public Integer busca(T elemento) {
        for (int i = 0; i < this.tamanho; i++) {
            if (this.elementos[i].equals(elemento)) {
                return i;
            }
        }
        return -1;
    }

    public Boolean contem(T elemento) {
        return this.busca(elemento) >= 0;
    }

    public void remove(int posicao) {
        if (!(posicao >= 0 && posicao < tamanho)) {
            throw new IllegalArgumentException("Posição invalida");
        }
        for (int i = posicao; i < this.tamanho - 1; i++) {
            this.elementos[i] = this.elementos[i + 1];
        }
        this.tamanho--;
    }

    public void remove(T elemento) {
        int posicao = this.busca(elemento);
        if (posicao >= 0) {
            this.remove(posicao);
        }
    }

    public Integer ultimoIndex(T elemento) {
        for (int i = this.tamanho - 1; i >= 0; i--) {
            if (this.elementos[i].equals(elemento)) {
                return i;
            }
        }
        return -1;
    }

    @SuppressWarnings("unchecked")
    public void limpar() {
        this.elementos = (T[]) new Object[this.elementos.length];
    }

}
