import cvxpy as cp
import numpy as np
from sinkhorn_knopp import sinkhorn_knopp as skp

#u = np.array((0.81, 0.80, 0.79, 0.78, 0.77, 0.76))
# u = np.array((0.81, 0.80, 0.79, 0.78, 0.77, 0.0))

#ATTENZIONE, PARAMETRIZZARE I GRUPPI. QUI FA :3, PERCHè HO DUE GRUPPI DA 3 (I PRIMI 3 E GLI ULTIMI 3)


def findProbMatrix(u):
    v = np.array([1.0/(np.log(2 + i)) for i, _ in enumerate(u)])
    P = cp.Variable((len(u), len(u)))
    objective = cp.Maximize(cp.matmul(cp.matmul(u, P), v))
    constraints = [cp.matmul(np.ones((1,len(u))), P) == np.ones((1,len(u))),
                   cp.matmul(P, np.ones((len(u),))) == np.ones((len(u),)),
                   0 <= P, P <= 1,
                   cp.matmul(cp.matmul(np.array([1/u[:3].sum(), 1/u[:3].sum(), \
                                                 1/u[:3].sum(), -1/u[3:].sum(), \
                                                 -1/u[3:].sum(), -1/u[3:].sum()]) / 3, P), v) == 0]
    prob = cp.Problem(objective, constraints)
    result = prob.solve(solver=cp.SCS)

    p_matrix = P.value

    print("MATRICE PROBABILITA %s\n" % p_matrix)
    for i in range(p_matrix.shape[0]):
        for j in range(p_matrix.shape[1]):
            if p_matrix[i][j] < 0:
                p_matrix[i][j] = 0

    p_matrix = np.around(p_matrix, decimals=4)

    sk = skp.SinkhornKnopp()

    ## I try to find the matrix each time by transposing it. This allows you to better adapt the values
    ## change them just a little such that the sum is 1. Thanks to https://github.com/btaba/sinkhorn_knopp
    ## I use 100 iterations for train the system
    for i in range(100):
        p_matrix = sk.fit(p_matrix.T)
    print(np.sum(p_matrix, axis=0))
    print(np.sum(p_matrix, axis=1))
    print('\n %s' % p_matrix)
    return p_matrix

