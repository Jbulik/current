package juju.test.calculator.js.impl;

import juju.test.calculator.js.Logger;

public class ConsoleLogger implements Logger {
    private String name;
    private static final String clr = "\033[0;32m";

    public ConsoleLogger(String name) {
        this.name = name;
    }

    public void log(String message) {
        System.out.println(clr + name + ": " + message);
    }
}