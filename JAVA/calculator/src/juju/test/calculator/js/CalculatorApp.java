package juju.test.calculator.js;

import juju.test.calculator.js.impl.ConsoleLogger;
import juju.test.calculator.js.impl.ConsoleUserInput;
import juju.test.calculator.js.impl.JsEvaluator;

public class CalculatorApp {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        calculator.setEvaluator(new JsEvaluator());
        calculator.setUserInput(new ConsoleUserInput());
        calculator.setLogger(new ConsoleLogger("calculator"));
        calculator.calculate();
    }
}
