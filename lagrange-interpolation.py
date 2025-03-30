import numpy as np
from sympy import symbols, simplify, expand, Rational

def get_points(n: int):
    x_values = []
    y_values = []
    
    print("Enter the coordinates of the three points:")
    for i in range(n):
        try:
            x = Rational(input(f"x{i}: "))
            y = Rational(input(f"y{i}: "))
            x_values.append(x)
            y_values.append(y)
        except ValueError:
            print("Error: Please enter valid numbers.")
            return None, None
    
    return x_values, y_values

def get_target_value():
    try:
        x_target = Rational(input("Enter the x value to evaluate the polynomial: "))
        return x_target
    except ValueError:
        print("Error: Please enter a valid number.")
        return None

def calculate_lagrange_polynomials(x_values, x):
    L = []
    n = len(x_values)
    for i in range(n):
        numerator = 1
        denominator = 1
        
        # Build Li
        for j in range(n):
            if i != j:
                numerator *= (x - x_values[j])
                denominator *= (x_values[i] - x_values[j])
        
        L.append(numerator / Rational(denominator))
    
    return L

def build_polynomial(y_values, L):
    polynomial = 0
    n = len(y_values)
    for i in range(n):
        polynomial += y_values[i] * L[i]
    
    return polynomial

def display_results(L, y_values, polynomial, x_target, x):
    simplified_polynomial = simplify(polynomial)
    expanded_polynomial = expand(polynomial)
    
    n = len(y_values)

    interpolated_value = simplified_polynomial.subs(x, x_target)
    
    # Display results
    print("\nLagrange Interpolation Results:")
    for i in range(n):
      print(f"\nL{i} = {L[i]}")
    print(f"\nUnsimplified polynomial:")
    print("f(x) = ")
    for i in range(n):
      if (i > 0):
        print(" + ")
      print(f"{y_values[i]}*({L[i]})")
    print(f"\nExpanded polynomial:")
    print(f"f(x) = {expanded_polynomial}")
    print(f"\nSimplified polynomial:")
    print(f"f(x) = {simplified_polynomial}")
    print(f"\nFor x = {x_target}, f(x) = {interpolated_value}")

def main():
    points_number: int
    points_number = int(input("Number of points: "))

    x_values, y_values = get_points(points_number)
    if x_values is None or y_values is None:
        return
    
    x_target = get_target_value()
    if x_target is None:
        return
    
    x = symbols('x')
    
    L = calculate_lagrange_polynomials(x_values, x)
    
    polynomial = build_polynomial(y_values, L)
    
    display_results(L, y_values, polynomial, x_target, x)

if __name__ == "__main__":
    main()
