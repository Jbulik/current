package calculator.complex;

import calculator.complex.impl.ComplexEvaluator;
import calculator.complex.impl.ConsoleLogger;
import calculator.complex.impl.ConsoleUserInput;

public class CalculatorApp {
    public static void main(String[] args) throws Exception {
        Calculator calculator = new Calculator();
        calculator.setEvaluator(new ComplexEvaluator());
        calculator.setUserInput(new ConsoleUserInput());
        calculator.setLogger(new ConsoleLogger("calculator"));
        calculator.calculate();
    }
}
