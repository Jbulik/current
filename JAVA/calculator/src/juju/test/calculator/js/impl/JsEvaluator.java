package juju.test.calculator.js.impl;

import juju.test.calculator.js.Evaluator;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

public class JsEvaluator implements Evaluator {
    private final ScriptEngine js;

    public JsEvaluator() {
        js = new ScriptEngineManager().getEngineByName("javascript");
    }

    @Override
    public String evaluate(String expression) throws ScriptException {
        Object result = js.eval(expression);
        return String.valueOf(result);
    }
}
