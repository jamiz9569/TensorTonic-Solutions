import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    N = len(A)
    M = len(A[0])
    
    # Initialize a result list with swapped dimensions (M rows, N columns)
    result = [[0.0 for _ in range(N)] for _ in range(M)]
    
    for i in range(N):
        for j in range(M):
            result[j][i] = A[i][j]
            
    return np.array(result)