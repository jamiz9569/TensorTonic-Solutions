import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    m= np.asarray(x,dtype=float)
    n= np.asarray(y,dtype=float)
    result = np.dot(m, n)

    return float(result)
    # Write code here
    