package toystore;

public class Toy {
    private int id;
    private String name;

    public Toy(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public int getId() {
        return id;
    }

    public String getName() {
        return name;
    }
}
