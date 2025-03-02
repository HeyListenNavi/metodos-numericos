import numpy as np
from typing import Callable, Optional

def successive_approximations_recursive(f: Callable[[float], float], tol: float, x: float = 0.5, iteration: int = 1) -> float:
    new_x: float = f(x) 
    difference: float = abs(new_x - x)

    # Print iteration in table format
    print(f"{'Iteration':<10}{'x':<10}{'g(x)':<10}{'Dif':<10}")
    print(f"{iteration:<10}{x:<10.6f}{new_x:<10.6f}{difference:<10.2E}")
    print()
    
    # Check tolerance
    isDifferenceLessThanTolerance: bool = difference < tol

    if isDifferenceLessThanTolerance:
        return new_x
    
    return successive_approximations_recursive(f=f, tol=tol, x=new_x, iteration=iteration + 1)

def main():
    equation = input("Enter the function in terms of x (e.g., x**3 - 4*x - 9): ")
    f: Callable[[float], float] = lambda x: eval(equation, {"x": x, "np": np})
    
    tol: float = float(input("Enter the tolerance: "))
    x: float = float(input("Enter x0: "))
    
    solution: float = successive_approximations_recursive(f=f, tol=tol, x=x)
    print(f"Solution found: {solution:.6f}")

if __name__ == "__main__":
    main()