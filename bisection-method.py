import numpy as np
from typing import Callable, Optional

def bisection_recursive(f: Callable[[float], float], a: float, b: float, tol: float, prev_c: Optional[float] = None, iteration: int = 1) -> float:
    # Calculate Midpoint
    c: float = (a + b) / 2 
    f_a: float = f(a)
    f_b: float = f(b)
    f_c: float = f(c)
    
    isErrorLessThanTolerance: bool = False;

    # Compute error percentage
    error = np.nan
    if prev_c != None:
        error: float = abs((c - prev_c) / c)
        # Check tolerance
        isErrorLessThanTolerance = error < tol
    
    # Print iteration in table format
    print(f"{'Iteration':<10}{'a':<10}{'b':<10}{'c':<10}{'f(a)':<10}{'f(b)':<10}{'f(c)':<10}{'Error %':<10}")
    print(f"{iteration:<10}{a:<10.6f}{b:<10.6f}{c:<10.6f}{f_a:<10.6f}{f_b:<10.6f}{f_c:<10.6f}{(error*100) if not np.isnan(error) else 'N/A':<10}")
    print()

    if isErrorLessThanTolerance or f_c == 0:
        return c
    
    if f_a * f_c < 0:
        return bisection_recursive(f, a, c, tol, c, iteration + 1)
    
    return bisection_recursive(f, c, b, tol, c, iteration + 1)

def main():
    equation = input("Enter the function in terms of x (e.g., x**3 - 4*x - 9): ")
    f: Callable[[float], float] = lambda x: eval(equation, {"x": x, "np": np})
    
    a: float = float(input("Enter the lower bound (a): "))
    b: float = float(input("Enter the upper bound (b): "))
    tol: float = float(input("Enter the tolerance: "))
    
    root: float = bisection_recursive(f=f, a=a, b=b, tol=tol)
    print(f"Root found: {root:.6f}")

if __name__ == "__main__":
    main()