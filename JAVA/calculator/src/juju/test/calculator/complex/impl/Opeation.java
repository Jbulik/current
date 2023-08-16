package juju.test.calculator.complex.impl;

public enum Opeation {
    ADD("+"),
    SUB("-"),
    MUL("*"),
    DIV("/");

    private final String op;

    Opeation(String op) {
        this.op = op;
    }

    public String getOp() {
        return op;
    }
}
