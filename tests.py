import pytest
from calculator import evaluate_expression  # Asegúrate de importar la función desde el módulo correcto

def test_simple_addition():
    assert evaluate_expression("2 + 2") == 4

def test_simple_subtraction():
    assert evaluate_expression("5 - 3") == 2

def test_simple_multiplication():
    assert evaluate_expression("4 * 3") == 12

def test_simple_division():
    assert evaluate_expression("10 / 2") == 5

def test_division_by_zero():
    assert evaluate_expression("5 / 0") == "Error: division by zero"

def test_expression_with_parentheses():
    assert evaluate_expression("2 + (3 * 4)") == 14

def test_nested_parentheses():
    assert evaluate_expression("(2 + (3 * 4)) - 5") == 9

def test_invalid_expression():
    assert evaluate_expression("2 + 2 *") == "Error: invalid syntax"  # Ajusta el mensaje de error según la implementación

def test_mixed_operators():
    assert evaluate_expression("2 + 3 * (4 - 1)") == 11
