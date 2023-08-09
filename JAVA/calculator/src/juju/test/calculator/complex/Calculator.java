package juju.test.calculator.complex;

import juju.test.calculator.complex.complex.Complex;
import juju.test.calculator.complex.impl.Opeation;

public class Calculator {

    private UserInput userInput;
    private Logger logger;
    private Evaluator evaluator;

    public void setLogger(Logger logger) {
        this.logger = logger;
    }

    public void setUserInput(UserInput userInput) {
        this.userInput = userInput;
    }

    public void setEvaluator(Evaluator evaluator) {
        this.evaluator = evaluator;
    }

    public void calculate() throws Exception {
        logger.log("starting calculator");
        logger.log("printing user prompt and reading user input...");
        userInput.prompt("Enter 1st argumentpress Enter>");
        Complex arg1 = userInput.readArgument();
        logger.log("1st argument is \"" + arg1 + "\"");

        userInput.prompt("Enter 2st argumentpress Enter>");
        Complex arg2 = userInput.readArgument();
        logger.log("2st argument is \"" + arg2 + "\"");

        userInput.prompt("Enter operation and press Enter>");
        Opeation op = userInput.readOperation();
        logger.log("Operation is \"" + op + "\"");

        Complex result = evaluator.calculate(arg1, arg2, op);

        logger.log("Calculation result is " + result);
        userInput.show("Result is: " + result);
        logger.log("finished");
    }

}
