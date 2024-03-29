// Задание Реализуйте структуру телефонной книги с помощью HashMap.
//Программа также должна учитывать, что в во входной структуре будут повторяющиеся имена с разными телефонами,
// их необходимо считать, как одного человека с разными телефонами.
// Вывод должен быть отсортирован по убыванию числа телефонов.

import java.util.*;

public class PhoneBook {
    public static void main(String[] args) {
        // Создаем телефонную книгу с помощью HashMap
        Map<String, Set<String>> phoneBook = new HashMap<>();

        // заполненяем телефонную книгу
        addContact(phoneBook, "Иванов", "1234567890");
        addContact(phoneBook, "Петров", "9876543210");
        addContact(phoneBook, "Иванов", "5555555555");
        addContact(phoneBook, "Сидоров", "1111111111");
        addContact(phoneBook, "Петров", "9999999999");
        addContact(phoneBook, "Сидоров", "2222222222");
        addContact(phoneBook, "Иванов", "8888888888");
        addContact(phoneBook, "Иванов", "15615615615");
        addContact(phoneBook, "Иванов", "3333333333");
        addContact(phoneBook, "Петров", "8888888888");

        // Сортируем по убыванию числа телефонов
        List<Map.Entry<String, Set<String>>> sortedEntries = new ArrayList<>(phoneBook.entrySet());
        sortedEntries.sort((entry1, entry2) -> Integer.compare(entry2.getValue().size(), entry1.getValue().size()));

        // Выводим отсортированные записи
        for (Map.Entry<String, Set<String>> entry : sortedEntries) {
            System.out.println("Имя: " + entry.getKey());
            System.out.println("Телефоны:");
            for (String phone : entry.getValue()) {
                System.out.println(phone);
            }
            System.out.println();
        }
    }

    // Метод для добавления контакта в телефонную книгу
    public static void addContact(Map<String, Set<String>> phoneBook, String name, String phone) {
        // Если контакт уже существует, добавляем телефон к существующему списку
        if (phoneBook.containsKey(name)) {
            phoneBook.get(name).add(phone);
        } else { // Иначе создаем новую запись
            Set<String> phones = new HashSet<>();
            phones.add(phone);
            phoneBook.put(name, phones);
        }
    }
}




