public class Main {
    public static void main(String[] args) {

        Human h = new Human("Julia");
        Human h1 = new Human("Jul1");
        Human h2 = new Human("Jul2");
        Human h3 = new Human("Jul3");

        Market market1 = new Market();

        market1.acceptToMarket(h);
        market1.acceptToMarket(h1);
        market1.acceptToMarket(h2);
        market1.acceptToMarket(h3);

        market1.update();





    }
}