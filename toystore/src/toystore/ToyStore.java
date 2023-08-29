package toystore;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.Random;

public class ToyStore {
    private List<Prize> prizes = new ArrayList<>();

    private Queue<Toy> winning = new LinkedList<>();

    public void add(PrizeToy priseToy) {
        prizes.add(priseToy);
    }

    public boolean game() {
        List<Prize> prizesInGame = new ArrayList<>();

        if (prizes.isEmpty()) {
            return false;
        }

        for (Prize prize : prizes) {

            for (int i = 0; i < prize.getFrequency(); i++) {
                prizesInGame.add(prize);
            }
        }

        Random random = new Random();
        int randomIndex = random.nextInt(prizesInGame.size());
        Prize prize = prizesInGame.get(randomIndex);
        prize.setQuantity(prize.getQuantity() - 1);
        if (prize.getQuantity() == 0) {
            prizes.remove(prize);
        }

        winning.offer((Toy) prize);
        return true;
    }

    public Toy getPrise() {
        return winning.poll();
    }


}
