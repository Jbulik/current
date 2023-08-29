package toystore;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.PrintStream;

public class App {
    public static void main(String[] args) throws IOException {
        ToyStore toyStore = new ToyStore();

        // Добавляем игрушки
        toyStore.add(new PrizeToy(1, "Bear", 1, 10));
        toyStore.add(new PrizeToy(2, "Duck", 3, 25));
        toyStore.add(new PrizeToy(3, "Rabbit", 8, 31));
        toyStore.add(new PrizeToy(4, "Barbie", 5, 77));


        // разыгрываем приз
        boolean hasWinner = toyStore.game();

        PrintStream file = new PrintStream(new FileOutputStream("winners.txt"));
        if (hasWinner) {
            // получаем приз
            Toy toy = toyStore.getPrise();

            // записываем приз в файл
            System.out.printf("id=%d, name=%s\n", toy.getId(), toy.getName());
            file.printf("id=%d, name=%s\n", toy.getId(), toy.getName());
        } else {
            System.out.println("Нет доступных призов");
            file.println("Нет доступных призов");
        }
        file.close();
    }
}
