import sympy as sp
import numpy as np

def forward_finite_difference(f, x0, h=0.01):
    first_derivative = (f(x0 + h) - f(x0)) / h
    second_derivative = (f(x0 + 2*h) - 2*f(x0 + h) + f(x0)) / h**2
    return first_derivative, second_derivative

def main():
    expr = input("Enter the function in terms of x (e.g., sin(x) + x**2): ")
    x = sp.symbols('x')
    function = sp.sympify(expr)
    f_lambda = sp.lambdify(x, function, "numpy")
    
    x0 = float(input("Enter the point x0 where the derivative should be evaluated: "))
    h = float(input("Enter the step size h (e.g., 0.01): "))

    first_num, second_num = forward_finite_difference(f_lambda, x0, h)

    first_analytic = sp.diff(function, x).evalf(subs={x: x0})
    second_analytic = sp.diff(function, x, x).evalf(subs={x: x0})

    first_num_expr = f"(({x0 + h}^2) - ({x0}^2)) / {h}"
    second_num_expr = f"(({x0 + 2*h}^2) - 2*({x0 + h}^2) + ({x0}^2)) / {h**2}"
    first_analytic_expr = sp.diff(function, x).subs(x, x0)
    second_analytic_expr = sp.diff(function, x, x).subs(x, x0)

    first_num_error = round(first_num - first_analytic, 5)
    second_num_error = round(second_num - second_analytic, 5)

    print("\nResults:")
    print(f"First numerical derivative: {first_num:.5f}")
    print(f"First numerical derivative expression: {first_num_expr}")
    print(f"First analytical derivative: {first_analytic:.5f}")
    print(f"First analytical derivative expression: {first_analytic_expr}")
    print(f"First numerical derivative error: {first_num_error}")
    print(f"Second numerical derivative: {second_num:.5f}")
    print(f"Second numerical derivative expression: {second_num_expr}")
    print(f"Second analytical derivative: {second_analytic:.5f}")
    print(f"Second analytical derivative expression: {second_analytic_expr}")
    print(f"Second numerical derivative error: {second_num_error}")

if __name__ == "__main__":
    main()

