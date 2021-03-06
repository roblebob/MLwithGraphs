import numpy as np


def florence():
    return np.array([
        #Ac Al Ba Bi Ca Gi Gu La Me Pa Pe Ri Sa St To
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Ac
        [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # Al
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # Ba
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],  # Bi
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # Ca
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Gi
        [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],  # Gu
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # La
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # Me
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # Pa
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # Pe
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1],  # Ri
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # Sa
        [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],  # St
        [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0],  # To
    ])


def node_centrality_trail(A=florence(), iterations=30):
    """eigenvector centrality"""
    e = np.ones(A.shape[0])

    for _ in np.arange(0, iterations):
        e = (A @ e.T)
        e /= np.linalg.norm(e)
    else:
        pass

    return e


if __name__ == '__main__':
    print(node_centrality_trail(florence(), 2000))
