package toystore;

public class PrizeToy extends Toy implements Prize {
    private int quantity;
    private int frequency;

    public PrizeToy(int id, String name, int quantity, int frequency) {
        super(id, name);
        this.quantity = quantity;
        this.frequency = frequency;
    }

    @Override
    public int getQuantity() {
        return quantity;
    }

    @Override
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }

    @Override
    public int getFrequency() {
        return frequency;
    }

    @Override
    public void setFrequency(int frequency) {
        this.frequency = frequency;
    }
}
