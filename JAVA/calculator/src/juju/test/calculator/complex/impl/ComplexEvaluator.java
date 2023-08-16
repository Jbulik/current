package juju.test.calculator.complex.impl;

import juju.test.calculator.complex.Evaluator;
import juju.test.calculator.complex.complex.Complex;

public class ComplexEvaluator implements Evaluator {
    @Override
    public Complex calculate(Complex arg1, Complex arg2, Opeation opeation) throws Exception {
        switch (opeation) {
            case ADD:
                return add(arg1, arg2);
            case SUB:
                return sub(arg1, arg2);
            case MUL:
                return mul(arg1, arg2);
            case DIV:
                return div(arg1, arg2);
            default:
                throw new Exception("Operation is null");
        }
    }

    public Complex add(Complex arg1, Complex arg2) {
        double real = arg1.getR() + arg2.getR();
        double imag = arg1.getI() + arg2.getI();
        return new Complex(real, imag);
    }

    public Complex sub(Complex arg1, Complex arg2) {
        double real = arg1.getR() - arg2.getR();
        double imag = arg1.getI() - arg2.getI();
        return new Complex(real, imag);
    }

    public Complex mul(Complex arg1, Complex arg2) {
        double real = arg1.getR() * arg2.getR() - arg1.getI() * arg2.getI();
        double imag = arg1.getR() * arg2.getI() + arg1.getI() * arg2.getR();
        return new Complex(real, imag);
    }


    public Complex div(Complex arg1, Complex arg2) {
        double scale = arg2.getR() * arg2.getR() + arg2.getI() * arg2.getI();
        Complex arg2B = new Complex(arg2.getR() / scale, -arg2.getI() / scale);
        return mul(arg1, arg2B);
    }


}
