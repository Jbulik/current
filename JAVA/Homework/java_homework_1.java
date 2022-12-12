import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

/**
 * Составить частотный словарь элементов одномерного массива
 * Частотный словарь содержит информацию о том, сколько раз встречается элемент
 * входных данных. { 1, 9, 9, 0, 2, 8, 0, 9 }; // Задание списка чисел c клавиатуры.
0 встречается 2 раз(а)
1 встречается 1 раз(а)
2 встречается 1 раз(а)
8 встречается 1 раз(а)
9 встречается 3 раз(а)
 */
public class java_homework_1 {

    public static void main(String[] args) {
        String[] UserList = scan();
        int[] List = parse(UserList);
        Map<Integer, Integer> dictionaryValues;
        dictionaryValues = dictData(List);
        outData(dictionaryValues);
    }    
          
    
    static String[] scan() {
        // Ввод данных пользователем
        System.out.println("Введите числа через пробел: ");
        Scanner scn = new Scanner(System.in);
        String[] data = scn.nextLine().split(" ");
        scn.close();
        return data;        
    }



    static int[] parse(String[] str) {
        // Преобразование строки в числа
        int[] listInt = new int[str.length];
        for (int i = 0; i < str.length; i++) {
            listInt[i] = Integer.parseInt(str[i]);
        }
        return listInt;
    }

    static <dictionary> Map<Integer, Integer> dictData(int[] intList) {
        // Создание словаря. Ключ - число из списка. Значение - сколько раз встречается
        // число.
        Map<Integer, Integer> dictQuantityElement = new HashMap<Integer, Integer>();
        for (int i = 0; i < intList.length; i++) {
            if (dictQuantityElement.containsKey(intList[i]) != true) {
                dictQuantityElement.put(intList[i], 1);
            } else {
                dictQuantityElement.put(intList[i], dictQuantityElement.get(intList[i]) + 1);
            }
        }
        return dictQuantityElement;
    }

    static void outData(Object dictionaryValues) {
        // Вывод на печать
        for (Map.Entry<Integer, Integer> set : ((Map<Integer, Integer>) dictionaryValues).entrySet()) {
            System.out.printf("%d встречается %d раз\n", set.getKey(), set.getValue());
        }
    }
}
