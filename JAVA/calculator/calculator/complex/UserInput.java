package calculator.complex;

import calculator.complex.complex.Complex;
import calculator.complex.impl.Opeation;

public interface UserInput {
    void prompt(String message);

    Complex readArgument();

    Opeation readOperation() throws Exception;

    void show(String result);
}
