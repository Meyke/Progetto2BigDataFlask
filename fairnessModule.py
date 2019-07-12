
import fairProva as fp
import numpy as np

from birkhoff import birkhoff_von_neumann_decomposition

def fairnessMethod(hits=[]):
    #for hit in hits:
    #    hit['_source']['title'] = hit['_source']['title'] + " (fair ahahahaha)"
    #return hits

    u = np.array((0.81, 0.80, 0.79, 0.78, 0.77, 0.76))
    return fp.findProbMatrix(u)


if __name__ == "__main__":
    p_matrix = fairnessMethod()
    print("MATRICE PROBABILITA %s" % p_matrix)

    print('\n ##### Compute the Birkhoff-von Neumann decomposition P = θ1P1 +θ2P2 +···+ θnPn  ##### \n')
    result = birkhoff_von_neumann_decomposition(p_matrix)
    for coefficient, permutation_matrix in result:
        print('coefficient:', coefficient)
        print('permutation matrix:', permutation_matrix)

## TO DO:
# parametrization of groups in u, according to news editors

# (4) Sample permutation matrix Pi with probability proportional to θi and display the corresponding ranking ri .

# 4 CONSTRUCTING GROUP FAIRNESS CONSTRAINTS