import math
import numpy as np

def rectangle_rule():
    print("\n=== Rectangle Rule Approximation ===")
    a = float(input("Enter lower limit of integration (a): "))
    b = float(input("Enter upper limit of integration (b): "))
    n = int(input("Enter number of subintervals (n): "))
    
    # Get the function from user
    print("Enter your function in terms of x (e.g., 3*x**2 + 2*x + 1): ")
    print("Note: Use math.sin(x), math.exp(x), math.log(x), etc.")
    func_str = input("f(x) = ")
    
    # Define the function using lambda
    f = lambda x: eval(func_str, {'math': math, 'np': np, 'x': x})
    
    h = (b - a) / n
    integral = 0.0
    
    print("\nCalculation details:")
    print(f"Formula: Σ [f(x_i) * h] from i=0 to {n-1} where h = (b-a)/n = {h:.4f}")
    print("----------------------------------------")
    
    for i in range(n):
        x_i = a + i * h
        fx = f(x_i)
        integral += fx * h
        print(f"Interval {i+1}: x_{i} = {x_i:.4f}, f({x_i:.4f}) = {fx:.4f}, area = {fx:.4f} * {h:.4f} = {fx*h:.4f}")
    
    print("----------------------------------------")
    print(f"Approximate integral using Rectangle Rule with {n} subintervals: {integral:.6f}")
    print(f"Formula applied: Σ [f(x_i)*h] = {integral:.6f}")

def simpson_38_rule():
    print("\n=== Simpson's 3/8 Rule Approximation ===")
    a = float(input("Enter lower limit of integration (a): "))
    b = float(input("Enter upper limit of integration (b): "))
    n = int(input("Enter number of subintervals (must be multiple of 3): "))
    
    if n % 3 != 0:
        print("Error: Number of subintervals must be a multiple of 3 for Simpson's 3/8 Rule.")
        return
    
    # Get the function from user
    print("Enter your function in terms of x (e.g., np.e + x**2): ")
    func_str = input("f(x) = ")
    
    # Define the function using lambda
    f = lambda x: eval(func_str, {'math': math, 'np': np, 'x': x})
    
    h = (b - a) / n
    integral = f(a) + f(b)
    
    print("\nCalculation details:")
    print(f"Formula: (3h/8) * [f(x0) + 3Σf(xi) + 2Σf(xj) + f(xn)] where i≠3k, j=3k")
    print(f"Step size h = (b-a)/n = {h:.4f}")
    print("----------------------------------------")
    print(f"Initial terms: f({a:.4f}) + f({b:.4f}) = {f(a):.4f} + {f(b):.4f} = {f(a)+f(b):.4f}")
    
    for i in range(1, n):
        x_i = a + i * h
        if i % 3 == 0:
            term = 2 * f(x_i)
            integral += term
            print(f"x_{i} = {x_i:.4f} (multiple of 3): 2*f({x_i:.4f}) = 2*{f(x_i):.4f} = {term:.4f}")
        else:
            term = 3 * f(x_i)
            integral += term
            print(f"x_{i} = {x_i:.4f}: 3*f({x_i:.4f}) = 3*{f(x_i):.4f} = {term:.4f}")
    
    coefficient = 3 * h / 8
    final_integral = integral * coefficient
    
    print("----------------------------------------")
    print(f"Sum of all terms = {integral:.4f}")
    print(f"Final multiplication: (3h/8) = {coefficient:.6f}")
    print(f"Approximate integral using Simpson's 3/8 Rule with {n} subintervals: {final_integral:.6f}")
    print(f"Formula applied: (3*{h:.4f}/8)*{integral:.4f} = {final_integral:.6f}")

def main():
    while True:
        print("\nIntegral Approximation Calculator")
        print("1. Rectangle Rule")
        print("2. Simpson's 3/8 Rule")
        print("3. Exit")
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            rectangle_rule()
        elif choice == '2':
            simpson_38_rule()

if __name__ == "__main__":
    main()