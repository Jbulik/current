package juju.test.calculator.js.impl;

import juju.test.calculator.js.UserInput;

import java.util.Scanner;

public class ConsoleUserInput implements UserInput {
    private static final String clr = "\033[0;34m";

    @Override
    public void prompt(String message) {
        System.out.print(clr + message );
    }

    @Override
    public String read() {
        Scanner in = new Scanner(System.in);
        return in.nextLine();
    }

    @Override
    public void show(String message) {
        System.out.println(clr + message);
    }
}
