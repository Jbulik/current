package juju.test.calculator.complex;

import juju.test.calculator.complex.complex.Complex;
import juju.test.calculator.complex.impl.Opeation;

public interface UserInput {
    void prompt(String message);

    Complex readArgument();

    Opeation readOperation() throws Exception;

    void show(String result);
}
