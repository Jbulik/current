package juju.test.calculator.js;

public interface UserInput {
    void prompt(String message);
    String read();
    void show(String result);
}
