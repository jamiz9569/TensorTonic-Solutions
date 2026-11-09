import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    x = np.asarray(a, dtype=float)
    y = np.asarray(b, dtype=float)

    dot = np.dot(x, y)

    norm_x = np.linalg.norm(x)
    norm_y = np.linalg.norm(y)

    if norm_x == 0 or norm_y == 0:
        return 0.0

    return float(dot / (norm_x * norm_y))