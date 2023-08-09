package juju.test.calculator.complex;

import juju.test.calculator.complex.complex.Complex;
import juju.test.calculator.complex.impl.Opeation;

public interface Evaluator {
    Complex calculate(Complex arg1, Complex arg2, Opeation opeation) throws Exception;
}

