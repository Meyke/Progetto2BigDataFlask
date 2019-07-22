import cvxpy as cp
import numpy as np
from sinkhorn_knopp import sinkhorn_knopp as skp

#u = np.array((0.81, 0.80, 0.79, 0.78, 0.77, 0.76))
# u = np.array((0.81, 0.80, 0.79, 0.78, 0.77, 0.0))

#ATTENZIONE, PARAMETRIZZARE I GRUPPI. QUI FA :3, PERCHè HO DUE GRUPPI DA 3 (I PRIMI 3 E GLI ULTIMI 3)


def findProbMatrix(hits,type):

    scores = []
    publications = {}
    current_score = 0
    max_score = hits[0]['_score']
    for hit,i in zip(hits, range(len(hits))):
        score = hit['_score']/max_score
        scores.append(score)
        publication = hit['_source']['publication']
        if publication in publications:
            info = publications.get(publication)
            info.increaseValue(score,i)
        else:
            publications[publication] = PublicationInfo(score,1,[i])

    norm = np.array(scores)
    u = np.around(norm, decimals=2)
    print(u)

    v = np.array([1.0/(np.log(2 + i)) for i, _, in enumerate(u)])
    P = cp.Variable((len(u), len(u)))
    objective = cp.Maximize(cp.matmul(cp.matmul(u, P), v))
    constraints = [cp.matmul(np.ones((1,len(u))), P) == np.ones((1,len(u))),
                   cp.matmul(P, np.ones((len(u),))) == np.ones((len(u),)),
                   0 <= P, P <= 1]

    list_publications = list(publications.keys())
    for publication in list_publications:
        list_publications.remove(publication)
        occurrences = publications.get(publication).getOccurrences()
        positions1 = publications.get(publication).getPositions()
        for second_publication in list_publications:
            values = []
            positions = []
            for i in positions1:
                if type == 1:
                    values.append(1/occurrences)
                elif type == 2:
                    values.append(1/round(publications.get(publication).getScore(),0))
                else:
                    values.append(round(scores[i],0)/round(publications.get(publication).getScore(),0))
            second_occurrences = publications.get(second_publication).getOccurrences()
            positions2 = publications.get(second_publication).getPositions()
            for j in positions2:
                if type == 1:
                    values.append(-1/second_occurrences)
                elif type == 2:
                    values.append(-1/round(publications.get(second_publication).getScore(),0))
                else:
                    values.append(-round(scores[j],0)/round(publications.get(second_publication).getScore(),0))
            positions = positions1 + positions2
            print(values)
            positions.sort()
            constraints.append(cp.matmul(cp.matmul(np.array(values), P[positions]), v) == 0)




    prob = cp.Problem(objective, constraints)
    result = prob.solve(solver=cp.SCS)

    p_matrix = P.value
    print(p_matrix)

    print("MATRICE PROBABILITA %s\n" % p_matrix)
    for i in range(p_matrix.shape[0]):
        for j in range(p_matrix.shape[1]):
            if p_matrix[i][j] < 0:
                p_matrix[i][j] = 0

    p_matrix = np.around(p_matrix, decimals=4)

    sk = skp.SinkhornKnopp()

    ## I try to find the matrix each time by transposing it. This allows you to better adapt the values
    ## change them just a little such that the sum is 1. Thanks to https://github.com/btaba/sinkhorn_knopp
    ## I use 1000 iterations for train the system
    for i in range(1000):
        p_matrix = sk.fit(p_matrix.T)
    print(np.sum(p_matrix, axis=0))
    print(np.sum(p_matrix, axis=1))
    print('\n %s' % p_matrix)
    return p_matrix        

class PublicationInfo:
    def __init__(self, sum_score: float, occurences, positions):
        self.sum_score = sum_score
        self.occurences = occurences
        self.positions = positions

    def increaseValue(self, score: float, position):
        self.sum_score += score
        self.occurences += 1
        self.positions.append(position)
    
    def getOccurrences(self):
        return self.occurences

    def getPositions(self):
        return self.positions

    def getScore(self):
        return self.sum_score

    def __repr__(self):
        return str(self.__dict__)

