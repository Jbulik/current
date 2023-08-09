package juju.test.calculator.complex.complex;


public class Complex {
    private double r;
    private double i;

    public Complex(double real, double imag) {
        r = real;
        i = imag;
    }

    public double getR() {
        return r;
    }

    public double getI() {
        return i;
    }

    public String toString() {
        if (i == 0) return r + "";
        if (r == 0) return i + "i";
        if (i < 0) return r + " - " + (-i) + "i";
        return r + " + " + i + "i";
    }

}