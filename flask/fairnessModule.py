import findProbMatrix as fp
import numpy as np
import numpy.random as rn

from birkhoff import birkhoff_von_neumann_decomposition

def fairnessMethod(hits=[], type=1):

    p_matrix = fp.findProbMatrix(hits, type)

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