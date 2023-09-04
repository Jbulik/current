package calculator.complex;

import calculator.complex.complex.Complex;
import calculator.complex.impl.Opeation;

public interface Evaluator {
    Complex calculate(Complex arg1, Complex arg2, Opeation opeation) throws Exception;
}

