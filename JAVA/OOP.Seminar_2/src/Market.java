import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;



public class Market implements QueueBahaviour, MarketBahaviour {

    private List<Human> humansInMarket;
    private Queue<Human> humansQueve;

    public Market() {
        this.humansInMarket = new ArrayList<>();
        this.humansQueve = new LinkedList<>();
    }

    @Override
    public void acceptToMarket(Human human) {
        humansInMarket.add(human);

    }

    @Override
    public void releasedFromMarket(Human human) {
        humansInMarket.remove(human);


    }

    @Override
    public void takeQueue(Human human) {
        humansQueve.offer(human);

    }

    @Override
    public void takeOrders() {
        humansQueve.peek().setMakeOrder();


    }

    @Override
    public void giveOrders() {
        humansQueve.peek().isTakeOrder();

    }

    @Override
    public void releasedFromQueve() {
        System.out.println("Осталось" + humansInMarket.size());
        System.out.println("Bye" + humansQueve.peek().name);

        releasedFromMarket(humansQueve.poll());

    }


    public void update() {

        for (Human h : humansInMarket){
            humansQueve.offer(h);
        }
        while (!humansQueve.isEmpty()){
            takeOrders();
            giveOrders();
            releasedFromQueve();

        }
        System.out.println("Queue is empty");
    }
}