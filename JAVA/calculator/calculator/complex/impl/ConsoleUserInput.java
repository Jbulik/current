package calculator.complex.impl;

import calculator.complex.UserInput;
import calculator.complex.complex.Complex;

import java.util.Scanner;

public class ConsoleUserInput implements UserInput {
    private static final String clr = "\033[0;34m";

    @Override
    public void prompt(String message) {
        System.out.print(clr + message);
    }

    @Override
    public Complex readArgument() {
        Scanner in = new Scanner(System.in);

        String input = in.nextLine();
        String[] parts = input.split(",");
        return new Complex(Double.parseDouble(parts[0]), Double.parseDouble(parts[1]));
    }

    public Opeation readOperation() throws Exception {
        Scanner in = new Scanner(System.in);

        String input = in.nextLine();
        for (Opeation op : Opeation.values()) {
            if (input.equals(op.getOp())) {
                return op;
            }
        }
        throw new Exception("Unknown operation");
    }

    @Override
    public void show(String message) {
        System.out.println(clr + message);
    }
}
