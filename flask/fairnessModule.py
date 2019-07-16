
import findProbMatrix as fp
import numpy as np
import numpy.random as rn

from birkhoff import birkhoff_von_neumann_decomposition

class PubblicationInfo:
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


def fairnessMethod(hits=[], type=1):
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
            publications[publication] = PubblicationInfo(score,1,[i])



    u = np.array(scores)
    norm = np.around(u, decimals=2)
    print(norm)

    p_matrix = fp.findProbMatrix(norm, publications, type)

    print("MATRICE PROBABILITA %s" % p_matrix)

    print('\n ##### Compute the Birkhoff-von Neumann decomposition P = θ1P1 +θ2P2 +···+ θnPn  ##### \n')
    result = birkhoff_von_neumann_decomposition(p_matrix)
    for coefficient, permutation_matrix in result:
        print('coefficient:', coefficient)
        print('permutation matrix:', permutation_matrix)

    print('\n ##### Sample permutation matrix Pi with probability proportional to θi and display the corresponding ranking ri  ##### \n')

    weights, matrices = zip(*result)
    index = rn.choice(len(result), 1, p=weights)[0]
    print(index)
    ranking = matrices[index]
    ranking_indexes = np.where(ranking)[1]
    return reorder(hits, ranking_indexes, len(hits))


# Function to reorder elements of arr[] according 
# to index[] 
def reorder(arr, index, n): 
  
    # Fix all elements one by one 
    for i in range(0,n): 
  
           #  While index[i] and arr[i] are not fixed 
           while (index[i] != i): 
          
               # Store values of the target (or correct)  
               # position before placing arr[i] there 
               oldTargetI = index[index[i]] 
               oldTargetE = arr[index[i]] 
  
               # Place arr[i] at its target (or correct) 
               # position. Also copy corrected index for 
               # new position 
               arr[index[i]] = arr[i] 
               index[index[i]] = index[i] 
  
               # Copy old target values to arr[i] and 
               # index[i] 
               index[i] = oldTargetI 
               arr[i] = oldTargetE
               return arr 

if __name__ == "__main__":
    fairnessMethod()


## TO DO:
# parametrization of groups in u, according to news editors

# (4) Sample permutation matrix Pi with probability proportional to θi and display the corresponding ranking ri .

# 4 CONSTRUCTING GROUP FAIRNESS CONSTRAINTS