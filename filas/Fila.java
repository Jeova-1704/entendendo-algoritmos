import java.util.ArrayList;
import java.util.List;

public class Fila {
    private List<Object> fila;

    public Fila() {
        this.fila = new ArrayList<>();
    }

    public boolean isEmpty() {
        return this.fila.isEmpty();
    }

    public void adiciona(Object item) {
        this.fila.add(item);
    }

    public Object remove() {
        if (!isEmpty()) {
            return this.fila.remove(0);
        } else {
            throw new IndexOutOfBoundsException("A fila está vazia.");
        }
    }

    public int tamanho() {
        return this.fila.size();
    }

    public Object primeiroElemento() {
        if (!isEmpty()) {
            return this.fila.get(0);
        } else {
            throw new IndexOutOfBoundsException("A fila está vazia.");
        }
    }

    public void clear() {
        this.fila.clear();
    }

    public boolean verificaPresenca(Object item) {
        return this.fila.contains(item);
    }

    public List<Object> copia() {
        return new ArrayList<>(this.fila);
    }
}
