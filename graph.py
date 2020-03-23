import math

def euclid(p,q):
    x = p[0]-q[0]
    y = p[1]-q[1]
    return math.sqrt(x*x+y*y)
                
class Graph:

    # Complete as described in the specification, taking care of two cases:
    # the -1 case, where we read points in the Euclidean plane, and
    # the n>0 case, where we read a general graph in a different format.
    # self.perm, self.dists, self.n are the key variables to be set up.
    def __init__(self,n,filename):
        if (n == -1):
            pairs = g(filename)
            self.n = len(pairs)
            self.perm = [0]*self.n
            self.dists = [[0]*self.n for i in range(self.n)]
            for i in range(self.n):
                self.perm[i] = i
                for j in range(self.n):
                    self.dists[i][j] = euclid(pairs[i], pairs[j])
        else:
            file = open(filename, 'r')
            reader = file.readlines()
            self.n = n
            self.perm = [0]*self.n
            for i in range(self.n):
                self.perm[i] = [i]
                for j in range(self.n):
                    self.dists[i][j] = 3
            
             

    # Complete as described in the spec, to calculate the cost of the
    # current tour (as represented by self.perm).
    def tourValue(self):
        tourlength = 0
        for i in range(self.n-1):
            tourlength += self.dists[self.perm[i]][self.perm[i+1]]
        tourlength += self.dists[self.perm[-1]][self.perm[0]]
        return tourlength

    # Attempt the swap of cities i and i+1 in self.perm and commit
    # commit to the swap if it improves the cost of the tour.
    # Return True/False depending on success.
    #def trySwap(self,i):


    # Consider the effect of reversiing the segment between
    # self.perm[i] and self.perm[j], and commit to the reversal
    # if it improves the tour value.
    # Return True/False depending on success.              
    #def tryReverse(self,i,j):


    def swapHeuristic(self):
        better = True
        while better:
            better = False
            for i in range(self.n):
                if self.trySwap(i):
                    better = True

    def TwoOptHeuristic(self):
        better = True
        while better:
            better = False
            for j in range(self.n-1):
                for i in range(j):
                    if self.tryReverse(i,j):
                        better = True
                

    # Implement the Greedy heuristic which builds a tour starting
    # from node 0, taking the closest (unused) node as 'next'
    # each time.
    #def Greedy(self):

def g(filename):
    file = open(filename, 'r')
    something = file.readlines()
    something = [x.strip() for x in something]
    n = len(something)
    list2 = []
    for i in range(n):
        list2 = list2 + something[i].split()
    list3 = [int(x) for x in list2]
    list6 = []
    for i in range(0,2*n,2):
        list6.append((list3[i],list3[i+1]))
    return list6