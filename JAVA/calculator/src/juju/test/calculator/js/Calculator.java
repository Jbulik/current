package juju.test.calculator.js;

public class Calculator {

    private UserInput userInput;
    private Logger logger;
    private Evaluator evaluator;

    public void setLogger(Logger logger) {
        this.logger = logger;
    }

    public void setEvaluator(Evaluator evaluator) {
        this.evaluator = evaluator;
    }

    public void setUserInput(UserInput userInput) {
        this.userInput = userInput;
    }

    public void calculate() {
        logger.log("starting calculator");
        logger.log("printing user prompt and reading user input...");
        userInput.prompt("Enter expression end press Enter>");
        String expression = userInput.read();
        logger.log("user input is \"" + expression + "\"");
        String result;
        try {
            logger.log("calculating..");
            result = evaluator.evaluate(expression);
            logger.log("calculation result \"" + result + "\"");
            userInput.show(result);
        } catch (Exception e) {
            logger.log("calculation error \"" + e.getMessage() + "\"");
            userInput.show("Expression error");
        }
        logger.log("finished");
    }
}
